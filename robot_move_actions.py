import robomaster
import time
import traceback

def robot_move(robot, X, Y, Z):
    ep_chassis = robot.chassis
    ep_chassis.drive_speed(x=X, y=Y, z=Z, timeout=5)

def robot_stop(robot, X, Y, Z):
    ep_chassis = robot.chassis
    ep_chassis.drive_speed(x=-X, y=-Y, z=-Z, timeout=5)
    time.sleep(0.1)
    ep_chassis.drive_speed(x=0, y=0, z=0, timeout=2)
    time.sleep(2)

def robot_distance_move(robot, x=0 , y=0 , z=0 , xy_speed=0.6 , z_speed=80):
    driving_action = robot.chassis.move(x,y,z,xy_speed,z_speed)
    driving_action.wait_for_completed()
    
def shift(robot,y,xy_speed=0.4):
    robot_distance_move(robot,0,0,(y//abs(y))*90)
    robot_distance_move(robot,x=y,y=0,z=0,xy_speed=xy_speed)
    robot_distance_move(robot,0,0,-(y//abs(y))*90)
