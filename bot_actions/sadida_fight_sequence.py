# Python Standard
import random
from time import sleep

# Local
from utils import BotModes, CharacterDetector

class DMGSadidaFightActions:
    @staticmethod
    def soul_capture_click(bot):
        skill_type = CharacterDetector.SOUL_CAPTURE
        skill_detector: Detection = bot.targets[BotModes.FIGHTING].get(skill_type)
        if len(skill_detector.rectangles) > 0:
            rectangle = skill_detector.rectangles[:1]
            print(f"SADIDA FIGHT: {skill_type.value} LOCALIZED")
            x, y = bot._get_x_y_from_rectangle(rectangle=rectangle)
            bot.move_and_click(x, y)

            return True

        return False

    @staticmethod
    def earthquake_click(bot):
        skill_type = CharacterDetector.EARTHQUAKE
        skill_detector: Detection = bot.targets[BotModes.FIGHTING].get(skill_type)
        if len(skill_detector.rectangles) > 0:
            rectangle = skill_detector.rectangles[:1]
            print(f"SADIDA FIGHT: {skill_type.value} LOCALIZED")
            x, y = bot._get_x_y_from_rectangle(rectangle=rectangle)
            bot.move_and_click(x, y)

            return True

        return False

    @staticmethod
    def poisoned_wind_click(bot):
        skill_type = CharacterDetector.POISONED_WIND
        skill_detector: Detection = bot.targets[BotModes.FIGHTING].get(skill_type)
        if len(skill_detector.rectangles) > 0:
            rectangle = skill_detector.rectangles[:1]
            print(f"SADIDA FIGHT: {skill_type.value} LOCALIZED")
            x, y = bot._get_x_y_from_rectangle(rectangle=rectangle)
            bot.move_and_click(x, y)

            return True

        return False

    @staticmethod
    def tree_skill(bot):
        skill_type = CharacterDetector.TREE_SKILL
        skill_detector: Detection = bot.targets[BotModes.FIGHTING].get(skill_type)
        if len(skill_detector.rectangles) > 0:
            rectangle = skill_detector.rectangles[:1]
            print(f"SADIDA FIGHT: {skill_type.value} LOCALIZED")
            x, y = bot._get_x_y_from_rectangle(rectangle=rectangle)
            bot.move_and_click(x, y)

            return True

        return False

    @staticmethod
    def tooltip(bot):
        action_type = CharacterDetector.TOOLTIP
        action_detector: Detection = bot.targets[BotModes.FIGHTING].get(action_type)
        if len(action_detector.rectangles) > 0:
            rectangle = action_detector.rectangles[:1]
            print(f"SADIDA FIGHT: {action_type.value} LOCALIZED")
            x, y = bot._get_x_y_from_rectangle(rectangle=rectangle)
            bot.move_and_click(x, y)
            sleep(random.randint(40, 150) / 100)
            return True

        return False
