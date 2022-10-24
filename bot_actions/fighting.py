from utils import CombatDetector, BotState, BotModes, CharacterDetector
from detection import Detection


class FightingActions:
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

    @staticmethod
    def confirm_pause(bot):
        confirm_pause_detector: Detection = bot.targets[BotModes.FIGHTING].get(
            CombatDetector.PAUSE
        )
        if len(confirm_pause_detector.rectangles) > 0:
            rectangle = confirm_pause_detector.rectangles[:1]
            print("FIGHT: confirm pause")
            x, y = bot._get_x_y_from_rectangle(rectangle=rectangle)
            bot.move_and_click(x, y)
            return True

        return False

    @staticmethod
    def am_i_tree(bot) -> bool:
        am_i_tree_detector: Detection = bot.targets[BotModes.FIGHTING].get(
            CharacterDetector.AM_I_TREE
        )
        if len(am_i_tree_detector.rectangles) > 0:
            print("FIGHT: I AM A TREE CONFIRMED")
            return True
        return False

    @staticmethod
    def am_i_tree2(bot) -> bool:
        am_i_tree_detector: Detection = bot.targets[BotModes.FIGHTING].get(
            CharacterDetector.AM_I_TREE2
        )
        if len(am_i_tree_detector.rectangles) > 0:
            print("FIGHT: I AM A TREE CONFIRMED")
            return True
        return False

    @staticmethod
    def am_i_in_fight(bot) -> bool:
        am_i_in_fight_detector: Detection = bot.targets[BotModes.FIGHTING].get(
            CombatDetector.AM_I_IN_FIGHT
        )
        if len(am_i_in_fight_detector.rectangles) > 0:
            rectangle = am_i_in_fight_detector.rectangles[:1]
            if len(rectangle) > 0:
                return True

        return False
