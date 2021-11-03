# Import Internal Programs
import L2_Speed_Control as sc
import L2_Inverse_Kinematics as inv

# Import External programs
import numpy as np
import time


def square1m():
    myVelocities = np.array([0.4, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(2.5)  # input your duration (s)

    myVelocities = np.array([0, 3.14 / 2])  # input your 2nd pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(1.25)  # input your duration (s)

    myVelocities = np.array([0.4, 0])  # input your 3rd pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(2.5)  # input your duration (s)

    myVelocities = np.array([0, 3.14 / 2])  # input your 4th pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(1.25)  # input your duration (s)

    myVelocities = np.array([0.4, 0])  # input your 5th pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(2.5)  # input your duration (s)

    myVelocities = np.array([0, 3.14 / 2])  # input your 6th pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(1.25)  # input your duration (s)

    myVelocities = np.array([0.4, 0])
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(2.5)

def square0_5m():
    myVelocities = np.array([0.4, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(1.25)  # input your duration (s)

    myVelocities = np.array([0, 3.14 / 2])  # input your 2nd pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(1.25)  # input your duration (s)

    myVelocities = np.array([0.4, 0])  # input your 3rd pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(1.25)  # input your duration (s)

    myVelocities = np.array([0, 3.14 / 2])  # input your 4th pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(1.25)  # input your duration (s)

    myVelocities = np.array([0.4, 0])  # input your 5th pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(1.25)  # input your duration (s)

    myVelocities = np.array([0, 3.14 / 2])  # input your 6th pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(1.25)  # input your duration (s)

    myVelocities = np.array([0.4, 0])
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(1.25)


def triangle():
    myVelocities = np.array([0.4, 2*3.14/3])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(2.5)  # input your duration (s)

    myVelocities = np.array([0, 4*3.14 / 3])  # input your 2nd pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(1)  # input your duration (s)

    myVelocities = np.array([0.4, 0])  # input your 3rd pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(2.5)  # input your duration (s)

    myVelocities = np.array([0, 2*3.14 / 3])  # input your 4th pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(1.25)  # input your duration (s)

    myVelocities = np.array([0.4, 0])  # input your 5th pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(2.5)  # input your duration (s)

while 1:
    square1m()
    time.sleep(10)
    square0_5m()
    time.sleep(10)
    triangle()
