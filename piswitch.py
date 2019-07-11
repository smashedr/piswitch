import logging
import os
import re
import redis
import time
from keyboard import Keyboard

TWITCH_USER = os.environ.get('TWITCH_USER')
REDIS_PASS = os.environ.get('REDIS_PASS')
REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = int(os.environ.get('REDIS_PORT', 6379))
REDIS_DB = int(os.environ.get('REDIS_DB', 2))

logger = logging.getLogger('piswitch')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('queue.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


if __name__ == '__main__':
    keyboard = Keyboard()
    r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, password=REDIS_PASS)
    p = r.pubsub()
    p.subscribe(TWITCH_USER)
    while True:
        message = p.get_message()
        if message:
            logger.info(message)
            if message['type'] == 'message':
                data = message['data'].decode()
                logger.info(data)
                level_id = ''.join(re.findall('[a-zA-Z0-9]+', data))
                logger.info(level_id)
                keyboard.write('{}\n'.format(level_id))
        time.sleep(1)
