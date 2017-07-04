#! /usr/bin/python
"""
Varmint Pest - Attempts to frighten away varmints such as raccoons
Created 7/04/17 by Greg Griffes  
"""
import time, sys, os
import logging

from automat import MethodicalMachine

##import RPi.GPIO as GPIO
##import pigpio # http://abyz.co.uk/rpi/pigpio/python.html
##import spidev
##import Adafruit_ADS1x15
##from collections import deque
##import threading

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
# =======================================
# Local classes
# =======================================
class _heating_element(object):
    # Create the heating element class

    def turn_on(self):
        logging.debug("turning on the heating element")


##########################
class varmintpest_fsm(object):
##########################
# Create the state machine class from Automat
    _machine = MethodicalMachine()

    #=======================================
    # Inputs
    #=======================================
    @_machine.input()
    def brew_button(self):
        "The user has pressed the brew button"

    @_machine.input()
    def put_in_beans(self):
        "The user put in some beans"

    #=======================================
    # Outputs
    #=======================================
    @_machine.output()
    def _heat_the_element(self):

        self.he = _heating_element()
        "heat up the element"
        self.he.turn_on()

    #=======================================
    # States
    #=======================================
    @_machine.state()
    def have_beans(self):
        "In this state you have beans"

    @_machine.state(initial=True)
    def dont_have_beans(self):
        "in this state, you don't have beans"

    #=======================================
    # Transition logic
    #=======================================

    dont_have_beans.upon(put_in_beans, enter=have_beans, outputs=[])
    have_beans.upon(brew_button, enter=dont_have_beans, outputs=[_heat_the_element])

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

        logging.debug('debug logging is on')

# -----------------------------------
# Create objects
# -----------------------------------
        varmintpest = varmintpest_fsm()
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

            varmintpest.put_in_beans()
            varmintpest.brew_button()
            
            time.sleep(3.0)


            # note end time
            end_time = time.time()
            # work out elapsed time                                                       
            elapsed_time = (end_time - start_time)
            logging.debug("Elapsed time = "+str(elapsed_time))
   
###########################################################
# END
###########################################################
    except KeyboardInterrupt:
        logging.debug("Keyboard Interrupt exception!")
        exit()

    except BaseException as e:
        logging.error('General exception!: ' + str(e))

    # normal exit
