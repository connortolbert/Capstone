import time
import L2_speed_control as sc
import L1_motor as motors
import L2_track_target as track
import L3_follow as follow
import PID
import L2_inverse_kinematics as inv

def shoot():
    print("Shoot")
    motors.FlyWheel(1)
    motors.Agitator(.5)
    time.sleep(.1)
    motors.Agitator(0)
    time.sleep(1)
    motors.FlyWheel(0)
    time.sleep(3)

def search():
    target = track.colorTarget(follow.Blue)
    print(target)
    stop = (0,0)
    if target[0] is None:                                   # if there is no colored target detected
        print("no target located.")                         # do not drive
        sc.driveOpenLoop(stop)                         # command motors in open-loop fashion
        
    else:
        x_range = track.getAngle(target[0])        # find out the angle of the target
        radius = target[2]                        # find out the radius of the target
        if radius > 100:
            sc.driveOpenLoop(stop)
            time.sleep(2)
            shoot()
        print("Target position: ", x_range, "\t radius", radius)
        chassisTargets = PID.con_turnAndGo(x_range)                 # take the x target location & generate turning
        pdTargets = inv.convert(chassisTargets)             # phi dot targets (rad/s) [for open loop?]
        print("pdTargets: ", pdTargets)
        sc.driveOpenLoop(pdTargets)
        
    
if __name__ == "__main__":
    while 1:
        search()