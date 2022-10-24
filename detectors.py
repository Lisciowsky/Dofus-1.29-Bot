import random
from detection import Detection
from image_detector import ImageDetector
from utils import (
    FarmerDetector,
    GlobalDetector,
    CombatDetector,
    IndicatorsDetector,
    MoonIslandDetector,
    CharacterDetector,
)

PLANTS = "./images/plants/"
ACTIONS = "./images/actions/"

# Farming
WHEAT = PLANTS + "wheat.png"
REAP = ACTIONS + "reap.png"

# Fight / Confirmations
CLOSE_FIGHT = ACTIONS + "close_fight.png"
LVL_UP = ACTIONS + "lvl_up_confirm.png"
AM_I_IN_FIGHT = "./images/indicators/in_fight_indicator.png"
ATTACK = "./images/actions/attack.png"
READY_FIGHT = "./images/actions/ready_fight.png"

# Monsters
AMBUSH = "./images/monsters/moon_island/ambush.png"
GREEN_SMALL_TURTLE = "./images/monsters/moon_island/green_small_turtle.png"
BAMBOO_RIGHT = "./images/monsters/moon_island/bamboo_right.png"
BAMBOO_LEFT = "./images/monsters/moon_island/bamboo_left.png"
SMALL_BAMBOO_RIGHT = "./images/monsters/moon_island/small_bambo_right.png"
SMALL_BAMBOO_LEFT = "./images/monsters/moon_island/small_bambo_left.png"
COCONUT = "./images/monsters/moon_island/coconut.png"

# Characters
SADI_TOOLTIP = "./images/character/sadi_tooltip.png"

# Character Skills
EARTHQUAKE = "./images/character/skills/earthquake.png"
POISONED_WIND = "./images/character/skills/poisoned_wind.png"
SOUL_CAPTURE = "./images/character/skills/soul_capture.png"
TREE_SKILL = "./images/character/skills/tree_skill.png"


THRESHOLDS = {
    "ACTIONS": {
        "ATTACK": 0.90,
        "REAP": 0.90,
        "CLOSE_FIGHT": 0.90,
        "LVL_UP": 0.90,
        "READY_FIGHT": 0.90,
    },
    "INDICATORS": {"AM_I_IN_FIGHT": 0.95},
    "PLANTS": {"WHEAT": 0.40},
    "MONSTERS": {"ALL": 0.50},
    "CHARACTER": {"ARTWORK": 0.90, "SKILLS": 0.90},
}


def _initialize_global_detectors():
    """
    GLOBAL DETECTORS, ATTACHED AS DEFAULT
    """
    return {
        GlobalDetector.CLOSE_FIGHT: GlobalDetectors.get_close_fight_detector(),
        GlobalDetector.LVL_UP: GlobalDetectors.get_lvl_up_detector(),
    }


# Initialize Detectors
def initialize_farming_detectors():
    """
    FARM DETECTORS
    """
    global_detectors = _initialize_global_detectors()
    return {
        FarmerDetector.WHEAT: FarmDetectors.get_wheat_detector(),
        FarmerDetector.REAP: FarmDetectors.get_reap_detector(),
    } | global_detectors


def initialize_fight_detectors():
    """
    COMBAT DETECTORS
    """
    global_detectors = _initialize_global_detectors()
    return {
        CombatDetector.CONFIRM_ATTACK: FightDetectors.confirm_attack(),
        CombatDetector.CONFIRM_READY: FightDetectors.confirm_ready(),
        CombatDetector.AM_I_IN_FIGHT: FightDetectors.am_i_in_fight_detector(),
    } | global_detectors


def initialize_moon_island_mobs_detectors():
    """
    MOON INSLAND MOBS DETECTORS
    """
    global_detectors = _initialize_global_detectors()
    return {
        # Mobs Detectors
        MoonIslandDetector.AMBUSH: MoonIslandMobsDetectors.ambush_detector(),
        MoonIslandDetector.GREEN_SMALL_TURTLE: MoonIslandMobsDetectors.green_small_turtle_detector(),
        MoonIslandDetector.BAMBOO_RIGHT: MoonIslandMobsDetectors.bamboo_right_detector(),
        MoonIslandDetector.BAMBOO_LEFT: MoonIslandMobsDetectors.bamboo_left_detector(),
        MoonIslandDetector.SMALL_BAMBOO_RIGHT: MoonIslandMobsDetectors.small_bamboo_right_detector(),
        MoonIslandDetector.SMALL_BAMBOO_LEFT: MoonIslandMobsDetectors.small_bamboo_left_detector(),
        MoonIslandDetector.COCONUT: MoonIslandMobsDetectors.coconut_detector(),
        # Characters Detectors
        CharacterDetector.TOOLTIP: CharacterDetectors.artwork_detector(),
        CharacterDetector.EARTHQUAKE: CharacterDetectors.earthquake_detector(),
        CharacterDetector.POISONED_WIND: CharacterDetectors.poisoned_wind_detector(),
        CharacterDetector.SOUL_CAPTURE: CharacterDetectors.soul_capture_detector(),
        CharacterDetector.TREE_SKILL: CharacterDetectors.tree_skill_detector(),
    }


