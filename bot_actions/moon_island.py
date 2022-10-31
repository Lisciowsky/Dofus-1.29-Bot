# Python Standard
import random
from time import sleep

# Local
from utils import MoonIslandDetector, BotState, BotModes

# adding pixels to X = "->>>" & adding pixels to Y = "UP"
ADD_PIXELS = {
    "bamboo_left_monster_click": {"x": 25.0, "y": 0.0},
    "coconut_monster_click": {"x": 25.0, "y": 0.0},
    "big_bamboo_1_and_2": {"x": 35.0, "y": 10.0},
    "turtle": {"x": 10.0, "y": 0.0},
}


def random_sleep():
    """
    Sleep for random time between casting the spells.
    """
    sleep(random.randint(120, 200) / 100)


class MoonIslandActions:
    @staticmethod
    def ambush_monster_click(bot):
        monster_type = MoonIslandDetector.AMBUSH
        monster_detector: Detection = bot.targets[BotModes.FIGHTING].get(monster_type)
        if len(monster_detector.rectangles) > 0:
            rectangle = monster_detector.rectangles[:1]
            print(f"MOON MONSTERS: {monster_type.value} LOCALIZED")
            x, y = bot._get_x_y_from_rectangle(rectangle=rectangle)
            bot.move_and_click(x, y)
            random_sleep()
            return True

        return False

    @staticmethod
    def green_small_turtle_monster_click(bot):
        monster_type = MoonIslandDetector.GREEN_SMALL_TURTLE
        monster_detector: Detection = bot.targets[BotModes.FIGHTING].get(monster_type)
        if len(monster_detector.rectangles) > 0:
            rectangle = monster_detector.rectangles[:1]
            print(f"MOON MONSTERS: {monster_type.value} LOCALIZED")
            x, y = bot._get_x_y_from_rectangle(rectangle=rectangle)
            bot.move_and_click(x, y)
            random_sleep()
            return True

        return False

    @staticmethod
    def bamboo_right_monster_click(bot):
        monster_type = MoonIslandDetector.BAMBOO_RIGHT
        monster_detector: Detection = bot.targets[BotModes.FIGHTING].get(monster_type)
        if len(monster_detector.rectangles) > 0:
            rectangle = monster_detector.rectangles[:1]
            print(f"MOON MONSTERS: {monster_type.value} LOCALIZED")
            x, y = bot._get_x_y_from_rectangle(rectangle=rectangle)
            bot.move_and_click(x, y)
            random_sleep()
            return True

        return False

    @staticmethod
    def bamboo_left_monster_click(bot):
        monster_type = MoonIslandDetector.BAMBOO_LEFT
        monster_detector: Detection = bot.targets[BotModes.FIGHTING].get(monster_type)
        if len(monster_detector.rectangles) > 0:
            rectangle = monster_detector.rectangles[:1]
            print(f"MOON MONSTERS: {monster_type.value} LOCALIZED")
            x, y = bot._get_x_y_from_rectangle(rectangle=rectangle)
            bot.move_and_click(
                x + ADD_PIXELS["bamboo_left_monster_click"]["x"],
                y + +ADD_PIXELS["bamboo_left_monster_click"]["y"],
            )
            random_sleep()
            return True

        return False

    @staticmethod
    def small_bamboo_right_monster_click(bot):
        monster_type = MoonIslandDetector.SMALL_BAMBOO_RIGHT
        monster_detector: Detection = bot.targets[BotModes.FIGHTING].get(monster_type)
        if len(monster_detector.rectangles) > 0:
            rectangle = monster_detector.rectangles[:1]
            print(f"MOON MONSTERS: {monster_type.value} LOCALIZED")
            x, y = bot._get_x_y_from_rectangle(rectangle=rectangle)
            bot.move_and_click(x, y)
            random_sleep()
            return True

        return False

    @staticmethod
    def bamboo_1_monster_click(bot):
        monster_type = MoonIslandDetector.BAMBOO_1
        monster_detector: Detection = bot.targets[BotModes.FIGHTING].get(monster_type)
        if len(monster_detector.rectangles) > 0:
            rectangle = monster_detector.rectangles[:1]
            print(f"MOON MONSTERS: {monster_type.value} LOCALIZED")
            x, y = bot._get_x_y_from_rectangle(rectangle=rectangle)
            bot.move_and_click(
                x + ADD_PIXELS["big_bamboo_1_and_2"]["x"],
                y + ADD_PIXELS["big_bamboo_1_and_2"]["y"],
            )
            random_sleep()
            return True

        return False

    @staticmethod
    def bamboo_2_monster_click(bot):
        monster_type = MoonIslandDetector.BAMBOO_2
        monster_detector: Detection = bot.targets[BotModes.FIGHTING].get(monster_type)
        if len(monster_detector.rectangles) > 0:
            rectangle = monster_detector.rectangles[:1]
            print(f"MOON MONSTERS: {monster_type.value} LOCALIZED")
            x, y = bot._get_x_y_from_rectangle(rectangle=rectangle)
            bot.move_and_click(
                x + ADD_PIXELS["big_bamboo_1_and_2"]["x"],
                y + ADD_PIXELS["big_bamboo_1_and_2"]["y"],
            )
            random_sleep()
            return True

        return False

    @staticmethod
    def turtle_click(bot):
        monster_type = MoonIslandDetector.TURTLE
        monster_detector: Detection = bot.targets[BotModes.FIGHTING].get(monster_type)
        if len(monster_detector.rectangles) > 0:
            rectangle = monster_detector.rectangles[:1]
            print(f"MOON MONSTERS: {monster_type.value} LOCALIZED")
            x, y = bot._get_x_y_from_rectangle(rectangle=rectangle)
            bot.move_and_click(
                x + ADD_PIXELS["turtle"]["x"], y + ADD_PIXELS["turtle"]["y"]
            )
            random_sleep()
            return True

        return False

    @staticmethod
    def coconut_monster_click(bot):
        monster_type = MoonIslandDetector.COCONUT
        monster_detector: Detection = bot.targets[BotModes.FIGHTING].get(monster_type)
        if len(monster_detector.rectangles) > 0:
            rectangle = monster_detector.rectangles[:1]
            print(f"MOON MONSTERS: {monster_type.value} LOCALIZED")
            x, y = bot._get_x_y_from_rectangle(rectangle=rectangle)
            bot.move_and_click(
                x + ADD_PIXELS["coconut_monster_click"]["x"],
                y + ADD_PIXELS["coconut_monster_click"]["y"],
            )
            random_sleep()
            return True

        return False
