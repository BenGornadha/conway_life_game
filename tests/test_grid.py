import unittest

from cell import AliveCell
from dimension import Dimension
from grid import Grid
from position import Position


class MyTestCase(unittest.TestCase):
    def test_grid_is_iterable_and_is_by_default_full_of_dead_cells(self):
        grid = Grid(dimensions=Dimension(1, 1))
        count_cell = 0
        for _ in grid:
            count_cell += 1

        self.assertEqual(1, count_cell)

    def test_grid_can_register_Alive_cell(self):
        grid = Grid(dimensions=Dimension(1, 1))
        grid.register_cell(cell=AliveCell(Position(0,0)))
        count_cell = 0
        for cell in grid:
            count_cell += 1
            self.assertTrue(cell.is_alive())
        self.assertEqual(1, count_cell)