class GlobalDetectors:
    @staticmethod
    def get_close_fight_detector():
        image_detector = ImageDetector()
        return Detection(
            image_detector=image_detector,
            lookup_path=CLOSE_FIGHT,
            threshold=THRESHOLDS["ACTIONS"]["CLOSE_FIGHT"],
        )

    @staticmethod
    def get_lvl_up_detector():
        image_detector = ImageDetector()
        return Detection(
            image_detector=image_detector,
            lookup_path=LVL_UP,
            threshold=THRESHOLDS["ACTIONS"]["LVL_UP"],
        )


class FarmDetectors:
    @staticmethod
    def get_wheat_detector():
        image_detector = ImageDetector()
        return Detection(
            image_detector=image_detector,
            lookup_path=WHEAT,
            threshold=THRESHOLDS["PLANTS"]["WHEAT"],
        )

    @staticmethod
    def get_reap_detector():
        image_detector = ImageDetector()
        return Detection(
            image_detector=image_detector,
            lookup_path=REAP,
            threshold=THRESHOLDS["ACTIONS"]["REAP"],
        )


class FightDetectors:
    @staticmethod
    def am_i_in_fight_detector():
        image_detector = ImageDetector()
        return Detection(
            image_detector=image_detector,
            lookup_path=AM_I_IN_FIGHT,
            threshold=THRESHOLDS["INDICATORS"]["AM_I_IN_FIGHT"],
        )

    @staticmethod
    def confirm_ready():
        image_detector = ImageDetector()
        return Detection(
            image_detector=image_detector,
            lookup_path=READY_FIGHT,
            threshold=THRESHOLDS["ACTIONS"]["READY_FIGHT"],
        )

    @staticmethod
    def confirm_attack():
        image_detector = ImageDetector()
        return Detection(
            image_detector=image_detector,
            lookup_path=ATTACK,
            threshold=THRESHOLDS["ACTIONS"]["ATTACK"],
        )


class MoonIslandMobsDetectors:
    @staticmethod
    def ambush_detector():
        image_detector = ImageDetector()
        return Detection(
            image_detector=image_detector,
            lookup_path=AMBUSH,
            threshold=THRESHOLDS["MONSTERS"]["ALL"],
        )

    @staticmethod
    def green_small_turtle_detector():
        image_detector = ImageDetector()
        return Detection(
            image_detector=image_detector,
            lookup_path=GREEN_SMALL_TURTLE,
            threshold=THRESHOLDS["MONSTERS"]["ALL"],
        )

    @staticmethod
    def bamboo_right_detector():
        image_detector = ImageDetector()
        return Detection(
            image_detector=image_detector,
            lookup_path=BAMBOO_RIGHT,
            threshold=THRESHOLDS["MONSTERS"]["ALL"],
        )

    @staticmethod
    def bamboo_left_detector():
        image_detector = ImageDetector()
        return Detection(
            image_detector=image_detector,
            lookup_path=BAMBOO_LEFT,
            threshold=THRESHOLDS["MONSTERS"]["ALL"],
        )

    @staticmethod
    def small_bamboo_left_detector():
        image_detector = ImageDetector()
        return Detection(
            image_detector=image_detector,
            lookup_path=SMALL_BAMBOO_LEFT,
            threshold=THRESHOLDS["MONSTERS"]["ALL"],
        )

    @staticmethod
    def small_bamboo_right_detector():
        image_detector = ImageDetector()
        return Detection(
            image_detector=image_detector,
            lookup_path=SMALL_BAMBOO_RIGHT,
            threshold=THRESHOLDS["MONSTERS"]["ALL"],
        )

    @staticmethod
    def coconut_detector():
        image_detector = ImageDetector()
        return Detection(
            image_detector=image_detector,
            lookup_path=COCONUT,
            threshold=THRESHOLDS["MONSTERS"]["ALL"],
        )


class CharacterDetectors:
    @staticmethod
    def artwork_detector():
        image_detector = ImageDetector()
        return Detection(
            image_detector=image_detector,
            lookup_path=SADI_TOOLTIP,
            threshold=THRESHOLDS["CHARACTER"]["ARTWORK"],
        )

    @staticmethod
    def earthquake_detector():
        image_detector = ImageDetector()
        return Detection(
            image_detector=image_detector,
            lookup_path=EARTHQUAKE,
            threshold=THRESHOLDS["CHARACTER"]["SKILLS"],
        )

    @staticmethod
    def poisoned_wind_detector():
        image_detector = ImageDetector()
        return Detection(
            image_detector=image_detector,
            lookup_path=POISONED_WIND,
            threshold=THRESHOLDS["CHARACTER"]["SKILLS"],
        )

    @staticmethod
    def soul_capture_detector():
        image_detector = ImageDetector()
        return Detection(
            image_detector=image_detector,
            lookup_path=SOUL_CAPTURE,
            threshold=THRESHOLDS["CHARACTER"]["SKILLS"],
        )

    @staticmethod
    def tree_skill_detector():
        image_detector = ImageDetector()
        return Detection(
            image_detector=image_detector,
            lookup_path=TREE_SKILL,
            threshold=THRESHOLDS["CHARACTER"]["SKILLS"],
        )
