from bot import DofusBot
from utils import BotModes, BotState, GlobalDetector


class BeforeEachRun:

    bot: DofusBot

    @staticmethod
    def closing_fight(bot) -> bool:
        closing_fight_detector: Detection = bot.targets[BotModes.FARMING].get(
            GlobalDetector.CLOSE_FIGHT
        )
        if len(closing_fight_detector.rectangles) > 0:
            rectangle = closing_fight_detector.rectangles[:1]
            print("FIGHT: detected closing fight")
            x, y = bot._get_x_y_from_rectangle(rectangle=rectangle)
            bot.move_and_click(x, y)
            return True

        return False

    @staticmethod
    def lvl_up(bot) -> bool:
        lvl_up_detector: Detection = bot.targets[BotModes.FARMING].get(
            GlobalDetector.LVL_UP
        )
        if len(lvl_up_detector.rectangles) > 0:
            rectangle = lvl_up_detector.rectangles[:1]
            print("FIGHT detected lvl up confirmation")
            x, y = bot._get_x_y_from_rectangle(rectangle=rectangle)
            bot.move_and_click(x, y)
            return True

        return False

    @staticmethod
    def am_i_in_fight(bot) -> bool:
        am_i_in_fight_detector: Detection = bot.targets[BotModes.FIGHTING].get(
            GlobalDetector.AM_I_IN_FIGHT
        )
        if len(am_i_in_fight_detector.rectangles) > 0:
            rectangle = am_i_in_fight_detector.rectangles[:1]
            if rectangle:
                bot.state = BotState.FIGHTING
                return True

        return False
