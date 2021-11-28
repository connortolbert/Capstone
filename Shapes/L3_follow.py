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

# THIS SECTION ONLY RUNS IF THE PROGRAM IS CALLED DIRECTLY
if __name__ == "__main__":
    while True:
        target = track.colorTarget(Blue)  # generate a target from selected color
        if target[0] is None:  # if there is no colored target detected
            print("no target located.")  # do not drive
            stop = (0, 0)
            sc.driveOpenLoop(stop)  # command motors in open-loop fashion

        else:
            PID.openloop_drive(target)  # command motors in open-loop fashion
            # PID.loop_drive(target)                                    # PID Drive
            time.sleep(0.01)  # short delay