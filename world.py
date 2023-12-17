from __future__ import annotations
from typing import Any, List

from cell import Cell
from grid import Grid
from tests.test_rules import GameOfLifeRules


class World:

    def __init__(self, grid: Grid) -> None:
        self._grid = grid
        self._rules = GameOfLifeRules()

    def display(self) -> List[List[Cell]]:
        return self._grid.grid

    def tick(self) -> World:
        future_grid = Grid(dimensions=self._grid.dimensions)
        for square in self._grid:
            next_cell = self._rules.apply(square=square)
            future_grid.register_cell(next_cell)
        return World(grid=future_grid)

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, World) and self._grid == other._grid

    def __repr__(self) -> str:
        res = ""
        for cell in self._grid:
            if cell.is_alive():
                res += "O"
            else:
                res += "X"

        return res
