import unittest

from cell import DeadCell, AliveCell
from position import Position


class MyTestCase(unittest.TestCase):
    def test_equality_of_cell_are_on_class(self):
        self.assertEqual(DeadCell(position=Position(0, 0)), DeadCell(position=Position(1, 0)))

    def test_equality_of_cell_are_on_class2(self):
        self.assertEqual(AliveCell(position=Position(0, 0)), AliveCell(position=Position(1, 0)))
