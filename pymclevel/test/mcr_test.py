import pymclevel.test.anvil_test
from pymclevel.test.templevel import TempLevel

__author__ = 'Rio'


class TestMCR(pymclevel.test.anvil_test.TestAnvilLevel):
    def setUp(self):
        self.indevLevel = TempLevel("hell.mclevel")
        self.anvilLevel = TempLevel("PyTestWorld")
