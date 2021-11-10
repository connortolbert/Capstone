# Level 3 program for driving SCUTTLE and handling other tasks in parallel

# IMPORT EXTERNAL ITEMS
import time
import numpy as np  # for handling matrices
import math

# IMPORT INTERNAL ITEMS
import L2_speed_control as sc  # closed loop control. Import speed_control for open-loop
import L2_inverse_kinematics as inv  # calculates wheel parameters from chassis
import L2_kinematics as kin  # calculates chassis parameters from wheels
# import L2_log as log  # log live data to local files
# import L2_obstacle as obs  # for detecting obstacles
# import L2_color_target as ct # for driving with computer vision tracking
import L1_encoder as enc  # for accessing encoders directly


# CREATE A THREAD FOR DRIVING
def loop_drive(duration, Velo=[]):
    # initialize variables for control system
    t0 = 0
    t1 = 1
    e00 = 0
    e0 = 0
    e1 = 0
    dt = 0
    de_dt = np.zeros(2)  # initialize the de_dt
    count = 0
    start = 0
    stop = 0
    while (count < duration):
        # start = time.time()
        count += 1
        print(count)
        # THIS CODE IS FOR OPEN AND CLOSED LOOP control
        myVelocities = Velo  # input your first pair
        # print(myVelocities)
        pdTargets = inv.convert(myVelocities)
        # print(pdTargets)
        pdCurrents = kin.getPdCurrent()  # assign the global variable value to a local var
        # THIS BLOCK UPDATES VARS FOR CONTROL SYSTEM
        t0 = t1  # assign t0
        t1 = time.time()  # generate current time
        dt = t1 - t0  # calculate dt
        e00 = e0  # assign previous previous error
        e0 = e1  # assign previous error
        e1 = pdCurrents - pdTargets  # calculate the latest error
        de_dt = (e1 - e0) / dt  # calculate derivative of error
        sc.driveClosedLoop(pdTargets, pdCurrents, de_dt)  # call the control system
        time.sleep(0.05)

    # stop = time.time()
    # dur = stop - start
    # print(dur)


if __name__ == "__main__":
    straight = np.array([0.4, 0])
    zero = np.array([0, 0])

    loop_drive(10, straight)
    loop_drive(10, zero)