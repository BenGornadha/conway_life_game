import unittest

from cell import AliveCell
from dimension import Dimension
from grid import Grid
from position import Position
from world import World


class MyTestCase(unittest.TestCase):

    def create_grid_XOO_XOX(self):
        grid = Grid(Dimension(2, 3))
        grid.register_cell(AliveCell(position=Position(0, 1)))
        grid.register_cell(AliveCell(position=Position(0, 2)))
        grid.register_cell(AliveCell(position=Position(1, 1)))
        return grid

    def create_grid_XOO_XOO(self):
        grid = Grid(Dimension(2, 3))
        grid.register_cell(AliveCell(position=Position(0, 1)))
        grid.register_cell(AliveCell(position=Position(0, 2)))
        grid.register_cell(AliveCell(position=Position(1, 1)))
        grid.register_cell(AliveCell(position=Position(1, 2)))
        return grid


    def test_something(self):
        w = World(grid=self.create_grid_XOO_XOX())
        sut = w.tick()

        expected_grid = self.create_grid_XOO_XOO()
        expected = World(grid=expected_grid)
        self.assertEqual(repr(expected), repr(sut))
