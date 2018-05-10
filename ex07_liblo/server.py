#!/usr/bin/python3

# requirements
import sys
import liblo
import logging

# configure logger
logger = logging.getLogger('pyliblo')
logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.DEBUG)
logging.debug("Logging subsystem initialized")

# create server
try:
    server = liblo.Server(8000)
except liblo.ServerError as err:
    print(err)
    sys.exit()

# create an handler
def myCallback(path, args):
    f1, f2 = args
    logging.debug("New request on %s" % path)
    logging.debug("The float argument 2 is: %s" % f1)
    logging.debug("The float argument 2 is: %s" % f2)
    
# create a fallback handler
def myFallbackCallback(path, args, types, src, data):
    logging.error("Unsupported message")
    
# register method taking an int and a float
server.add_method("/rate_intensity", 'ff', myCallback)

# register a fallback for unhandled messages
server.add_method(None, None, myFallbackCallback)

# loop and dispatch messages every 100ms
while True:
    server.recv(100)
