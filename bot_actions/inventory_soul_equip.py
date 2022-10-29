# Python Standard
import time

# Local
from utils import BotModes, GlobalDetector


class InventorySoulEquip:
    @staticmethod
    def open_inventory(bot) -> bool:
        inventory_detector: Detection = bot.targets[BotModes.FIGHTING].get(
            GlobalDetector.INVENTORY
        )
        if len(inventory_detector.rectangles) > 0:
            rectangle = inventory_detector.rectangles[:1]
            print("Inventory: opening inventory")
            x, y = bot._get_x_y_from_rectangle(rectangle=rectangle)
            bot.move_and_click(x, y)
            return True

        return False

    @staticmethod
    def equip_soul(bot) -> bool:
        soul_detector: Detection = bot.targets[BotModes.FIGHTING].get(
            GlobalDetector.SOUL
        )
        if len(soul_detector.rectangles) > 0:
            rectangle = soul_detector.rectangles[:1]
            print("Inventory: equiping soul")
            print(rectangle)
            x, y = bot._get_x_y_from_rectangle(rectangle=rectangle)
            bot.move_and_click(x, y, double=True)

            return True

        return False
