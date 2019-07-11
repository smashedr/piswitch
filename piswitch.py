import logging
import os
import re
import redis
import sys
import time
from keyboard import Keyboard
from systemd.journal import JournalHandler
import systemd.daemon

TWITCH_USER = os.environ.get('TWITCH_USER')
REDIS_PASS = os.environ.get('REDIS_PASS')
REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = int(os.environ.get('REDIS_PORT', 6379))
REDIS_DB = int(os.environ.get('REDIS_DB', 2))

log_format = '%(levelname)s %(module)s:%(lineno)d - %(message)s'
journald_handler = JournalHandler()
journald_handler.setFormatter(logging.Formatter(log_format))
logger = logging.getLogger(__name__)
logger.addHandler(journald_handler)
logger.setLevel(logging.INFO)


if __name__ == '__main__':
    keyboard = Keyboard()
    r = redis.StrictRedis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        db=REDIS_DB,
        password=REDIS_PASS,
    )
    p = r.pubsub()
    p.subscribe(TWITCH_USER)
    systemd.daemon.notify('READY=1')
    while True:
        try:
            message = p.get_message()
            if message:
                logger.info(message)
                if message['type'] == 'message':
                    data = message['data'].decode()
                    level_id = ''.join(re.findall('[a-zA-Z0-9]+', data))
                    logger.info(level_id)
                    keyboard.write('{}\n'.format(level_id))
            time.sleep(1)
        except (KeyboardInterrupt, SystemExit):
            logger.info('Caught exit signal. Shutting down...')
            sys.exit(0)
        except Exception as error:
            logger.exception(error)
            logger.error('Caught Exception: {}'.format(error))
            time.sleep(1)
            continue
