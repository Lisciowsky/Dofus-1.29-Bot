# Python Standard
from time import sleep

# Local
from detection import Detection
from image_detector import ImageDetector
from bot import DofusBot, BotModes

from detectors import initialize_farming_detectors, FarmerDetector

# Third Party
from mss import mss
import numpy as np
import cv2

sct = mss()
# Screen dimensions of your computer
bounding_box = {"top": 0, "left": 0, "width": 1680, "height": 1050}

# Initialize Detectors
farming_detectors = initialize_farming_detectors()
for detector in farming_detectors.values():
    detector.start()

# Bot instance
dofus_bot = DofusBot(mode=BotModes.FARMING)
dofus_bot.start()
# Sleep to change the windows to Dofus
sleep(2)


if __name__ == "__main__":
    while True:
        # get an updated image of the game
        sct_img = sct.grab(bounding_box)
        screenshot = np.array(sct_img)
        # updating the screenshot for detectors
        {
            detector_enum: detector.update(screenshot=screenshot)
            for detector_enum, detector in farming_detectors.items()
        }
        targets = {BotModes.FARMING: farming_detectors}

        dofus_bot.update_screenshot(screenshot=screenshot)
        dofus_bot.update_targets(targets=targets)

        key = cv2.waitKey(1)
        if key == ord("q"):
            detector.stop()
            cv.destroyAllWindows()
            # Stopping threads
            (detector.stop() for detector in farming_detectors.values())
            dofus_bot.stop()
            break