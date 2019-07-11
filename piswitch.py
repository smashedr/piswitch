import json
import logging
import os
import redis
import time
from keyboard import Keyboard

TWITCH_USER = os.environ.get('TWITCH_USER')
REDIS_PASS = os.environ.get('REDIS_PASS')
REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = int(os.environ.get('REDIS_PORT', 6379))

logger = logging.getLogger('piswitch')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('queue.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


if __name__ == '__main__':
    keyboard = Keyboard()
    r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=2, password=REDIS_PASS)
    p = r.pubsub()
    p.subscribe(TWITCH_USER)
    while True:
        message = p.get_message()
        if message:
            logger.info(message)
            if message['type'] == 'message':
                data = message['data'].decode()
                message = json.loads(data)
                logger.info(message)
                # keyboard.write('G5S1MLBTG\n')
        time.sleep(2)
