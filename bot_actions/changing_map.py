# Python Standard
import time

# Local
from utils import BotModes, MapDetector

# adding pixels to X = "->>>" & adding pixels to Y = "UP"
ADD_PIXELS = {
    "handle_phoenix_map": {"x": 35.0, "y": 10.0},
    "handle_woman_map": {"x": 25.0, "y": 10.0},
}


class MapComeBackActions:
    @staticmethod
    def handle_phoenix_map(bot) -> bool:
        map_detector: Detection = bot.targets[BotModes.FIGHTING].get(
            MapDetector.PHOENIX
        )
        map_back_detector: Detection = bot.targets[BotModes.FIGHTING].get(
            MapDetector.PHOENIX_COME_BACK
        )

        if len(map_detector.rectangles) > 0:
            print("I am on the wrong map ...")
            if len(map_back_detector.rectangles) > 0:
                rectangle = map_back_detector.rectangles[:1]
                x, y = bot._get_x_y_from_rectangle(rectangle=rectangle)
                bot.move_and_click(
                    x + ADD_PIXELS["handle_phoenix_map"]["x"],
                    y + ADD_PIXELS["handle_phoenix_map"]["y"],
                )
                return True

        return False

    @staticmethod
    def handle_woman_map(bot) -> bool:
        map_detector: Detection = bot.targets[BotModes.FIGHTING].get(MapDetector.WOMAN)
        map_back_detector: Detection = bot.targets[BotModes.FIGHTING].get(
            MapDetector.WOMAN_COME_BACK
        )

        if len(map_detector.rectangles) > 0:
            print("I am on the wrong map ...")
            if len(map_back_detector.rectangles) > 0:
                rectangle = map_back_detector.rectangles[:1]
                x, y = bot._get_x_y_from_rectangle(rectangle=rectangle)
                bot.move_and_click(
                    x + ADD_PIXELS["handle_woman_map"]["x"],
                    y + ADD_PIXELS["handle_woman_map"]["y"],
                )
                return True

        return False
