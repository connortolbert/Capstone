import motors
import time

while(1):
        print("motors.py: driving fwd")
        motors.sendLeft(0.8)
        motors.sendRight(0.8)
        time.sleep(2)                       # run fwd for 4 seconds

        print("stopping motors 4 seconds")
        motors.sendLeft(0)
        motors.sendRight(0)
        time.sleep(2)

        print("turn on agitator and flywheel motors")
        motors.flywheel1(1)
        motors.flywheel2(1)
        motors.agitator1(.5)
        motors.agitator2(.5)
        time.sleep(.1)
        motors.agitator1(0)
        motors.agitator2(0)
        time.sleep(1)
        motors.flywheel1(0)
        motors.flywheel2(0)

        print("Spin")
        motors.sendLeft(-0.5)
        motors.sendRight(0.5)
        time.sleep(.5)                       # run reverse for 4 seconds

        print("stopping motors 4 seconds")
        motors.sendLeft(0)
        motors.sendRight(0)
        time.sleep(2)

        print("motors.py: driving fwd")
        motors.sendLeft(0.8)
        motors.sendRight(0.8)
        time.sleep(2)                       # run fwd for 4 seconds
