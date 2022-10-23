import random
from detection import Detection
from image_detector import ImageDetector
from utils import FarmerDetector, GlobalDetector, CombatDetector, IndicatorsDetector

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

SMALL_GOBBY = "./images/monsters/black_gobby/"

THRESHOLDS = {
    "ACTIONS": {
        "ATTACK": 0.9,
        "REAP": 0.90,
        "CLOSE_FIGHT": 0.90,
        "LVL_UP": 0.90,
        "READY_FIGHT": 0.90,
    },
    "INDICATORS": {"AM_I_IN_FIGHT": 0.95},
    "PLANTS": {"WHEAT": 0.4},
    "MONSTERS": {"CLICK_ON_MONSTER": 0.5},
}


def _initialize_global_detectors():
    """
    GLOBAL DETECTORS, ATTACHED AS DEFAULT
    """
    return {
        GlobalDetector.CLOSE_FIGHT: get_close_fight_detector(),
        GlobalDetector.LVL_UP: get_lvl_up_detector(),
        GlobalDetector.AM_I_IN_FIGHT: am_i_in_fight_detector(),
    }


# Initialize Detectors
def initialize_farming_detectors():
    """
    FARM DETECTORS
    """
    global_detectors = _initialize_global_detectors()
    return {
        FarmerDetector.WHEAT: get_wheat_detector(),
        FarmerDetector.REAP: get_reap_detector(),
    } | global_detectors


def initialize_fight_detectors():
    """
    COMBAT DETECTORS
    """
    global_detectors = _initialize_global_detectors()
    return {
        CombatDetector.CONFIRM_ATTACK: get_wheat_detector(),
        CombatDetector.CONFIRM_READY: get_reap_detector(),
    } | global_detectors


def get_wheat_detector():
    image_detector = ImageDetector()
    return Detection(
        image_detector=image_detector,
        lookup_path=WHEAT,
        threshold=THRESHOLDS["PLANTS"]["WHEAT"],
    )


def get_reap_detector():
    image_detector = ImageDetector()
    return Detection(
        image_detector=image_detector,
        lookup_path=REAP,
        threshold=THRESHOLDS["ACTIONS"]["REAP"],
    )


def get_close_fight_detector():
    image_detector = ImageDetector()
    return Detection(
        image_detector=image_detector,
        lookup_path=CLOSE_FIGHT,
        threshold=THRESHOLDS["ACTIONS"]["CLOSE_FIGHT"],
    )


def get_lvl_up_detector():
    image_detector = ImageDetector()
    return Detection(
        image_detector=image_detector,
        lookup_path=LVL_UP,
        threshold=THRESHOLDS["ACTIONS"]["LVL_UP"],
    )


def attack_monster_detector():
    image_detector = ImageDetector()
    path = random.choice(os.listdir(SMALL_GOBBY))
    return Detection(
        image_detector=image_detector,
        lookup_path=path,
        threshold=THRESHOLDS["MONSTERS"]["CLICK_ON_MONSTER"],
    )


def confirm_attack():
    image_detector = ImageDetector()
    return Detection(
        image_detector=image_detector,
        lookup_path=ATTACK,
        threshold=THRESHOLDS["ACTIONS"]["ATTACK"],
    )


def confirm_ready():
    image_detector = ImageDetector()
    return Detection(
        image_detector=image_detector,
        lookup_path=READY_FIGHT,
        threshold=THRESHOLDS["ACTIONS"]["READY_FIGHT"],
    )


def am_i_in_fight_detector():
    image_detector = ImageDetector()
    return Detection(
        image_detector=image_detector,
        lookup_path=AM_I_IN_FIGHT,
        threshold=THRESHOLDS["INDICATORS"]["AM_I_IN_FIGHT"],
    )
