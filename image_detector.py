from typing import Tuple, List
from time import sleep

import cv2
import numpy as np
import pyautogui
import os


class ImageDetector:
    def __init__(self):
        pass

    def detect_rectangles(self, screenshot, file_path: str, threshold: float):
        """file_path: image to detect path.
        returns: list of locations
        """

        self.template = cv2.imread(f"./{file_path}")

        self.screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)
        self.template = cv2.cvtColor(self.template, cv2.COLOR_RGB2GRAY)

        self.t_h, self.t_w = self.template.shape
        method = cv2.TM_CCOEFF_NORMED
        result = cv2.matchTemplate(self.screenshot, self.template, method)
        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))

        rectangles = self.get_rectangles_from_locations(locations=locations)
        rectangles, weights = self.single_out_rectangles(rectangles=rectangles)

        return rectangles, weights

    def _visualize(self, detected_objects: list):
        line_color = (0, 255, 0)
        line_type = cv2.LINE_4
        copied_screenshot = self.screenshot.copy()

        for loc in detected_objects:
            # Determine the box positions
            top_left = loc
            bottom_right = (top_left[0] + self.t_w, top_left[1] + self.t_h)
            # Draw the box
            cv2.rectangle(
                copied_screenshot, top_left, bottom_right, line_color, line_type
            )

        cv2.imshow("Matches", copied_screenshot)
        cv2.waitKey()

    def get_rectangles_from_locations(
        self, locations: List[Tuple[int, int]]
    ) -> List[list]:
        rectangles = []
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), self.t_w, self.t_h]
            rectangles.append(rect)
            rectangles.append(rect)

        return rectangles

    @staticmethod
    def single_out_rectangles(rectangles: List) -> Tuple[list, list]:
        """
        The groupThreshold parameter will almost always be 1.
        If you set it to 0 it's not going to group any rectangles at all.
        And if you set it to something higher, it's going to require that more rectangles are overlapping each other before creating a grouped result for them.

        The eps parameter controls how close together the rectangles need to be before they will be grouped together.
        Lower values require that rectangles be closer together to be merged, while higher values will group together rectangles that are farther away.
        This is a good value to play around with to make sure you're getting the results you expect.
        """
        rectangles, weights = cv2.groupRectangles(rectangles, groupThreshold=1, eps=0.5)
        return rectangles, weights

    @staticmethod
    def _get_mac_adjusted_x_y(location: Tuple[int, int]):
        x = location[0] / 2
        y = location[1] / 2
        return x, y

    def _click(self, location: Tuple[int, int], h_plus=0.0, w_plus=0.0):
        x, y = self._get_mac_adjusted_x_y(location)
        pyautogui.click(x + w_plus, y + h_plus)

    def _move(self, location: Tuple[int, int], h_plus=0.0, w_plus=0.0, **kwargs):
        x, y = self._get_mac_adjusted_x_y(location)
        pyautogui.moveTo(x + w_plus, y + h_plus, **kwargs)


if __name__ == "__main__":
    detector = ImageDetector()
    wheat_locations = detector.locate_elem_on_image(
        file_path="images/plants/" + WHEAT_IMAGES[0], show_results=False, threshold=0.4
    )
    # detector._visualize(detected_objects=wheat_locations)
    wheat_rectangles = detector.get_rectangles_from_locations(locations=wheat_locations)
    wheat_rectangles, weights = detector.single_out_rectangles(
        rectangles=wheat_rectangles
    )
    # detector._visualize(detected_objects=[x[:2] for x in rectangles])

    for wheat_result in sorted(wheat_rectangles, key=lambda x: x[0]):
        detector._move(location=wheat_result, h_plus=40.0, w_plus=50.0, duration=0.1)
        detector._click(location=wheat_result, h_plus=40.0, w_plus=50.0)
        reap_locations = detector.locate_elem_on_image(
            file_path="images/actions/reap.png", threshold=0.95
        )
        reap_rectangles = detector.get_rectangles_from_locations(
            locations=reap_locations
        )
        reap_rectangles, weights = detector.single_out_rectangles(
            rectangles=reap_rectangles
        )
        if len(reap_rectangles) > 0:
            detector._move(location=reap_locations[0], duration=0.3, w_plus=10.0)
            sleep(0.3)
            detector._click(location=reap_locations[0], w_plus=20.0, h_plus=20.0)
            sleep(16)
        sleep(0.2)

    print(f"rectangles: {rectangles}")
    print(f"weights: {weights}")
