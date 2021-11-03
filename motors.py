# Motors Program for SCUTTLE running RasPi
# This example sends commands to two motors on the appropriate pins for H-bridge
# For pin mapping, see Wiring Guide Pi on the SCUTTLE webpage.
# Last update: 2020.11 with improved PWM method

# Import external libraries
import gpiozero                             # used for PWM outputs
from gpiozero import PWMOutputDevice as pwm # for driving motors, LEDs, etc
import time                                 # for keeping time
import numpy as np                          # for handling arrays

frq = 150                                   # motor driving frequency
# Broadcom (BCM) pin numbering for RasPi is as follows: PHYSICAL:       NAME:
left_chA  = pwm(17, frequency=frq,initial_value=0)     # PIN 11        GPIO17
left_chB  = pwm(18, frequency=frq,initial_value=0)     # PIN 12        GPIO18
right_chA = pwm(22, frequency=frq,initial_value=0)     # PIN 15        GPIO22
right_chB = pwm(23, frequency=frq,initial_value=0)     # PIN 16        GPIO23

flywheel1 = pwm(9, frequency=frq,initial_value=0)     # PIN 21        GPIO9
flywheel2 = pwm(25, frequency=frq,initial_value=0)     # PIN 22        GPIO25
agitator1 = pwm(19, frequency=frq,initial_value=0)     # PIN 35        GPIO19
agitator2 = pwm(16, frequency=frq,initial_value=0)     # PIN 36        GPIO16

def computePWM(speed):              # take an argument in range [-1,1]
    if speed == 0:
        x = np.array([0,0])         # set all PWM to zero
    else:
        x = speed + 1.0             # change the range to [0,2]
        chA = 0.5 * x               # channel A sweeps low to high
        chB = 1 - (0.5 * x)         # channel B sweeps high to low
        x = np.array([chA, chB])    # store values to an array
        x = np.round(x,2)           # round the values
    return(x)

def sendLeft(mySpeed):          # takes at least 0.3 ms
    myPWM = computePWM(mySpeed)
    left_chB.value = myPWM[0]
    left_chA.value = myPWM[1]

def sendRight(mySpeed):         # takes at least 0.3 ms
    myPWM = computePWM(mySpeed)
    right_chB.value = myPWM[0]
    right_chA.value = myPWM[1]

def FlyWheel(mySpeed):          # takes at least 0.3 ms
    myPWM = computePWM(mySpeed)
    flywheel2.value = myPWM[0]
    flywheel1.value = myPWM[1]

def Agitator(mySpeed):         # takes at least 0.3 ms
    myPWM = computePWM(mySpeed)
    agitator2.value = myPWM[0]
    agitator1.value = myPWM[1]
    
def Test():
        #time.sleep(10)
        #print("Move Forward")
        #sendLeft(-0.8)
        #sendRight(0.8)
        #time.sleep(3)
        #print("Stop Movement")
        #sendLeft(0)
        #sendRight(0)
        #time.sleep(5)
        print("Shoot")
        Agitator(-.7)
        FlyWheel(1)
        time.sleep(3)
        print("Off")
        Agitator(0)
        FlyWheel(0)
        time.sleep(0)

# THIS LOOP ONLY RUNS IF THE PROGRAM IS CALLED DIRECTLY
if __name__ == "__main__":
    myRate = 0.
    while(1):
        #print("motors.py: driving fwd")
        #sendLeft(0.8)
        #sendRight(0.8)
        #time.sleep(4)                       # run fwd for 4 seconds
        #print("motors.py: driving reverse")
        #sendLeft(-0.8)
        #sendRight(-0.8)
        #time.sleep(4)                       # run reverse for 4 seconds
        #print("stopping motors 4 seconds")
        #sendLeft(0)
        #sendRight(0)
        #time.sleep(4)
        print("Test")
        sendLeft(-0.8)
        sendRight(0.8)
        #Agitator(-.5)
        #FlyWheel(.8)
        time.sleep(2)
        print("OFF")
        sendLeft(0)
        sendRight(0)
        Agitator(0)
        FlyWheel(0)
        time.sleep(5)
        