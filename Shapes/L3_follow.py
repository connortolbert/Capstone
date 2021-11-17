# This is a demo for following a colored object.
# A basketball is an easy object to tune for colors and perform following
# Last updated 2021.06 DPM

# Import external programs
import time  # keeping time
import numpy as np  # for handling matrices

# Import internal programs
import L2_track_target as track
import L2_speed_control as sc
import L2_inverse_kinematics as inv
# import L2_Kinematics as kin
import PID

# import GediServer as GS


# Declare relevant variables
radius = 0  # radius of target
cruiseRate = 0.6  # speed for cruising (fraction)
r1 = 28  # radius desired (pixels)
tol = 3  # radius tolerance (pixels)

# PID Controller Variable Initialization
pdTargets = np.array([4, 4])  # desired PhiDots (speeds)

# Color Spaces
Red = ((0, 125, 155), (50, 180, 215))
Green = ((50, 70, 95), (75, 140, 140))
Blue = ((50, 130, 70), (125, 255, 225))


# if GS.full_msg == 5:
#    selected_color = Red

# if GS.full_msg == 6:
#    selected_color = Green

# if GS.full_msg == 7:
#    selected_color = Blue

def forwardFunction(r0):  # when the target is straight on, approach
    xdt = 0  # initial x_dot target is zero
    if r0 < (r1 - tol):  # if target looks too small
        xdt = cruiseRate  # x_dot target, drive fwd
    elif r0 > (r1 + tol):  # if target looks too big
        xdt = -1 * cruiseRate  # x_dot target, drive backwards
    return xdt


# THIS SECTION ONLY RUNS IF THE PROGRAM IS CALLED DIRECTLY
if __name__ == "__main__":
    while True:
        target = track.colorTarget(Blue)  # generate a target from selected color
        if target[0] is None:  # if there is no colored target detected
            print("no target located.")  # do not drive
            stop = (0, 0)
            sc.driveOpenLoop(stop)  # command motors in open-loop fashion

        else:
            # sc.driveOpenLoop(pdTargets)                         # command motors in open-loop fashion
            PID.loop_drive()  # PID Drive
            time.sleep(0.01)  # short delay