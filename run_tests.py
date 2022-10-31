import unittest
from tests.test_utils import TestPyutilMixins

# utils
def utils_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestPyutilMixins(methodName="test_get_mac_adjusted_x_y"))
    suite.addTest(TestPyutilMixins(methodName="test_cursos_position_after_click"))
    suite.addTest(TestPyutilMixins(methodName="test_move"))
    suite.addTest(TestPyutilMixins(methodName="test_move_with_h_plus_and_w_plus"))
    # suite.addTest(TestPyutilMixins(methodName="test_move_time_with_duration"))

    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(utils_suite())
