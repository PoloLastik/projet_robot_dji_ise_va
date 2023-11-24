import time
import robomaster
import robot_distance_actions
import robot_move_actions

def robot_move_until_threshold(ep_robot,X,Y,Z,threshold):
    while True:
        distance = robot_distance_actions.get_distance(ep_robot)
        robot_move_actions.robot_move(ep_robot,X=X, Y=Y,Z=Z)
        # print(f'Distance mesurée:{distance}')
        if distance <=threshold:
            robot_move_actions.robot_stop(ep_robot,X=X, Y=Y,Z=Z)            
            print('Stop')
            break
        time.sleep(0.1)
        
