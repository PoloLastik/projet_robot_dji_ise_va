import robomaster
import time

def robot_move_for_period(robot:robomaster.Robot,X,Y,Z,time):
    """Bouge le robot vers les directions X,Y,Z pendant un temps time

    Args:
        robot (robomaster.Robot): Robot à etre déplacé
        X (float): Direction avant
        Y (float): Direction Droite-gauche
        Z (int): DeGres de rotation
        time (int): Temps de déplacement
    """
    ep_chassis=robot.chassis
    ep_chassis.drive_speed(x=X, y=Y, z=Z, timeout=5)
    time.sleep(time)
    ep_chassis.drive_speed(x=0, y=0, z=0, timeout=5)