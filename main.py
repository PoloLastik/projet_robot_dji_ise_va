from robomaster import robot
import time
import robot_distance_actions
import robot_move_actions_unblocked
import robot_move_actions
if __name__ == '__main__':
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