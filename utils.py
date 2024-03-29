from typing import Tuple
from enum import Enum
import pyautogui


class MoonIslandDetector(Enum):
    AMBUSH = "AMBUSH"
    GREEN_SMALL_TURTLE = "GREEN_SMALL_TURTLE"
    BAMBOO_RIGHT = "BAMBOO_RIGHT"
    BAMBOO_LEFT = "BAMBOO_LEFT"
    BAMBOO_1 = "BAMBOO_1"
    BAMBOO_2 = "BAMBOO_2"
    TURTLE = "TURTLE"
    SMALL_BAMBOO_RIGHT = "SMALL_BAMBOO_RIGHT"
    COCONUT = "COCONUT"


class MapDetector(Enum):
    PHOENIX = "PHOENIX"
    WOMAN = "WOMAN"
    PHOENIX_COME_BACK = "PHOENIX_COME_BACK"
    WOMAN_COME_BACK = "WOMAN_COME_BACK"


class CharacterDetector(Enum):
    TOOLTIP = "TOOLTIP"
    AM_I_TREE = "AM_I_TREE"
    AM_I_TREE2 = "AM_I_TREE2"

    # Skills
    EARTHQUAKE = "EARTHQUAKE"
    POISONED_WIND = "POISONED_WIND"
    SOUL_CAPTURE = "SOUL_CAPTURE"
    TREE_SKILL = "TREE_SKILL"


class FarmerDetector(Enum):
    WHEAT = "WHEAT"
    REAP = "REAP"


class CombatDetector(Enum):
    PERFORM_ATTACK = "PERFORM_ATTACK"
    CONFIRM_ATTACK = "CONFIRM_ATTACK"
    CONFIRM_READY = "CONFIRM_READY"
    AM_I_IN_FIGHT = "AM_I_IN_FIGHT"
    PAUSE = "PAUSE"


class GlobalDetector(Enum):
    CLOSE_FIGHT = "CLOSE_FIGHT"
    LVL_UP = "LVL_UP"
    INVENTORY = "INVENTORY"
    SOUL = "SOUL"


class BotModes(Enum):
    FARMING = "FARMING"
    FIGHTING = "FIGHTING"


class Farming(Enum):
    pass


class BotState:
    INITIALIZING = 0
    SEARCHING = 1
    REAPING = 2
    FARMING = 3
    FIGHTING = 4


# UTILS FUNCTIONS


class PyutilMixns:
    @staticmethod
    def _get_mac_adjusted_x_y(x, y):
        x = x / 2
        y = y / 2
        return x, y

    @classmethod
    def click(cls, x, y, h_plus=0.0, w_plus=0.0):
        x, y = cls._get_mac_adjusted_x_y(x, y)
        pyautogui.click(x + w_plus, y + h_plus)

    @classmethod
    def move(cls, x, y, h_plus=0.0, w_plus=0.0, **kwargs):
        x, y = cls._get_mac_adjusted_x_y(x, y)
        pyautogui.moveTo(x + w_plus, y + h_plus, **kwargs)
