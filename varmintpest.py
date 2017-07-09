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
    """varmintpest_fsm is a state machine using the Automat MethodicalMachine
    There are three states:
    S1: Daytime (the initial state)
    S2: Nighttime-motion (waiting for motion)
    S3: Nighttime-IR (upon IR signature, set off the varmint blast)

    State: S1 (Daytime) parameters:
        S1I1: Input 1: daylight-yes
        S1I2: Input 2: daylight-no

        S1T1: Transition 1: upon daylight-yes
            S1O1: Output 1: Play bird songs
            S1T1ns: Next state: enter daytime
        S1T2: Transition 2: upon daylight-no
            S1O2: Output 2: message entering nighttime and test for motion
            S1T2ns: Next state: enter nighttime-motion

    State: S2 (nighttime-motion) parameters:
        S2I1: Input 1: daylight-yes
        S2I2: Input 2: daylight-no
        S2I3: Input 3: motion-detected
        S2I4: Input 4: motion-not-detected

        S2T1: Transition 1: upon daylight-yes
            S2O1: message start of daytime
            S2T1ns: enter S1 daytime
        S2T2: Transition 2: upon daylight-no
            S2T2ns: enter S2 nighttime-motion
        S2T3: Transition 3: upon motion-detected
            S2O2: message motion detected
            S2T3ns: enter S3 nighttime-IR
        S2T4: Transition 4: upon motion-not-detected
            S2T4ns: enter S2 nighttime-motion

     State: S3 (Nighttime-IR) parameters:
        S3I1: Input 1: IR-detected
        S3I2: Input 2: IR-not-detected

        S3T1: Transition 1: upon IR-detected
            S3O1: Output 1: Perform Varmint-blast
            S3T1ns: Next state: enter nighttime-motion
        S3T2: Transition 2: upon IR-not-detected
            S3O2: Output 2: log false-motion-detection
            S3T2ns: Next state: enter S2 nighttime-motion


    """

# Create the state machine class from Automat
    _machine = MethodicalMachine()

#=======================================
# Inputs
#=======================================
    @_machine.input()
    def daylightYes(self):
        "Light sensor indicates day time"

    @_machine.input()
    def daylightNo(self):
        "Light sensor indicates night time"

    @_machine.input()
    def motionDetected(self):
        "Motion - possible varmint"

    @_machine.input()
    def motionNotDetected(self):
        "Nothing found, keep looking"

    @_machine.input()
    def IRDetected(self):
        "IR signature indicates varmint"

    @_machine.input()
    def IRNotDetected(self):
        "Nothing found, keep looking"


#=======================================
# Outputs
#=======================================
    @_machine.output()
    def _play_bird_sounds(self):
        logging.debug('playing bird sounds')
        time.sleep(1.0)

    @_machine.output()
    def _nighttime(self):
        logging.debug('entering nighttime-motion state')
        time.sleep(1.0)

    @_machine.output()
    def _messageStartOfDaytime(self):
        logging.debug('entering daytime state')
        time.sleep(1.0)

    @_machine.output()
    def _messageMotionDetected(self):
        logging.debug('Motion detected! Entering motion-IR state')
        time.sleep(1.0)

    @_machine.output()
    def _performVarmintBlast(self):
        logging.debug('IR detected! Performing Varmint Blast!')
        time.sleep(1.0)

    @_machine.output()
    def _messageFalseMotionDetected(self):
        logging.debug('Motion detected but no IR signature')
        time.sleep(1.0)


#=======================================
# S1 State
#=======================================
    @_machine.state(initial=True)
    def daytime(self):
        "wait for nighttime"

#=======================================
# S2 State - nighttime-motion
#=======================================
    @_machine.state()
    def nighttimeMotion(self):
        "wait for motion or daytime"

#=======================================
# S3 State - nighttime-IR
#=======================================
    @_machine.state()
    def nighttimeIR(self):
        "wait for IR signature"


#=======================================
# S1 Transition logic
#=======================================
    daytime.upon(daylightYes, enter=daytime, outputs=[_play_bird_sounds])
    daytime.upon(daylightNo, enter=nighttimeMotion, outputs=[_nighttime])

#=======================================
# S2 Transition logic
#=======================================
    nighttimeMotion.upon(daylightYes, enter=daytime, outputs=[_messageStartOfDaytime])
    nighttimeMotion.upon(daylightNo, enter=nighttimeMotion, outputs=[])
    nighttimeMotion.upon(motionDetected, enter=nighttimeIR, outputs=[_messageMotionDetected])
    nighttimeMotion.upon(motionNotDetected, enter=nighttimeMotion, outputs=[])

#=======================================
# S3 Transition logic
#=======================================
    nighttimeIR.upon(IRDetected, enter=nighttimeMotion, outputs=[_performVarmintBlast])
    nighttimeIR.upon(IRNotDetected, enter=nighttimeMotion, outputs=[_messageFalseMotionDetected])

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
#        daylight_sensor = _daylight_sensor()

# -----------------------------------
# Create and start daemons
# -----------------------------------

# -----------------------------------
# Create and start graphics
# -----------------------------------

###############################################################
# Main program
###############################################################

        varmintpest.daylightYes()       # move to day time state
        varmintpest.daylightNo()        # move to night time state

        varmintpest.motionNotDetected() # move to day time state
        varmintpest.motionNotDetected() # move to day time state
        varmintpest.motionNotDetected() # move to day time state
        varmintpest.motionNotDetected() # move to day time state

        varmintpest.motionDetected() # move to day time state

        varmintpest.IRNotDetected() # move to day time state

        varmintpest.motionDetected() # move to day time state

        varmintpest.IRDetected() # move to day time state

        varmintpest.motionNotDetected() # move to day time state
        varmintpest.motionNotDetected() # move to day time state
        varmintpest.motionNotDetected() # move to day time state
        varmintpest.motionNotDetected() # move to day time state

        varmintpest.daylightYes() # move to day time state

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
