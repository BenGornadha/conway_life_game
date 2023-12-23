from __future__ import annotations

import unittest

from cell import DeadCell, AliveCell
from dimension import Dimension
from grid import Grid
from position import Position
from square import Square


class TestGrid2(unittest.TestCase):
    def test_grid_with_two_cells_is_iterable(self):
        grid = Grid(dimensions=Dimension(1, 2))
        count_squares = 0
        for _ in grid:
            count_squares += 1

        self.assertEqual(2, count_squares)

    def test_Grid_is_iterable_and_yields_Square(self):
        grid = Grid(dimensions=Dimension(1, 1))
        an_iter = iter(grid)
        a_square = next(an_iter)

        self.assertEqual(Square(cell=DeadCell(position=Position(0, 0)), alive_neighbours=0), a_square)

    def test_grid_can_register_Alive_cell(self):
        grid = Grid(dimensions=Dimension(1, 1))
        grid.register_cell(cell=AliveCell(Position(0,0)))
        count_cell = 0
        for square in grid:
            count_cell += 1
            cell = square.cell
            self.assertTrue(cell.is_alive())
        self.assertEqual(1, count_cell)

