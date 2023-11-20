import cv2
from robomaster import robot
robots = []

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
    

def on_detect_person(person_info):
    number = len(person_info)
    robots.clear()
    for i in range(0, number):
        x, y, w, h = person_info[i]
        print(f'Personne détéctée à :{x},{y},{w},{h}')
        robots.append(PersonInfo(x, y, w, h))
        print("robot: x:{0}, y:{1}, w:{2}, h:{3}".format(x, y, w, h))

def show_follow_result(ep_robot):

    ep_vision = ep_robot.vision
    ep_camera = ep_robot.camera

    ep_camera.start_video_stream(display=False)
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
    rotation = x_position/10
    return rotation