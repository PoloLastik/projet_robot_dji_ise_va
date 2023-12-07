import cv2
from robomaster import robot
robots = []
area_min = 0.15
area_max = 0.17


class PersonInfo:

    def __init__(self, x, y, w, h):
        self._x = x
        self._y = y
        self._w = w
        self._h = h

    @property
    def pt1(self):
        return int((self._x - self._w / 2) * 1280), int((self._y - self._h / 2) * 720)

    @property
    def pt2(self):
        return int((self._x + self._w / 2) * 1280), int((self._y + self._h / 2) * 720)

    @property
    def center(self):
        return int(self._x * 1280), int(self._y * 720)
    
    @property
    def area(self):
        return self._w * self._h

def on_detect_person(person_info):
    global robots
    number = len(person_info)
    robots.clear()
    for i in range(0, number):
        x, y, w, h = person_info[i]
        # print(f'Personne détéctée à :{x},{y},{w},{h}')
        robots.append(PersonInfo(x, y, w, h))

def show_follow_result(ep_robot):

    ep_vision = ep_robot.vision
    ep_camera = ep_robot.camera

    ep_camera.start_video_stream(display=True)
    ep_vision.sub_detect_info(name="person", callback=on_detect_person)

    for i in range(0, 500):
        img = ep_camera.read_cv2_image(strategy="newest", timeout=0.5)
        for j in range(0, len(robots)):
            cv2.rectangle(img, robots[j].pt1, robots[j].pt2, (255, 255, 255))
        cv2.imshow("robots", img)
        cv2.waitKey(1)
    cv2.destroyAllWindows()
    ep_vision.unsub_detect_info(name="robot")
    cv2.destroyAllWindows()
    print(ep_vision.get_version())
    ep_camera.stop_video_stream()
    ep_robot.close()

def to_degrees(x_position):
    rotation = 0
    rotation = x_position*180 - 90 # Regarder le rapport, ici pour une range [-1;1]
    return rotation

def activate_follow_personn(ep_robot):
    ep_vision = ep_robot.vision
    ep_vision.sub_detect_info(name="person", callback=on_detect_person)

def deactivate_follow_personn(ep_robot):
    ep_vision = ep_robot.vision
    ep_vision.unsub_detect_info(name='personn')

def to_translation(X):
    returned_value = 0
    if area_max < X:
        returned_value = -0.3
    elif area_min > X:
        returned_value = 0.3
    else: 
        returned_value = 0
    return returned_value

def follow_personn(ep_robot):
    global robots
    X = 0
    personn = robots[0] if len(robots)>0 else PersonInfo(0.5,0,0.4,0.4)
    # print(f'Point détécté : {personn.pt1[0]}')
    rotation = to_degrees(personn._x)
    trans = to_translation(personn.area)
    print(f'Area:{personn.area}')
    return rotation, trans
