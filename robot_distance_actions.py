import time
import robomaster
from robomaster import robot
from robomaster import camera
from robomaster import sensor

cur_distance = 0

def store_distance(sub_info,selected_data_index=0):
    """Cette fonctions est utilisée pour instancier la variable cur_distance avec la distance mesurée dans sub_info.
    sub_info comporte 4 distance mesurées. Utilisée en callback de eps_sensor.sub_distance.

    Args:
        sub_info (List): Liste des distances mesurées
        selected_data_index (int, optional): Item selectionné dans sub_info. Defaults to 0.
    """
    global cur_distance
    cur_distance = sub_info[selected_data_index]

def get_distance(robot):
    """Retourne la distance mesurée par le robot.

    Args:
        robot (robomaster.robot): Robot concernée

    Returns:
        float: Distance mesurée.
    """
    global cur_distance
    ep_sensor = robot.sensor
    ep_sensor.sub_distance(freq=5, callback=store_distance)
    time.sleep(60)
    ep_sensor.unsub_distance()
    return cur_distance

# def sub_data_handler(sub_info):
#     distance = sub_info
#     print("Distance : {0}".format(distance[0]))

if __name__ == '__main__':
    
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")    
    ep_chassis=ep_robot.chassis
    ep_robot.set_robot_mode(mode=robot.CHASSIS_LEAD)

    #ep_chassis.drive_speed(x=2, y=0, z=0, timeout=5)
    #time.sleep(1)
    #ep_chassis.drive_speed(x=0, y=0, z=0, timeout=5)
    # result_action = ep_chassis.move(x=3, y=0, z=0, xy_speed=0.7)
    # result_action.wait_for_completed()
    #et_camera = ep_robot.camera

    #sous gros test wallah
    ep_sensor = ep_robot.sensor
    ep_sensor.sub_distance(freq=5, callback=sub_data_handler)
    time.sleep(60)
    ep_sensor.unsub_distance()
    ep_robot.close()

