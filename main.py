import robomaster
import time
import robot_distance_actions
import robot_move_actions

if __name__ == '__main__':
    
    ep_robot = robomaster.Robot()
    ep_robot.initialize(conn_type="ap")    
    ep_robot.set_robot_mode(mode=robot.CHASSIS_LEAD)
    robot_move_actions.robot_move_for_period(ep_robot,1,0,0,1)
    distance = robot_distance_actions.get_distance(ep_robot)
    print(f'Distance mesurée:{distance}')
    ep_robot.close()