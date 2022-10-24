# Python Standard
from typing import List
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
    FarmerDetector,
    PyutilMixns,
    GlobalDetector,
    CombatDetector,
)

# Every Run Global Indicators
from bot_actions.before_each_run import BeforeEachRun

# Specific Indicators
from bot_actions.farming import FarmingActions
from bot_actions.fighting import FightingActions
from bot_actions.moon_island import MoonIslandActions
from bot_actions.sadida_fight_sequence import DMGSadidaFightActions


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
        lvl_up_success = BeforeEachRun.lvl_up(self)
        if lvl_up_success:
            return True
        closing_fight_success = BeforeEachRun.closing_fight(self)
        if closing_fight_success:
            return True

        def inner(*args, **kwargs):
            fn(*args, **kwargs)

        return inner

    @must_check_for_every_mode
    def is_farming(self):
        reaping_success = FarmingActions.reaping(self)
        if reaping_success:
            return True
        farming_success = FarmingActions.farming(self)
        if farming_success:
            return True

        return False

    @must_check_for_every_mode
    def is_fighting(self):
        # TOOD

        if self.state == BotState.FIGHTING:
            DMGSadidaFightActions

        else:
            if MoonIslandActions.ambush_monster_click(bot):
                # click attack
                return True
            if MoonIslandActions.ambush_monster_click(bot):
                return True
            
            return False

        return False

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
