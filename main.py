
import robomaster
from robomaster import robot
import robot_move_actions
import time
import robot_distance_actions
import robot_move_actions_unblocked
import robot_follow_personn
if __name__ == '__main__':
    
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")    
    ep_robot.set_robot_mode(mode=robot.CHASSIS_LEAD)
    print('initialized')
    print('Try to follow')
    print(robot_follow_personn.follow_personn())
    time.sleep(60)
    ep_robot.close()