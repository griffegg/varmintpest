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
NIGHT = 0
DAY = 1

# -----------------------------------
# Initialize
# -----------------------------------
# =======================================
# Local classes
# =======================================
class _daylight_sensor(object):
    # Create the daylight sensor class
    def __init__(self):
        self.night = NIGHT
        self.day = DAY

    def __del__(self):
        logging.debug('daylight sensor class closed')

    def read(self):
        logging.debug("Daylight sensor indicates night time")
        return self.night

##########################
class varmintpest_fsm(object):
##########################
# Create the state machine class from Automat
    _machine = MethodicalMachine()

    #=======================================
    # Inputs
    #=======================================
    @_machine.input()
    def day_detected(self):
        "Light sensor indicates day time"

    @_machine.input()
    def night_detected(self):
        "Light sensor indicates night time"

    #=======================================
    # Outputs
    #=======================================
    @_machine.output()
    def _play_bird_sounds(self):
        logging.debug('playing bird sounds')
        time.sleep(2.0)

    @_machine.output()
    def _varmint_hunting(self):
        logging.debug('hunting varmints')
        time.sleep(2.0)

    #=======================================
    # States
    #=======================================
    @_machine.state(initial=True)
    def daytime(self):
        "In this state, do daytime things"

    @_machine.state()
    def nighttime(self):
        "in this state, do night time things"

    #=======================================
    # Transition logic
    #=======================================

    daytime.upon(night_detected, enter=nighttime, outputs=[_varmint_hunting])
    nighttime.upon(day_detected, enter=daytime, outputs=[_play_bird_sounds])

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
        daylight_sensor = _daylight_sensor()

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

        daylight_status = DAY

        while True:         #Demo loop

# intial state is daytime
            if daylight_sensor.read() == NIGHT and daylight_status == DAY:
                daylight_status = NIGHT
                varmintpest.night_detected()    # move to night time state
            elif daylight_sensor.read() == DAY and daylight_status == NIGHT:
                daylight_status = DAY
                varmintpest.day_detected()      # move to day time state
            else:
                time.sleep(3.0)

###########################################################
# END
###########################################################
    except KeyboardInterrupt:
        logging.debug("Keyboard Interrupt exception!")
        exit()

    except BaseException as e:
        logging.error('General exception!: ' + str(e))

    # normal exit
