# This script is from Lab 6 of MXET 300, "Lab6Template.py"

# Import External Items
import time
import numpy as np
import threading
import math
import csv

# Import Internal Items
import L2_speed_control as sc
import L2_inverse_kinematics as inv
import L2_kinematics as kin


# import L2_log as log

def loop_drive(pdT):
    count = 0
    # Initialize Variables for Control System
    t0 = 0  # time sample
    t1 = 1  # time sample
    e00 = 0  # error sample
    e0 = 0  # error sample
    e1 = 1  # error sample
    dt = 0  # delta in time
    de_dt = np.zeros(2)  # initialize the de_dt

    while (1):
        count += 1

        # This code is used for open and closed loop control
        pdTargets = pdT  # desired PhiDots
        pdCurrents = kin.getPdCurrent()  # current PhiDots

        # Updating Control System Variables
        t0 = t1  #
        t1 = time.time()  #
        dt = t1 - t0  # calculating dt
        e00 = e0  # assigning previous previous error
        e0 = e1  # assigning previous error
        e1 = pdCurrents - pdTargets  # calculating current error
        de_dt = (e1 - e0) / dt

        # Driving
        sc.driveClosedLoop(pdTargets, pdCurrents, de_dt)
        time.sleep(0.05)
        return

        # outputs DATA to csv file
        # if count == 1:
        #  log.clear_file()
        #   log.csv_write([count, pdCurrents[0], pdTargets[0]])
        # elif count > 1 and <= 400:
        #    log-csv_write ([count, pdCurrents[0], pdTargets[0]])

# loop_drive()