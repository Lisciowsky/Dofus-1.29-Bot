from bot import DofusBot
from utils import MoonIslandDetector, BotState, BotModes


class MoonIslandActions:

    bot: DofusBot

    @staticmethod
    def ambush_monster_click(bot):
        monster_type = MoonIslandDetector.AMBUSH
        monster_detector: Detection = bot.targets[BotModes.FIGHTING].get(monster_type)
        if len(monster_detector.rectangles) > 0:
            rectangle = monster_detector.rectangles[:1]
            print(f"MOON MONSTERS: {monster_type.value} LOCALIZED")
            x, y = bot._get_x_y_from_rectangle(rectangle=rectangle)
            bot.move_and_click(x, y)
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
            bot.move_and_click(x, y)
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
            return True

        return False

    @staticmethod
    def small_bamboo_left_monster_click(bot):
        monster_type = MoonIslandDetector.SMALL_BAMBOO_LEFT
        monster_detector: Detection = bot.targets[BotModes.FIGHTING].get(monster_type)
        if len(monster_detector.rectangles) > 0:
            rectangle = monster_detector.rectangles[:1]
            print(f"MOON MONSTERS: {monster_type.value} LOCALIZED")
            x, y = bot._get_x_y_from_rectangle(rectangle=rectangle)
            bot.move_and_click(x, y)
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
            bot.move_and_click(x, y)
            return True

        return False
