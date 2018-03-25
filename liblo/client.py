#!/usr/bin/python3

# requirements
import liblo
import logging
from random import random, randint
 
# configure logger
logger = logging.getLogger('pyliblo')
logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.DEBUG)
logging.debug("Logging subsystem initialized")

# send 10 packets
for i in range(10):

    # send message "/foo/message1" with int, float and string arguments
    logging.debug("Sending test message %s" % i)
    try:
        i = randint(0,100)
        f = random()
        liblo.send(liblo.Address(1234), "/example", i, f)
    except:
        logging.error("Error while sending message")
        
# bye!
logging.debug("Bye!")
