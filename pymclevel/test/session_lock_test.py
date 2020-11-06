import unittest

from pymclevel.infiniteworld import SessionLockLost
from pymclevel.test.templevel import TempLevel


class SessionLockTest(unittest.TestCase):
    def test_session_lock(self):
        temp = TempLevel("AnvilWorld")
        level = temp.level

        def touch():
            level.saveInPlace()

        self.assertRaises(SessionLockLost, touch)
