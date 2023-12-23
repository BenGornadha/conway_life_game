from __future__ import annotations

from alive_counter import NeighboursAliveCounter, CacheNeighboursPositions
from cell import Cell
from collections_rows_of_cells import CollectionRowOfCells
from dimension import Dimension
from square import Square


class Grid:
    CACHE_NEIGHBOURS = CacheNeighboursPositions()

    def __init__(self, dimensions: Dimension):
        self._dimensions = dimensions
        self._all_cells = CollectionRowOfCells(dimension=dimensions)
        self._neighbours_alive_counter = NeighboursAliveCounter(all_cells=self._all_cells)

    @property
    def all_cells(self) -> CollectionRowOfCells:
        return self._all_cells

    @property
    def dimensions(self) -> Dimension:
        return self._dimensions

    def register_cell(self, cell: Cell) -> None:
        if cell.is_alive():
            self._all_cells.register_alive_at(position=cell.position)

    def __eq__(self, other: Grid) -> bool:
        return isinstance(other, Grid) and self._all_cells == other._all_cells

    def __iter__(self) -> Square:
        for a_row in self._all_cells:
            for a_cell in a_row:
                yield Square(cell=a_cell, alive_neighbours=self._neighbours_alive_counter.for_a(cell=a_cell))
