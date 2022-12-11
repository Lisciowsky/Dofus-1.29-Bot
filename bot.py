# Python Standard
import random
from typing import List, Union
from time import sleep, time
from datetime import datetime
from threading import Thread, Lock
from enum import Enum

# Third Party
import cv2 as cv
import pyautogui

# Local
from detection import Detection
from utils import (
    BotModes,
    BotState,
    PyutilMixns,
    GlobalDetector,
    CombatDetector,
    CharacterDetector,
    MoonIslandDetector,
)

# Every Run Global Actions / Indicators
from bot_actions.before_each_run import BeforeEachRun

# Specific Actions / Indicators
from bot_actions.farming import FarmingActions
from bot_actions.fighting import FightingActions
from bot_actions.moon_island import MoonIslandActions
from bot_actions.sadida_fight_sequence import DMGSadidaFightActions
from bot_actions.inventory_soul_equip import InventorySoulEquip
from bot_actions.changing_map import MapComeBackActions


class DofusBot:

    # constants
    INITIALIZING_SECONDS = 3
    FARMING_SECONDS = 16

    # threading properties
    stopped = True
    lock = None

    # properties
    state = None
    targets = None
    screenshot = None
    timestamp = None
    click_history = []

    def __init__(self, mode: BotModes):
        self.lock = Lock()
        self.state = BotState.INITIALIZING
        self.timestamp = time()
        self.mode = mode
        # we will populate the state of detectors in this dictionary to stop Combat detectors
        # from processing the image while in searching state, and vice versa.
        self.detectors_state = {}

    @staticmethod
    def move_and_click(x, y, double: bool = False):
        PyutilMixns.move(x, y, h_plus=0.0, w_plus=0.0, duration=0.3)
        sleep(random.randint(20, 50) / 100)
        PyutilMixns.click(x, y, h_plus=0.0, w_plus=0.0)
        if double:
            PyutilMixns.click(x, y, h_plus=0.0, w_plus=0.0)

    @staticmethod
    def _get_x_y_from_rectangle(rectangle):
        t_h = rectangle[0][2] / 2 / 2
        t_w = rectangle[0][3] / 2 / 2
        x = rectangle[0][0] + t_h
        y = rectangle[0][1] + t_w
        return x, y

    def handle_in_fight_tree_sequence(self) -> bool:
        if FightingActions.am_i_tree(self) or FightingActions.am_i_tree2(self):
            print("am i tree ?")
            if FightingActions.confirm_pause(self):
                print("Confirming I am tree")
                return True

        return False

    def handle_sadida_skill_sequence(self):
        yes = False
        sleep(random.randint(10, 150) / 100)

        self.lock.acquire()

        casted_spells = {
            "soul_capture_click": False,
            "earthquake_click": False,
            "poisoned_wind_click": False,
            "tree_skill": False,
        }

        if DMGSadidaFightActions.soul_capture_click(self):
            yes = DMGSadidaFightActions.tooltip(self)
            casted_spells["soul_capture_click"] = True
        if (
            DMGSadidaFightActions.earthquake_click(self)
            and casted_spells["soul_capture_click"]
        ):
            yes = DMGSadidaFightActions.tooltip(self)
            casted_spells["earthquake_click"] = True
        if (
            DMGSadidaFightActions.poisoned_wind_click(self)
            and casted_spells["soul_capture_click"]
            and casted_spells["earthquake_click"]
        ):
            yes = DMGSadidaFightActions.tooltip(self)
            casted_spells["poisoned_wind_click"] = True
        if (
            DMGSadidaFightActions.tree_skill(self)
            and casted_spells["soul_capture_click"]
            and casted_spells["earthquake_click"]
            and casted_spells["poisoned_wind_click"]
        ):
            yes = DMGSadidaFightActions.tooltip(self)
            casted_spells["tree_skill"] = True

        self.lock.release()

        if yes:
            FightingActions.confirm_pause(self)
            return True

    def _pause_or_active_detectors(
        self,
        pause: bool,
        detector_enumerator: Union[
            CharacterDetector, CombatDetector, MoonIslandDetector
        ],
    ):
        """
        We do not want to run search for monsters detectors while fighting and vice versa.
        This method is checking for detectors state, and pausing them off.
        :params detector_enumerator: enumerator based on filtered out detectors will be paused / activated.
        """
        detector_name = detector_enumerator.__name__

        if pause:
            if self.detectors_state.get(detector_name):
                print(f"Pausing {detector_name} detectors")
                {
                    detector_enum: detector.pause()
                    for detector_enum, detector in self.detectors.items()
                    if detector_enum in detector_enumerator
                }
                self.lock.acquire()
                self.detectors_state[detector_name] = False
                self.lock.release()

            return

        if not self.detectors_state.get(detector_name):
            print(f"Activating {detector_name} detectors")
            {
                detector_enum: detector.unpause()
                for detector_enum, detector in self.detectors.items()
                if detector_enum in detector_enumerator
            }
            self.lock.acquire()
            self.detectors_state[detector_name] = True
            self.lock.release()

    def open_inventory_equip_soul_sequence(self) -> bool:
        # Soul Equip
        print("trying to open inventory")
        if InventorySoulEquip.open_inventory(self):
            print("localized inventory, trying to equip the soul")
            sleep(3)
        if InventorySoulEquip.equip_soul(self):
            sleep(0.5)
            print("Soul equip successful")
            print("Closing inventory")
            if InventorySoulEquip.open_inventory(self):
                return True

    def proceed_fighting_sequence(self):
        if self.targets is None:
            print("waiting for targets, sleeping for 2")
            sleep(random.randint(20, 200) / 100)
            return True

        # We do make it to make sure we won't experience any pop-up windows from game.
        pyautogui.moveTo(x=1650, y=15)
        sleep(0.5)

        # Here we handle global pop up windows, that's why they run regardless of state.
        # make sure we are on the right map
        change_phoenix_map_success = MapComeBackActions.handle_phoenix_map(self)
        if change_phoenix_map_success:
            return
        change_woman_map_success = MapComeBackActions.handle_woman_map(self)
        if change_woman_map_success:
            return

        lvl_up_success = BeforeEachRun.lvl_up(self)
        if lvl_up_success:
            self.state = BotState.SEARCHING
            return True
        closing_fight_success = BeforeEachRun.closing_fight(self)
        if closing_fight_success:
            # equip the soul after finishing the fight.
            self.open_inventory_equip_soul_sequence()
            self.state = BotState.SEARCHING
            return True
        confirm_ready_success = FightingActions.confirm_ready(self)
        if confirm_ready_success:
            return True

        if FightingActions.am_i_in_fight(self):
            self.state = BotState.FIGHTING
        # Here we handle global pop up windows, that's why they run regardless of state.

        if self.state == BotState.FIGHTING:
            print("Fighting ...")
            # Activating combat detectors
            self._pause_or_active_detectors(
                pause=False, detector_enumerator=CharacterDetector
            )
            # Pausing mob search detectors
            self._pause_or_active_detectors(
                pause=True, detector_enumerator=MoonIslandDetector
            )

            if FightingActions.confirm_ready(self):
                return True
            if self.handle_in_fight_tree_sequence():
                FightingActions.confirm_pause(self)
                return True
            if self.handle_sadida_skill_sequence():
                return True

            return False

        if self.state == BotState.SEARCHING:
            print("Searching...")
            # Activating mob search detectors
            self._pause_or_active_detectors(
                pause=False, detector_enumerator=MoonIslandDetector
            )
            # Pausing combat detectors
            self._pause_or_active_detectors(
                pause=True, detector_enumerator=CharacterDetector
            )
            if MoonIslandActions.ambush_monster_click(self):
                if FightingActions.confirm_attack(self):
                    return True
            if MoonIslandActions.bamboo_left_monster_click(self):
                if FightingActions.confirm_attack(self):
                    return True
            if MoonIslandActions.bamboo_right_monster_click(self):
                if FightingActions.confirm_attack(self):
                    return True
            if MoonIslandActions.coconut_monster_click(self):
                if FightingActions.confirm_attack(self):
                    return True
            if MoonIslandActions.green_small_turtle_monster_click(self):
                if FightingActions.confirm_attack(self):
                    return True
            if MoonIslandActions.small_bamboo_right_monster_click(self):
                if FightingActions.confirm_attack(self):
                    return True
            if MoonIslandActions.bamboo_1_monster_click(self):
                if FightingActions.confirm_attack(self):
                    return True
            if MoonIslandActions.bamboo_2_monster_click(self):
                if FightingActions.confirm_attack(self):
                    return True
            if MoonIslandActions.turtle_click(self):
                if FightingActions.confirm_attack(self):
                    return True

            return False

        return False

    def update_targets(self, targets):
        self.lock.acquire()
        self.targets = targets
        self.lock.release()

    def update_detectors(self, detectors: dict):
        self.detectors = detectors

    def start(self):
        self.stopped = False
        t = Thread(target=self.run)
        t.start()

    def stop(self):
        self.stopped = True

    def run(self):
        print(f"Starting Bot instance at {datetime.now().isoformat()}")
        while not self.stopped:
            if self.targets is None:
                sleep(1.5)
                continue

            if self.state == BotState.INITIALIZING:
                if time() > self.timestamp + self.INITIALIZING_SECONDS:
                    print("Initialization Passed")

                    self.lock.acquire()
                    self.state = BotState.SEARCHING
                    self.lock.release()

            # FIGHTING FIGHTING FIGHTING FIGHTING
            if self.mode == BotModes.FIGHTING:
                success = self.proceed_fighting_sequence()

                if not success:
                    success = self.proceed_fighting_sequence()

                if success:
                    self.lock.acquire()
                    self.state = BotState.FIGHTING
                    self.lock.release()
                else:
                    self.lock.acquire()
                    self.state = BotState.SEARCHING
                    self.lock.release()
