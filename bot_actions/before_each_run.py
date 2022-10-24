from utils import BotModes, BotState, GlobalDetector


class BeforeEachRun:
    @staticmethod
    def closing_fight(bot) -> bool:
        closing_fight_detector: Detection = bot.targets[BotModes.FIGHTING].get(
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
        lvl_up_detector: Detection = bot.targets[BotModes.FIGHTING].get(
            GlobalDetector.LVL_UP
        )
        if len(lvl_up_detector.rectangles) > 0:
            rectangle = lvl_up_detector.rectangles[:1]
            print("FIGHT detected lvl up confirmation")
            x, y = bot._get_x_y_from_rectangle(rectangle=rectangle)
            bot.move_and_click(x, y)
            return True

        return False
