# Imports

from robomaster import robot
import time
import robot_distance_actions
import robot_move_actions_unblocked
import robot_follow_personn
import robot_move_actions

# Constant

ROBOT_STRAIGHT_STANDARD_SPEED_X = 0.3

def wait_for_launch():
    while input('Ready ? ')!='yes':
        print('Ok, waiting...')
        pass
def instantiate_robot():
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")    
    ep_robot.set_robot_mode(mode=robot.CHASSIS_LEAD)
    print('Robot Initialized...')
    return ep_robot

def robot_find_wayout(ep_robot):
    """Trouve le coté correct pour se décaler dans l'évitement d'un obstacle.

    Args:
        ep_robot (ROBOT): Robot

    Returns:
        str: Indique droite ou gauche
    """
    wayout = ''
    print('Moving to right...')
    ep_robot.chassis.move(0,0,900)
    robot_distance_actions.start_distance_measurement(ep_robot)
    print('Measuring...')
    distance_right = robot_distance_actions.get_distance(ep_robot)
    print(distance_right)
    print('Moving to left...')
    ep_robot.chassis.move(0,0,-1800)
    print('Measuring...')
    distance_left = robot_distance_actions.get_distance(ep_robot)
    print(distance_left)
    ep_robot.chassis.move(0,0,900)
    if not (distance_right and distance_left and distance_right>0 and distance_left>0):
        wayout = 'error'
    elif distance_right>distance_left:
        wayout = 'right'
    elif distance_left>distance_right:
        wayout = 'left'
    else:wayout = 'None'
    return wayout

if __name__ == '__main__':
    
    ep_robot = instantiate_robot()
    wait_for_launch()
    robot_move_actions_unblocked.robot_move_until_threshold(ep_robot,ROBOT_STRAIGHT_STANDARD_SPEED_X,0,0,300)
    wyaout = robot_find_wayout(ep_robot)
    print('Wayout :' + wyaout)
    print('Done !')
    ep_robot.close()