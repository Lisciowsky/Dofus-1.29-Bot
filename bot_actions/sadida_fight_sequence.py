from bot import DofusBot
from utils import BotModes, BotState, GlobalDetector
import pyautogui

class DMGSadidaFightActions:
    
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
