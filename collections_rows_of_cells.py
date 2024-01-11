from __future__ import annotations

from typing import List

from cell import Cell, DeadCell, AliveCell
from dimension import Dimension
from position import Position


class CollectionRowOfCells:
    def __init__(self, dimension: Dimension) -> None:
        self._rows = [RowOfCells(index=index_row, number_of_cells=dimension.number_of_columns) for index_row in
                      range(dimension.number_of_row)]

    def __iter__(self):
        return iter(self._rows)

    def register_alive_at(self, position):
        row = self._row_of_cells_at(position)
        row.register_alive_at(position=position)

    def _row_of_cells_at(self, position: Position) -> RowOfCells:
        return self._rows[position.row_index]

    def find_cell_at(self, position) -> Cell:
        if self._is_out_of_bounds(position=position):
            return DeadCell(position=Position(-1, -1))
        return self._rows[position.row_index].find_cell_at(position.column_index)

    @staticmethod
    def _is_out_of_bounds(position: Position) -> bool:
        return position.row_index < 0 or position.column_index < 0


class RowOfCells:
    def __init__(self, index: int = 0, number_of_cells: int = 0):
        self._cells: List[Cell] = [DeadCell(position=Position(index, column_index)) for column_index in
                                   range(number_of_cells)]

    def register_alive_at(self, position: Position) -> None:
        self._cells[position.column_index] = AliveCell(position=position)

    def find_cell_at(self, column) -> Cell:
        return self._cells[column]

    def __iter__(self):
        return iter(self._cells)

    def __eq__(self, other) -> bool:
        return isinstance(other, RowOfCells) and self._cells == other._cells
