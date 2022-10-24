from bot import DofusBot
from utils import CombatDetector, BotState, BotModes


class FightingActions:

    bot: DofusBot

    @staticmethod
    def attack_monster(bot):
        atack_monster_detector: Detection = bot.targets[BotModes.FIGHTING].get(
            CombatDetector.PERFORM_ATTACK
        )
        if len(atack_monster_detector.rectangles) > 0:
            rectangle = atack_monster_detector.rectangles[:1]
            print("FIGHT: attack monster")
            x, y = bot._get_x_y_from_rectangle(rectangle=rectangle)
            bot.move_and_click(x, y)
            return True

        return False

    @staticmethod
    def confirm_attack(bot):
        confirm_attack_detector: Detection = bot.targets[BotModes.FIGHTING].get(
            CombatDetector.CONFIRM_ATTACK
        )
        if len(confirm_attack_detector.rectangles) > 0:
            rectangle = confirm_attack_detector.rectangles[:1]
            print("FIGHT: confirm attack")
            x, y = bot._get_x_y_from_rectangle(rectangle=rectangle)
            bot.move_and_click(x, y)
            return True

        return False

    @staticmethod
    def confirm_ready(bot):
        confirm_ready_detector: Detection = bot.targets[BotModes.FIGHTING].get(
            CombatDetector.CONFIRM_READY
        )
        if len(confirm_ready_detector.rectangles) > 0:
            rectangle = confirm_ready_detector.rectangles[:1]
            print("FIGHT: confirm ready")
            x, y = bot._get_x_y_from_rectangle(rectangle=rectangle)
            bot.move_and_click(x, y)
            return True

        return False
