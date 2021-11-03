import L2_track_target as track
import time
import motors as mtrs


def Demo2():
    x_range = -5
    i = 5
    while 1:
        target = track.colorTarget(track.Green)  # generate a target
        print(target)
        x = target[0]
        if x is None:
            print("no target located.")
        else:
            x_range = track.getAngle(x)
            print("Target x location: ", x_range)
            time.sleep(0.1)  # short delay

        if x_range > -2:
            i = i - 1
            print("Hi")
            if i < 0:
                print("Test")
                mtrs.FlyWheel(.8)
                time.sleep(3)
                mtrs.Agitator(-.8)
                time.sleep(.5)
                mtrs.Agitator(0)
                time.sleep(0.5)
                print("OFF")
                mtrs.FlyWheel(0)
                time.sleep(10)


while True:
    Demo2()