#! /usr/bin/python
"""
Varmint Pest - Attempts to frighten away varmints such as raccoons
Created 7/04/17 by Greg Griffes  
"""
import time, sys, os
##import RPi.GPIO as GPIO
##import pigpio # http://abyz.co.uk/rpi/pigpio/python.html
##import spidev
##import Adafruit_ADS1x15
##from collections import deque
##import threading
##import logging
##import datetime
##from picamera import PiCamera

# for graphics
##from webcolors import name_to_rgb
##import pygame
##from pygame.locals import *

# Global variables
##global flow_count
##flow_count = 0

#camera = PiCamera()

# Provides a logging solution for troubleshooting
logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')

# -----------------------------------
# Constants
# -----------------------------------

# -----------------------------------
# Initialize
# -----------------------------------

##########################
class one(object):
##########################

    def __init__(self, flow_zone, flow_queue):
        self.flow_zone = flow_zone
        self.flow = flow_queue
      
    def __del__(self):
        print 'flow '+str(self.flow_zone)+' closed'

    def flow_calculator (self, freq):
        LPM2GPM = 0.264172  # Liters per minute to gallons per minute factor
    #    return (LPM2GPM*(freq/5.5))    # in GPM
        return float(freq/5.5)               # in LPM


###############################################################
# Main program
###############################################################
if __name__ == '__main__':

# -----------------------------------
# Initialize variables
# -----------------------------------


# -----------------------------------
# Exception handler
# -----------------------------------
    try:

        logging.debug('valves[] = '+str(valves))

# -----------------------------------
# Create objects
# -----------------------------------
    # create the objects
        valve_power_object = []
        valve_current_object = []
        for v in range(NUMBER_OF_VALVES):
            valve_power_object.append(valve_power(v, valves[v][VALVE_GPIO]))
            valve_current_object.append(valve_current(v))

# -----------------------------------
# Create and start daemons
# -----------------------------------

# -----------------------------------
# Create and start graphics
# -----------------------------------

###############################################################
# Main loop
###############################################################

        loop = 0    # used to determine the first time through each valve_status change
        
        while True:         #Demo loop

            # note start time
            start_time = time.time()

            


            # note end time
            end_time = time.time()
            # work out elapsed time                                                       
            elapsed_time = (end_time - start_time)
            print ("Elapsed time = "+str(elapsed_time))
   
###########################################################
# END
###########################################################
    except KeyboardInterrupt:
        exit()

    except:

    # normal exit
