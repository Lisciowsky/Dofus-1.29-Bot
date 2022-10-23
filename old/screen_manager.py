from typing import Optional, Literal
import pyautogui


class ScreenManager:
    @staticmethod
    def _locate_item_on_screen(image_file: str):
        """
        Returns location (BOX) of detected image in the screen.
        :params image_file: image_filename of png that we are looking for.
        region argument (a 4-integer tuple of (left, top, width, height))
        """
        location_result = pyautogui.locateOnScreen(image_file)
        return location_result

    @staticmethod
    def _get_point_from_detected_image_location(detected_image_result):
        """
        Returns (POINT) of detected image in the screen.
        :params image_file: image_filename of png that we are looking for.
        """
        return pyautogui.center(detected_image_result)

    @classmethod
    def click(cls, image_file: str, region: Literal["Left", "Right", "Top", "Bottom"]):
        try:
            box = cls._locate_item_on_screen(image_file=image_file)
            point = cls._get_point_from_detected_image_location(
                detected_image_result=box
            )
            point_x, point_y = point
            point_x, point_y = point_x / 2, point_y / 2
            pyautogui.click(point_x, point_y)
        except Exception as ex:
            print(f"Unable to move to desired location...{ex}")
