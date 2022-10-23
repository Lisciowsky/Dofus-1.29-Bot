# detection.py
# Python Standard
from threading import Thread, Lock

# Third Party
import cv2 as cv

# Local
from image_detector import ImageDetector


class Detection:

    # threading properties
    stopped = True
    lock = None
    rectangles = []
    # properties
    screenshot = None
    t_w = None
    t_h = None

    def __init__(
        self, image_detector: ImageDetector, lookup_path: str, threshold: float
    ):
        # create a thread lock object
        self.lock = Lock()
        self.image_detector = image_detector
        self.lookup_path = lookup_path
        self.threshold = threshold

    def update(self, screenshot):
        self.lock.acquire()
        self.screenshot = screenshot
        self.lock.release()

    def start(self):
        self.stopped = False
        t = Thread(target=self.run)
        t.start()

    def stop(self):
        self.stopped = True

    def run(self):
        print(
            f"Running detector for: {self.lookup_path} with threashold: {self.threshold}"
        )
        while not self.stopped:
            if not self.screenshot is None and self.lookup_path:
                # do object detection
                rectangles, _ = self.image_detector.detect_rectangles(
                    self.screenshot,
                    file_path=self.lookup_path,
                    threshold=self.threshold,
                )
                # lock the thread while updating the results
                self.lock.acquire()
                self.rectangles = rectangles
                self.t_w = self.image_detector.t_w
                self.t_h = self.image_detector.t_h

                self.lock.release()
