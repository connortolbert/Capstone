import time
#import numpy as np
#import threading
#import math
#import csv

#Import Internal Items
import L1_motor as motors
#import L2_speed_control as sc
#import L2_inverse_kinematics as inv
#import L2_kinematics as kin
#import L2_log as log
#import L3_follow as follow
#import L2_track_target as track

if __name__ == "__main__":
    while(1):
        print("Spin Agitator motor Forward")
        motors.FlyWheel(1)
        time.sleep(.1)
        motors.Agitator(.5)
        time.sleep(.1)
        motors.FlyWheel(0)
        time.sleep(1)
        motors.Agitator(0)
        time.sleep(1)
        motors.FlyWheel(0)
        time.sleep(3)
