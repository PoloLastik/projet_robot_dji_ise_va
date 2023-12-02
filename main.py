# Imports

from robomaster import robot
import robomaster
import time
import robot_distance_actions
import robot_move_actions_unblocked
import robot_follow_personn
import robot_move_actions

# Constant

ROBOT_STRAIGHT_STANDARD_SPEED_X = 0.3
ROBOT_WEIGHT  = 0.3
def wait_for_launch():
    """Lance une boucle infinie pour lancer le programme
    """
    while input('Ready ? ')!='yes':
        print('Ok, waiting...')
        pass

def instantiate_robot():
    """
    Instancie le robot et le retourne.    
    """
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
    ep_chassis:robomaster.robot.chassis
    ep_chassis = ep_robot.chassis
    robot_move_actions.robot_distance_move(ep_robot,0,0,-90)
        
    print('Measuring...')
    distance_right = robot_distance_actions.get_distance(ep_robot)
    print(distance_right)
    print('Moving to left...')
    robot_move_actions.robot_distance_move(ep_robot,0,0,90)
    robot_move_actions.robot_distance_move(ep_robot,0,0,90)

    print('Measuring...')
    distance_left = robot_distance_actions.get_distance(ep_robot)
    print(distance_left)
    
    robot_move_actions.robot_distance_move(ep_robot,0,0,-90)

    # ep_chassis.move(0,0,90).wait_for_completed()
    if not (distance_right and distance_left and distance_right>0 and distance_left>0):
        wayout = 'error'
    elif distance_right>distance_left:
        wayout = 'right'
    elif distance_left>distance_right:
        wayout = 'left'
    else:wayout = 'None'
    return wayout

def move_until_threshold_with_obstacle_avoidance(ep_robot,position_threshold):
    """Réalise un parcours de 10m avec évitement des obstacles

    Args:
        ep_robot (Robot): Robot Concerné
    """
    print('Départ du parcours...')
    ep_chassis = robot.chassis
    robot_distance_actions.start_distance_measurement(ep_robot)
    robot_distance_actions.start_position_measurement(ep_robot)
    position = robot_distance_actions.get_position_data(robot)
    while(position<position_threshold):
        robot_move_actions.robot_move(ep_robot,X=ROBOT_STRAIGHT_STANDARD_SPEED_X, Y=0,Z=0)
        distance = robot_distance_actions.get_distance(ep_robot)
        if distance <=300:
            robot_move_actions.robot_stop(ep_robot,X=ROBOT_STRAIGHT_STANDARD_SPEED_X, Y=0,Z=0)
            wayout = robot_find_wayout(ep_robot=ep_robot)
            if wayout=='right':
                robot_move_actions.robot_distance_move(ep_robot,0,0.4,0)
            elif wayout=='left':            
                robot_move_actions.robot_distance_move(ep_robot,0,-0.4,0)
            else:
                print('No wayout found !')
                robot_move_actions.robot_move(ep_robot,0.5,0,0)
        position = robot_distance_actions.get_position_data(ep_robot)
  
            
def robot_move_until():
    try:
        ep_robot = robot.Robot()
        ep_robot.initialize(conn_type="ap")
        ep_robot.set_robot_mode(mode=robot.CHASSIS_LEAD)
        print('initialized')

        # Stocker la position initiale
        robot_distance_actions.start_position_measurement(ep_robot, freq=5)

        while True:
            # Effectuer le mouvement jusqu'à ce que la distance atteigne un seuil
            robot_move_actions.robot_move(ep_robot, X=0.3, Y=0, Z=0)

            # Attendre un court instant
            time.sleep(0.02)

            # Arrêter la mesure de distance

            

            # Calculer la distance parcourue
            distance_parcourue = robot_distance_actions.get_position_data(ep_robot) - robot_distance_actions.position_x_initial
            print(f"Distance parcourue : {distance_parcourue} mètres")

       
            
            if (distance_parcourue>1.5):
                print('stop main')
                robot_move_actions.robot_stop(ep_robot, X=0.3, Y=0, Z=0)
                robot_distance_actions.stop_position_measurement(ep_robot)
                break
                
            # robot_move_actions.robot_move(ep_robot,-0.3,0,0)
            # time.sleep(4)
            # robot_move_actions.robot_stop(ep_robot,-0.3,0,0)
            
            
    
    except Exception as e: 
        print(f"An error occurred: {e}")
    finally:
        # Fermer la connexion du robot
        ep_robot.close()




if __name__ == '__main__':
    
    ep_robot = instantiate_robot()
    wait_for_launch()
    print('Départ du parcours...')
    position_threshold = 2.5
    move_to_right = -0.3
    move_to_left = 0.3
    ep_chassis = robot.chassis
    robot_distance_actions.start_distance_measurement(ep_robot)
    robot_distance_actions.start_position_measurement(ep_robot)
    position = robot_distance_actions.get_position_data(robot)
    while(position<position_threshold):
        print("1- Moving on !")
        robot_move_actions.robot_move(ep_robot,X=ROBOT_STRAIGHT_STANDARD_SPEED_X, Y=0,Z=0)
        print('2- Measuring !')
        distance = robot_distance_actions.get_distance(ep_robot)
        print(f'3- Distance front :{distance}')
        if distance <=300:
            print('4- Distance front straight !')
            robot_move_actions.robot_stop(ep_robot,X=ROBOT_STRAIGHT_STANDARD_SPEED_X, Y=0,Z=0)
            wayout = robot_find_wayout(ep_robot=ep_robot)
            if wayout=='right':
                print('5- Moving to right !')
                robot_move_actions.robot_distance_move(ep_robot,0,move_to_right,0)
            elif wayout=='left':
                print('6- Moving to left !')
           
                robot_move_actions.robot_distance_move(ep_robot,0,move_to_left,0)
            else:
                print('No wayout found !')
                robot_move_actions.robot_move(ep_robot,0.5,0,0)
        position = robot_distance_actions.get_position_data(ep_robot)
        print(f'7- Position:{position}')
    print('Stop !')
    ep_robot.close()
