from image_detector import ImageDetector
from vision import Vision
import pyautogui
import numpy as np
from time import sleep
import cv2
from mss import mss

bounding_box = {"top": 0, "left": 0, "width": 1680, "height": 1050}
sct = mss()

if __name__ == "__main__":
    sleep(2)
    detector = ImageDetector()

    sct_img = sct.grab(bounding_box)
    screenshot = np.array(sct_img)

    rectangles, weights = detector.detect_rectangles(
        file_path="./images/actions/lvl_up_confirm.png",
        screenshot=screenshot,
        threshold=0.9,
    )
    print(rectangles)
    screenshot, detected = Vision.draw_rectangles(
        rectangles=[x[:2] for x in rectangles],
        screenshot=screenshot,
        t_w=detector.t_w,
        t_h=detector.t_h,
    )
    print("detected", detected)
    cv2.imshow("Sample Screenshot", screenshot)
    key = cv2.waitKey(1)
    if key == ord("q"):
        cv2.destroyAllWindows()
