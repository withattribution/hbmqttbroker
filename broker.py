import logging
import asyncio
import os
from hbmqtt.broker import Broker
import netifaces as ni

logger = logging.getLogger(__name__)
MQTT_PORT = '4444'

#import socket
#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.connect(("8.8.8.8", 80))
#print(s.getsockname()[0])
#localIP = s.getsockname()[0]
#s.close()

config = {
    'listeners': {
        'default': {
            'type': 'tcp',
            'bind': ni.ifaddresses('wlan0')[2][0]['addr'] +':'+ MQTT_PORT,
        },
        'ws-mqtt': {
            'bind': '127.0.0.1:8083',
            'type': 'ws',
            'max_connections': 10,
        },
    },
    'sys_interval': 10,
    'auth': {
        'allow-anonymous': True,
        'password-file': os.path.join(os.path.dirname(os.path.realpath(__file__)), "passwd"),
        'plugins': [
            'auth_file', 'auth_anonymous'
        ]
    }
}

broker = Broker(config)

@asyncio.coroutine
def broker_coro():
    yield from broker.start()
    #yield from asyncio.sleep(5)
    #yield from broker.shutdown()


if __name__ == '__main__':
    formatter = "[%(asctime)s] :: %(levelname)s :: %(name)s :: %(message)s"
    #formatter = "%(asctime)s :: %(levelname)s :: %(message)s"
    logging.basicConfig(level=logging.INFO, format=formatter)
    asyncio.get_event_loop().run_until_complete(broker_coro())
    asyncio.get_event_loop().run_forever()

