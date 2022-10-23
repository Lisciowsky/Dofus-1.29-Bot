from typing import List
import cv2 as cv
import pyautogui
from time import sleep, time
from datetime import datetime
from threading import Thread, Lock
from enum import Enum
from utils import (
    BotModes,
    BotState,
    FarmerDetector,
    PyutilMixns,
    GlobalDetector,
    CombatDetector,
)
from detection import Detection


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

    @staticmethod
    def move_and_click(x, y):
        PyutilMixns.move(x, y, h_plus=30.0, w_plus=50.0, duration=0.2)
        sleep(0.2)
        PyutilMixns.click(x, y, h_plus=30.0, w_plus=40.0)

    @staticmethod
    def _get_x_y_from_rectangle(rectangle):
        x = rectangle[0][0]
        y = rectangle[0][1]
        return x, y

    def must_check_for_every_mode(self, fn):
        """
        Decorator for must checks before each bot run.
        """
        lvl_up_success = self.lvl_up()
        if lvl_up_success:
            return True
        closing_fight_success = self.closing_fight()
        if closing_fight_success:
            return True

        def inner(*args, **kwargs):
            fn(*args, **kwargs)

        return inner

    """ FARMING """

    def farming(self) -> bool:
        wheat_detector: Detection = self.targets[BotModes.FARMING].get(
            FarmerDetector.WHEAT
        )
        if len(wheat_detector.rectangles) > 0:
            rectangle = wheat_detector.rectangles[:1]
            print("FARMER: detected wheat")
            x, y = self._get_x_y_from_rectangle(rectangle=rectangle)
            self.move_and_click(x, y)
            print("FARMER: wheat ... sleaping for 2.5")
            sleep(2.5)
            return True

        return False

    def reaping(self) -> bool:
        reap_detector: Detection = self.targets[BotModes.FARMING].get(
            FarmerDetector.REAP
        )
        if len(reap_detector.rectangles) > 0:
            rectangle = reap_detector.rectangles[:1]
            print("FARMER: detected reap")
            x, y = self._get_x_y_from_rectangle(rectangle=rectangle)
            self.move_and_click(x, y)
            print("FARMER: reaping ... sleeping for 16")
            sleep(16)
            return True

        return False

    """ FARMING """

    """ FIGHTING """

    def attack_monster(self):
        atack_monster_detector: Detection = self.targets[BotModes.FIGHTING].get(
            CombatDetector.PERFORM_ATTACK
        )
        if len(atack_monster_detector.rectangles) > 0:
            rectangle = atack_monster_detector.rectangles[:1]
            print("FIGHT: attack monster")
            x, y = self._get_x_y_from_rectangle(rectangle=rectangle)
            self.move_and_click(x, y)
            return True

        return False

    def confirm_attack(self):
        confirm_attack_detector: Detection = self.targets[BotModes.FIGHTING].get(
            CombatDetector.CONFIRM_ATTACK
        )
        if len(confirm_attack_detector.rectangles) > 0:
            rectangle = confirm_attack_detector.rectangles[:1]
            print("FIGHT: confirm attack")
            x, y = self._get_x_y_from_rectangle(rectangle=rectangle)
            self.move_and_click(x, y)
            return True

        return False

    def confirm_ready(self):
        confirm_ready_detector: Detection = self.targets[BotModes.FIGHTING].get(
            CombatDetector.CONFIRM_READY
        )
        if len(confirm_ready_detector.rectangles) > 0:
            rectangle = confirm_ready_detector.rectangles[:1]
            print("FIGHT: confirm ready")
            x, y = self._get_x_y_from_rectangle(rectangle=rectangle)
            self.move_and_click(x, y)
            return True

        return False

    """ FIGHTING """

    """ BEFORE EACH RUN """

    def closing_fight(self) -> bool:
        closing_fight_detector: Detection = self.targets[BotModes.FARMING].get(
            GlobalDetector.CLOSE_FIGHT
        )
        if len(closing_fight_detector.rectangles) > 0:
            rectangle = closing_fight_detector.rectangles[:1]
            print("FIGHT: detected closing fight")
            x, y = self._get_x_y_from_rectangle(rectangle=rectangle)
            self.move_and_click(x, y)
            return True

        return False

    def lvl_up(self) -> bool:
        lvl_up_detector: Detection = self.targets[BotModes.FARMING].get(
            GlobalDetector.LVL_UP
        )
        if len(lvl_up_detector.rectangles) > 0:
            rectangle = lvl_up_detector.rectangles[:1]
            print("FIGHT detected lvl up confirmation")
            x, y = self._get_x_y_from_rectangle(rectangle=rectangle)
            self.move_and_click(x, y)
            return True

        return False

    def am_i_in_fight(self) -> bool:
        am_i_in_fight_detector: Detection = self.targets[BotModes.FIGHTING].get(
            GlobalDetector.AM_I_IN_FIGHT
        )
        if len(am_i_in_fight_detector.rectangles) > 0:
            rectangle = am_i_in_fight_detector.rectangles[:1]
            if rectangle:
                self.state = BotState.FIGHTING
                return True

        return False

    """ BEFORE EACH RUN """

    @must_check_for_every_mode
    def is_farming(self):
        reaping_success = self.reaping()
        if reaping_success:
            return True
        farming_success = self.farming()
        if farming_success:
            return True

        return False

    @must_check_for_every_mode
    def is_fighting(self):
        # TOOD
        
        reaping_success = self.reaping()
        if reaping_success:
            return True
        farming_success = self.farming()
        if farming_success:
            return True

        return False

    # def click_next_target(self):
    #     """
    #     filtered_targets key:
    #      - BotModes.Farming
    #     filtered_targets value:
    #      - farming_detectors
    #     """

    #     """ MODES """
    #     if self.state == BotState.FARMING:
    #         return True if self.is_farming() else False

    #     if self.state == BotState.FIGHTING:
    #         return True if self.is_fighting() else False
    #     """ MODES """

    #     # attack_monster = self.attack_monster()
    #     # if attack_monster:
    #     #     return True
    #     # confirm_attack = self.confirm_attack()
    #     # if confirm_attack:
    #     #     return True
    #     # confirm_ready = self.confirm_ready()
    #     # if confirm_ready:
    #     #     return True

    #     return False

    def update_targets(self, targets):
        self.lock.acquire()
        self.targets = targets
        self.lock.release()

    def update_screenshot(self, screenshot):
        self.lock.acquire()
        self.screenshot = screenshot
        self.lock.release()

    def start(self):
        self.stopped = False
        t = Thread(target=self.run)
        t.start()

    def stop(self):
        self.stopped = True

    def run(self):
        print(f"Starting Bot instance at {datetime.now().isoformat()}")
        while not self.stopped:
            if self.state == BotState.INITIALIZING:
                if time() > self.timestamp + self.INITIALIZING_SECONDS:
                    print("Initialization Passed")

            # INDICATORS INDICATORS INDICATORS INDICATORS
            if self.am_i_in_fight():
                self.lock.acquire()
                self.state = BotState.FIGHTING
                self.lock.release()
            else:
                self.lock.acquire()
                self.state = BotState.SEARCHING
                self.lock.release()

            # FARMING FARMING FARMING FARMING
            if self.mode == BotModes.FARMING:
                success = self.is_farming()

                if not success:
                    success = self.is_farming()

                if success:
                    self.lock.acquire()
                    self.state = BotState.FARMING
                    self.lock.release()

            # FIGHTING FIGHTING FIGHTING FIGHTING
            elif self.mode == BotModes.FIGHTING:
                success = self.is_fighting()

                if not success:
                    success = self.is_fighting()

                if success:
                    self.lock.acquire()
                    self.state = BotState.FIGHTING
                    self.lock.release()
