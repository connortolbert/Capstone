import L2_Speed_Control as sc
import L2_Inverse_Kinematics as inv
import encoders as enc

while 1:
    myVelocities = np.array([0.4, 0])  # input your first pair
    myPhiDots = inv.convert(myVelocities)
    encValues = enc.readShaftPositions()
    print("Left: ", encValues[0], "\t", "Right: ", encValues[1])
    for i in range(4):
        while(encValues[0] != (enc.readShaftPositions()[0])):
            sc.driveOpenLoop(myPhiDots)