from unittest import TestCase

import nativecap

class TestNativecap(TestCase):
    def test_simple_capture(self):
        nativecap.capture(0, 0, 640, 480)
