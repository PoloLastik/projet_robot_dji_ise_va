import time
import robomaster
from robomaster import robot
from robomaster import camera
from robomaster import sensor

def sub_data_handler(sub_info):
    distance = sub_info
    print("Distance : {0}".format(distance[0]))

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

