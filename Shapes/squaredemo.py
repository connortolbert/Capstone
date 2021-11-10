# Import Internal Programs
import L2_speed_control as sc
import L2_inverse_kinematics as inv

# Import External programs
import numpy as np
import time


def square1m():
    print("Straight 1")
    myVelocities = np.array([0.2, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(5)  # input your duration (s)

    print("Stop")
    myVelocities = np.array([0, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(1)  # input your duration (s)

    print("Turn 1")
    myVelocities = np.array([0, 3.14 / 2])  # input your 2nd pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(.925)  # input your duration (s)

    print("Straight 2")
    myVelocities = np.array([0.2, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(5)  # input your duration (s)

    print("Stop")
    myVelocities = np.array([0, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(1)  # input your duration (s)

    print("Turn 2")
    myVelocities = np.array([0, 3.14 / 2])  # input your 2nd pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(.925)  # input your duration (s)

    print("Straight 3")
    myVelocities = np.array([0.2, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(5)  # input your duration (s)

    print("Stop")
    myVelocities = np.array([0, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(1)  # input your duration (s)

    print("Turn 3")
    myVelocities = np.array([0, 3.14 / 2])  # input your 2nd pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(.925)  # input your duration (s)

    print("Straight 4")
    myVelocities = np.array([0.2, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(5)  # input your duration (s)

    print("Stop")
    myVelocities = np.array([0, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(1)  # input your duration (s)


def square0_5m():


def triangle():
    myVelocities = np.array([0.4, 2 * 3.14 / 3])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(2.5)  # input your duration (s)

    myVelocities = np.array([0, 4 * 3.14 / 3])  # input your 2nd pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(1)  # input your duration (s)

    myVelocities = np.array([0.4, 0])  # input your 3rd pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(2.5)  # input your duration (s)

    myVelocities = np.array([0, 2 * 3.14 / 3])  # input your 4th pair
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
    # square0_5m()
    # time.sleep(10)
    # triangle()
