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


print('test')