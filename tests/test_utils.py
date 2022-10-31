# Python Standard
import unittest
from time import perf_counter

# Third Party
import pyautogui

# Local
from utils import PyutilMixns


class TestPyutilMixins(unittest.TestCase):
    def setUp(self):
        self.x = 200
        self.y = 200

        self.t_w = 25
        self.t_h = 40

        self.duration = 0.5

    def test_get_mac_adjusted_x_y(self):
        x, y = PyutilMixns._get_mac_adjusted_x_y(x=self.x, y=self.y)
        self.assertAlmostEqual(first=(self.x / 2, self.y / 2), second=(x, y))

    def test_cursos_position_after_click(self):
        PyutilMixns.click(x=self.x, y=self.y)
        x, y = pyautogui.position()
        mac_x, mac_y = PyutilMixns._get_mac_adjusted_x_y(x=self.x, y=self.y)
        self.assertEqual(first=mac_x, second=x)
        self.assertEqual(first=mac_y, second=y)

    def test_move(self):
        PyutilMixns.move(x=self.x, y=self.y)
        x, y = pyautogui.position()
        mac_x, mac_y = PyutilMixns._get_mac_adjusted_x_y(x=self.x, y=self.y)
        self.assertEqual(first=mac_x, second=x)
        self.assertEqual(first=mac_y, second=y)

    def test_move_with_h_plus_and_w_plus(self):
        PyutilMixns.move(x=self.x, y=self.y, h_plus=self.t_h, w_plus=self.t_w)
        x, y = pyautogui.position()
        mac_x, mac_y = PyutilMixns._get_mac_adjusted_x_y(x=self.x, y=self.y)
        self.assertEqual(first=mac_x + self.t_w, second=x)
        self.assertEqual(first=mac_y + self.t_h, second=y)

    # def test_move_time_with_duration(self):
    #     start = perf_counter()
    #     PyutilMixns.move(x=self.x, y=self.y, duration=self.duration)
    #     stop = perf_counter()
    #     elapsed = stop - start
    #     self.assertAlmostEqual(first=elapsed, second=self.duration)
