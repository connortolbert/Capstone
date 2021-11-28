# speed_control.py takes target speeds and generates duty cycles
# to send to motors, and has a function to execute PID control.

# Import external libraries
import time

import numpy as np  # for handling arrays

# Import local files
import L1_motor as m  # for controlling motors
import L1_encoder as enc
import L2_inverse_kinematics as inv
import L2_kinematics as kin

# Initialize variables
u_integral = 0
# DRS = 0.8                                           # direct rescaling - for open-loop motor duty
kp = 0.04  # proportional term
ki = 0.04  # integral term
kd = 0.0  # derivative term
pidGains = np.array([kp, ki, kd])  # form an array to collect pid gains.


# a function for converting target rotational speeds to PWMs without feedback
def openLoop(pdl, pdr):
    DRS = 0.99  # create a variable for direct-re-scaling
    duties = np.array([pdl, pdr])  # put the values into an array
    duties = duties * 1 / 9.75 * DRS  # rescaling. 1=max PWM, 9.75 = max rad/s achievable
    duties[0] = sorted([-0.99, duties[0], 0.99])[1]  # place bounds on duty cycle
    duties[1] = sorted([-0.99, duties[1], 0.99])[1]  # place bounds on duty cycle
    return duties


def driveOpenLoop(pdTargets):  # Pass Phi dot targets to this function
    duties = openLoop(pdTargets[0], pdTargets[1])  # produce duty cycles from the phi dots
    print(duties)
    m.sendLeft(duties[0])  # send command to motors
    m.sendRight(duties[1])  # send command to motors


def scalingFunction(x):  # a fcn to compress the PWM region where motors don't turn
    if x < 100:
        x = x / 100
    else:
        x = x / 1000
    if -0.222 < x and x < 0.222:
        y = (x * 3)
    elif x > 0.222:
        y = ((x * 0.778) + 0.222)
    else:
        y = ((x * 0.778) - 0.222)
    return y


def con_scalingFunction(x):  # a fcn to compress the PWM region where motors don't turn

    if -22.2 < x and x < 22.2:
        y = (x * 3)
    elif x > 22.2:
        y = ((x * 0.778) + 0.222)
    else:
        y = ((x * 0.778) - 0.222)
    return y


def scaleMotorEffort(u):  # send the control effort signals to the scaling function
    u_out = np.zeros(2)
    print("Motor values before scaling:", u)
    u_out[0] = scalingFunction(u[0])
    u_out[1] = scalingFunction(u[1])
    print("Motor values after scaling:", u_out)
    return (u_out)


def driveClosedLoop(pdt, pdc, de_dt):  # this function runs motors for closed loop PID control
    global u_integral
    global u_proportional
    global u_derivative
    global u
    e = (pdt - pdc)  # compute error
    # print("\nError:", e)

    kp = pidGains[0]  # gains are input as constants, above
    ki = pidGains[1]
    kd = pidGains[2]

    # GENERATE COMPONENTS OF THE CONTROL EFFORT, u
    u_proportional = (e * kp)  # proportional term
    # print("\nProportional Gain:", u_proportional)

    try:
        u_integral += (e * ki)  # integral term
    except:
        u_integral = (e * ki)  # for first iteration, u_integral does not exist
    # print("\n Integral Gain:", u_integral)

    u_derivative = (de_dt * kd)  # derivative term takes de_dt as an argument
    # print("\nDerivative Gain:", u_derivative)

    # CONDITION THE SIGNAL BEFORE SENDING TO MOTORS
    u = np.round((u_proportional + u_integral + u_derivative), 2)  # must round to ensure driver handling
    u = scaleMotorEffort(u)  # MOVED to line 85                              # perform scaling - described above
    # u = u
    print("Before constraint", u)
    u[0] = sorted([-1, u[0], 1])[1]  # place bounds on the motor commands
    u[1] = sorted([-1, u[1], 1])[1]  # within [-1, 1]

    # w = u[0]
    # q = u[1]

    # if u[0] > .8:
    #     u[0] = w - .3

    # if u[1] > .8:
    #     u[1] = q - .3

    # print("After constraint", u)

    # SEND SIGNAL TO MOTORS
    # print("send motor signals")
    m.sendLeft(round(u[0], 2))  # must round to ensure driver handling!
    m.sendRight(round(u[1], 2))  # must round to ensure driver handling!f
    print("wheel speeds Left, Right", u[0], u[1])
    return
