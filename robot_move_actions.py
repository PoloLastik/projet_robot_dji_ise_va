import robomaster
import time

    
def robot_move(robot,X,Y,Z):
    print(f"Moving on {X} {Y} {Z} ")
    ep_chassis = robot.chassis
    ep_chassis.drive_speed(x=X, y=Y, z=Z, timeout=5)

def robot_stop(robot,X,Y,Z):
    ep_chassis = robot.chassis
    ep_chassis.drive_speed(x=-X, y=-Y, z=-Z, timeout=5)
    time.sleep(0.1)
    ep_chassis.drive_speed(x=0, y=0, z=0, timeout=5)

