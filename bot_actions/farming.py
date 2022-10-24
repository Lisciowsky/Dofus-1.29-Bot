from bot import DofusBot
from utils import FarmerDetector, BotState, BotModes


class FarmingActions:

    bot: DofusBot

    @staticmethod
    def farming(bot) -> bool:
        wheat_detector: Detection = bot.targets[BotModes.FARMING].get(
            FarmerDetector.WHEAT
        )
        if len(wheat_detector.rectangles) > 0:
            rectangle = wheat_detector.rectangles[:1]
            print("FARMER: detected wheat")
            x, y = bot._get_x_y_from_rectangle(rectangle=rectangle)
            bot.move_and_click(x, y)
            print("FARMER: wheat ... sleaping for 2.5")
            sleep(2.5)
            return True

        return False

    @staticmethod
    def reaping(bot) -> bool:
        reap_detector: Detection = bot.targets[BotModes.FARMING].get(
            FarmerDetector.REAP
        )
        if len(reap_detector.rectangles) > 0:
            rectangle = reap_detector.rectangles[:1]
            print("FARMER: detected reap")
            x, y = bot._get_x_y_from_rectangle(rectangle=rectangle)
            bot.move_and_click(x, y)
            print("FARMER: reaping ... sleeping for 16")
            sleep(16)
            return True

        return False
