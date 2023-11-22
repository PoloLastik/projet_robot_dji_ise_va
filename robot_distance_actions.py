import time
import robomaster
from robomaster import robot
from robomaster import camera
from robomaster import sensor

cur_distance = 0
started = False

def store_distance(sub_info,selected_data_index=0):
    """Cette fonctions est utilisée pour instancier la variable cur_distance avec la distance mesurée dans sub_info.
    sub_info comporte 4 distance mesurées. Utilisée en callback de eps_sensor.sub_distance.

    Args:
        sub_info (List): Liste des distances mesurées
        selected_data_index (int, optional): Item selectionné dans sub_info. Defaults to 0.
    """
    global cur_distance
    cur_distance = sub_info[selected_data_index]

def stop_distance_measurement(robot):
    global started
    ep_sensor = robot.sensor
    ep_sensor.unsub_distance()
    started = False

def start_distance_measurement(robot,freq=5):
    global started
    ep_sensor = robot.sensor
    ep_sensor.sub_distance(freq=freq, callback=store_distance)
    time.sleep(1)
    started = True
    
def get_distance(robot):
    """Retourne la distance mesurée par le robot.

    Args:
        robot (robomaster.robot): Robot concernée

    Returns:
        float: Distance mesurée.
    """
    global cur_distance
    if started:
        return cur_distance
    else: 
        print('Activate the measurement !')
        return -1

# Variables pour stocker la position avant et après le mouvement
position_x = 0
success_start = None
position_started = False

def position_callback(position_info):
    x, y, z = position_info
    print(f"Position data - X: {x}, Y: {y}, Z: {z}")
    # Utiliser les variables globales pour stocker la position avant et après le mouvement
    global position_x
    position_x = x
    # print(f'position courante : {position_x}')
    # Imprimer les données de position
    

def stop_position_measurement(robot):
    global position_started
    chassis = robot.chassis
    try:
        chassis.unsub_position()
        position_started = False
    except Exception as e:
        print(f"Error stopping position measurement: {e}")

position_x_initial = 0  # Ajoutez cette variable globale

def start_position_measurement(robot, freq=5):
    global position_started, position_x_initial  # Ajoutez position_x_initial
    chassis = robot.chassis
    try:
        # S'abonner aux données de position avec une fréquence spécifiée
        success = chassis.sub_position(freq=freq, callback=position_callback)
        if success:
            print('yes')
            # Stocker la position initiale
            position_x_initial=0
            # Attendre un certain temps pour recevoir des données de position
            position_started = True
        else:
            print("Failed to subscribe to position data.")
    except Exception as e:
        print(f"Error during position subscription: {e}")

def get_position_data(robot):
    global position_x, position_started
    if position_started:
        return position_x
    else:
        print('Activate the position measurement!')