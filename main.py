
import robomaster
from robomaster import robot
import robot_move_actions
import time
import robot_distance_actions
import robot_move_actions_unblocked
if __name__ == '__main__':
    
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")    
    ep_robot.set_robot_mode(mode=robot.CHASSIS_LEAD)
    print('initialized')
    ep_chassis=robot.chassis
    robot_distance_actions.start_distance_measurement(ep_robot,freq=20)
    robot_move_actions_unblocked.robot_move_until_threshold(ep_robot,X=0.3,Y=0,Z=0,threshold=300)
    
        time.sleep(0.02)
    robot_distance_actions.stop_distance_measurement(ep_robot)
    ep_robot.close()