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
import L3_follow as follow
import L2_track_target as track

# Declare relevant variables
radius = 0  # radius of target
cruiseRate = 0.6  # speed for cruising (fraction)
r1 = 28  # radius desired (pixels)
tol = 3  # radius tolerance (pixels)


def turnAndGo(x_range):  # turn towards object and approach

    xVal = 0.4 * x_range  # scale down for slower turns
    yVal = 0.8 * x_range
    zVal = 0.6 * x_range
    centerBand = 0.15  # in this band, don't turn
    # if 0.4 > abs(x_range) > centerBand:                               # outside the band, make a turn
    #     print("small TURN")
    #     chassisTargets = inv.map_speeds(np.array([0, xVal]))    # generate xd, td
    #     print(chassisTargets, "\n")

    if abs(x_range) > 0.4:  # outside the band, make a turn
        print("BIG TURN")
        chassisTargets = inv.map_speeds(np.array([0, zVal]))  # generate xd, td
        print(chassisTargets, "\n")

    else:
        print("forward")
        xdt = forwardFunction(radius)  # determine forward speed
        chassisTargets = inv.map_speeds(np.array([xdt, 0]))  # set td zero
        print(chassisTargets, "\n")

    return chassisTargets

    # dont use turn&go definition
    # pdtarget or chassistarget aren't updating figure out
    # hard coded the xval and yval values (based off of the maximum pd value connor did)


def turn_test(x_range):
    duty_l = round((x_range - 0.5 * 240))


def forwardFunction(r0):  # when the target is straight on, approach
    xdt = 0  # initial x_dot target is zero
    if r0 < (r1 - tol):  # if target looks too small
        xdt = cruiseRate  # x_dot target, drive fwd
    elif r0 > (r1 + tol):  # if target looks too big
        xdt = -1 * cruiseRate  # x_dot target, drive backwards
    return xdt


def loop_drive(color_target):
    count = 0
    # Initialize Variables for Control System
    t0 = 0  # time sample
    t1 = 1  # time sample
    e00 = 0  # error sample
    e0 = 0  # error sample
    e1 = 1  # error sample
    dt = 0  # delta in time
    de_dt = np.zeros(2)  # initialize the de_dt

    while (color_target[0] != None):
        count += 1
        print('\nCount: ', count)

        # This code is used for open and closed loop control
        pdCurrents = kin.getPdCurrent()  # current PhiDots

        # if target[0] is None:                                   # if there is no colored target detected
        #     print("no target located. loop")                         # do not drive
        #     stop = (0,0)
        #     sc.driveOpenLoop(stop)                         # command motors in open-loop fashion

        x_range = track.getAngle(color_target[0])  # find out the angle of the target
        radius = color_target[2]  # find out the radius of the target
        print("Target position: ", x_range, "\t radius", radius)
        chassisTargets = turnAndGo(x_range)  # take the x target location & generate turning
        pdTargets = inv.convert(chassisTargets)  # phi dot targets (rad/s) [for open loop?]
        # print("pdTargets: ", pdTargets)

        # Updating Control System Variables
        t0 = t1  #
        t1 = time.time()  #
        dt = t1 - t0  # calculating dt
        e00 = e0  # assigning previous previous error
        e0 = e1  # assigning previous error
        e1 = pdCurrents - pdTargets  # calculating current error
        de_dt = (e1 - e0) / dt
        # Driving

        print("pdTargets: ", pdTargets, "pdCurrents: ", pdCurrents)
        sc.driveClosedLoop(pdTargets, pdCurrents, de_dt)
        print("Driving")
        time.sleep(0.05)
        color_target = track.colorTarget(follow.Blue)


def openloop_drive(color_target):
    count = 0

    while (color_target[0] != None):
        count += 1
        print('\nCount: ', count)

        x_range = track.getAngle(color_target[0])  # find out the angle of the target
        radius = color_target[2]  # find out the radius of the target
        print("Target position: ", x_range, "\t radius", radius)
        chassisTargets = turnAndGo(x_range)  # take the x target location & generate turning
        pdTargets = inv.convert(chassisTargets)  # phi dot targets (rad/s) [for open loop?]
        print("pdTargets: ", pdTargets)
        sc.driveOpenLoop(pdTargets)
        print("Driving")
        time.sleep(0.05)
        color_target = track.colorTarget(follow.Blue)
