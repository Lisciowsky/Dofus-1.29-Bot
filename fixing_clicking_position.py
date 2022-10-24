import pyautogui
import numpy as np
from time import sleep
from mss import mss

from image_detector import ImageDetector

bounding_box = {"top": 0, "left": 0, "width": 1680, "height": 1050}
sct = mss()

if __name__ == "__main__":
    sleep(2)
    # detector = ImageDetector()

    # sct_img = sct.grab(bounding_box)
    # screenshot = np.array(sct_img)

    # rectangles, weights = detector.detect_rectangles(
    #     file_path="./images/character/sadi_on_fight_bar.png",
    #     screenshot=screenshot,
    #     threshold=0.9,
    # )
    # print(rectangles)
    # # input()
    # t_h = rectangles[0][2] / 2 / 2
    # t_w = rectangles[0][3] / 2 / 2

    # pyautogui.moveTo(rectangles[0][0] / 2 + t_h, rectangles[0][1] / 2 + t_w)
    pyautogui.moveTo(x=610, y=580)
