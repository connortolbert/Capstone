# Import Internal Programs
import L2_speed_control as sc
import L2_inverse_kinematics as inv

# Import External programs
import numpy as np
import time


def square(s):
    print("Straight 1")
    myVelocities = np.array([0.2, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(s * 5)  # input your duration (s)

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
    time.sleep(s * 5)  # input your duration (s)

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
    time.sleep(s * 5)  # input your duration (s)

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
    time.sleep(s * 5)  # input your duration (s)

    print("Stop")
    myVelocities = np.array([0, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(1)  # input your duration (s)

    print("Turn 4")
    myVelocities = np.array([0, 3.14 / 2])  # input your 2nd pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(.925)  # input your duration (s)

    print("Stop")
    myVelocities = np.array([0, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(1)  # input your duration (s)


def triangle(s):
    print("Straight 1")
    myVelocities = np.array([0.2, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(s * 5)  # input your duration (s)

    print("Stop")
    myVelocities = np.array([0, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(1)  # input your duration (s)

    print("Turn 1")
    myVelocities = np.array([0, 3.14 / 2])  # input your 2nd pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep((4 / 3) * .925)  # input your duration (s)

    print("Straight 2")
    myVelocities = np.array([0.2, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(s * 5)  # input your duration (s)

    print("Stop")
    myVelocities = np.array([0, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(1)  # input your duration (s)

    print("Turn 2")
    myVelocities = np.array([0, 3.14 / 2])  # input your 2nd pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep((4 / 3) * .925)  # input your duration (s)

    print("Straight 3")
    myVelocities = np.array([0.2, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(s * 5)  # input your duration (s)

    print("Stop")
    myVelocities = np.array([0, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(1)  # input your duration (s)

    print("Turn 3")
    myVelocities = np.array([0, 3.14 / 2])  # input your 2nd pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep((4 / 3) * .925)  # input your duration (s)

    print("Stop")
    myVelocities = np.array([0, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(1)  # input your duration (s)


def hexagon(s):
    print("Straight 1")
    myVelocities = np.array([0.2, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(s * 5)  # input your duration (s)

    print("Stop")
    myVelocities = np.array([0, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(1)  # input your duration (s)

    print("Turn 1")
    myVelocities = np.array([0, 3.14 / 2])  # input your 2nd pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep((2 / 3) * .925)  # input your duration (s)

    print("Straight 2")
    myVelocities = np.array([0.2, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(s * 5)  # input your duration (s)

    print("Stop")
    myVelocities = np.array([0, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(1)  # input your duration (s)

    print("Turn 2")
    myVelocities = np.array([0, 3.14 / 2])  # input your 2nd pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep((2 / 3) * .925)  # input your duration (s)

    print("Straight 3")
    myVelocities = np.array([0.2, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(s * 5)  # input your duration (s)

    print("Stop")
    myVelocities = np.array([0, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(1)  # input your duration (s)

    print("Turn 3")
    myVelocities = np.array([0, 3.14 / 2])  # input your 2nd pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep((2 / 3) * .925)  # input your duration (s)

    print("Straight 4")
    myVelocities = np.array([0.2, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(s * 5)  # input your duration (s)

    print("Stop")
    myVelocities = np.array([0, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(1)  # input your duration (s)

    print("Turn 4")
    myVelocities = np.array([0, 3.14 / 2])  # input your 2nd pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep((2 / 3) * .925)  # input your duration (s)

    print("Straight 5")
    myVelocities = np.array([0.2, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(s * 5)  # input your duration (s)

    print("Stop")
    myVelocities = np.array([0, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(1)  # input your duration (s)

    print("Turn 5")
    myVelocities = np.array([0, 3.14 / 2])  # input your 2nd pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep((2 / 3) * .925)  # input your duration (s)

    print("Straight 6")
    myVelocities = np.array([0.2, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(s * 5)  # input your duration (s)

    print("Stop")
    myVelocities = np.array([0, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(1)  # input your duration (s)

    print("Turn 6")
    myVelocities = np.array([0, 3.14 / 2])  # input your 2nd pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep((2 / 3) * .925)  # input your duration (s)

    print("Stop")
    myVelocities = np.array([0, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(1)  # input your duration (s)


def circle(s):
    # print("Hopefully I'm not a dumbass")
    # myVelocities = np.array([0.2, 2*np.pi])  # input your first pair
    # myPhiDots = inv.convert(myVelocities)
    # print(myPhiDots)
    # sc.driveOpenLoop(myPhiDots)
    # time.sleep(s * 5)  # input your duration (s)
    # print("you are a dumbass")
    # print("Attempt 2")
    if s == 1:
        for i in range(21):
            myVelocities = np.array([0.2, ((np.pi) / 12)])  # input your 2nd pair
            myPhiDots = inv.convert(myVelocities)
            # print(myPhiDots)
            backup = [3.595, 6.162]
            sc.driveOpenLoop(myPhiDots)
            time.sleep(s * 1)  # input your duration (s)
            print(i)

    elif s == 0.5:  # works
        for i in range(21):
            myVelocities = np.array([0.2, np.pi / 6])  # input your 2nd pair
            myPhiDots = inv.convert(myVelocities)
            # print(myPhiDots)
            backup = [2.311, 7.445]
            sc.driveOpenLoop(myPhiDots)
            time.sleep(s * 1)  # input your duration (s)
            print(i)

    else:
        print("Error")

    print("Stop")
    myVelocities = np.array([0, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    sc.driveOpenLoop(myPhiDots)
    time.sleep(3)  # input your duration (s)


if __name__ == "__main__":
    s = 1
    square(s)
    time.sleep(3)
    triangle(s)
    time.sleep(3)
    hexagon(s)
    time.sleep(3)
    circle(s)
    time.sleep(3)
    s = 0.5
    square(s)
    time.sleep(3)
    triangle(s)
    time.sleep(3)
    hexagon(s)
    time.sleep(3)
    circle(s)
    time.sleep(3)
