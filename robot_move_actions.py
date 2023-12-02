import robomaster
import time
import traceback

DEFAULT_ROBOT_SPEED_XY=0.4
MOVE_FACTOR_Y = 1
MOVE_FACTOR_X = 1
MOVE_FACTOR_UNTIL_ONE = [3, 3, 2, 1.5, 1, 1, 1, 1, 1, 1]
def robot_move(robot, X, Y, Z):
    ep_chassis = robot.chassis
    ep_chassis.drive_speed(x=X, y=Y, z=Z, timeout=5)

def robot_stop(robot, X, Y, Z):
    ep_chassis = robot.chassis
    ep_chassis.drive_speed(x=-X/10, y=-Y/10, z=-Z, timeout=5)
    time.sleep(0.1)
    ep_chassis.drive_speed(x=0, y=0, z=0, timeout=2)
    time.sleep(2)

def robot_distance_move(robot, x=0 , y=0 , z=0 , xy_speed=0.6 , z_speed=80):
    driving_action = robot.chassis.move(0,0,z,xy_speed,z_speed)
    driving_action.wait_for_completed()
    if x!=0 or y!=0:
        time_y = y/DEFAULT_ROBOT_SPEED_XY
        time_x = x/DEFAULT_ROBOT_SPEED_XY
        time_x, time_y = abs(time_x*MOVE_FACTOR_X), abs(time_y*MOVE_FACTOR_Y)
        print(f'Factorx = {int(time_x*10)} factor_y= {int(time_y*10)}')
        if time_x < 0.9:
            time_x = time_x*MOVE_FACTOR_UNTIL_ONE[int(time_x*10)]
        if time_y <0.9:
            time_y = time_y*MOVE_FACTOR_UNTIL_ONE[int(time_y*10)]
        print(f'time_x={time_x},time_y={time_y}')
        robot_move_while(robot,x,0,0,time_x)
        robot_move_while(robot,0,y,0,time_y)
    
def shift(robot,y,xy_speed=0.4):
    robot_distance_move(robot,0,0,(y//abs(y))*90)
    robot_distance_move(robot,x=y,y=0,z=0,xy_speed=xy_speed)
    robot_distance_move(robot,0,0,-(y//abs(y))*90)

def robot_move_while(robot, X,Y,Z,w_time):
    robot.chassis.drive_speed(x=X, y=-Y, z=-Z, timeout=5)
    time.sleep(w_time)
    robot_stop(robot,X,Y,Z)
    time.sleep(0.2)