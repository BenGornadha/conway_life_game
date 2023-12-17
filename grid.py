from __future__ import annotations

from typing import List

from v5.cell import Cell, DeadCell
from v5.dimension import Dimension
from v5.neighborhood import NeighborhoodPositionsCollection, Neighborhood
from v5.position import Position
from v5.square import Square


class DeadGridBuilder:
    def __init__(self):
        self._dimensions = Dimension(0, 0)
        self._grid = []

    def with_dimensions(self, dimensions) -> DeadGridBuilder:
        self._dimensions = dimensions
        return self

    def build(self) -> List[List[DeadCell]]:
        self._fill()
        return self._grid

    def _fill(self) -> None:
        grid = []
        for row_index in range(self._dimensions.number_of_row):
            row_of_cells = self._create_row_of_dead_cells(row_index)
            grid.append(row_of_cells)
        self._grid = grid

    def _create_row_of_dead_cells(self, row_index: int) -> List[DeadCell]:
        row = []
        for col_index in range(self._dimensions.num_of_columns):
            row.append(DeadCell(position=Position(row_index=row_index, column_index=col_index)))
        return row


CellRow = List[Cell]
AllCells = List[CellRow]


class Grid:
    CACHE_NEIGHBOURS = NeighborhoodPositionsCollection()

    def __init__(self, dimensions: Dimension):
        self._dimensions = dimensions
        self._grid: AllCells = DeadGridBuilder().with_dimensions(dimensions=dimensions).build()
        self._alive_counter = AliveCounter(all_cells=self._grid)
        self.current_row = 0
        self.current_col = 0

    @property
    def grid(self) -> AllCells:
        return self._grid

    @property
    def dimensions(self) -> Dimension:
        return self._dimensions

    def register_cell(self, cell: Cell) -> None:
        if cell.is_alive():
            position = cell.position
            self._grid[position.row_index][position.column_index] = cell

    def __eq__(self, other: Grid) -> bool:
        return isinstance(other, Grid) and self._grid == other._grid

    def __iter__(self) -> Grid:
        return self

    def __next__(self) -> Square:
        if self.current_row < self._dimensions.number_of_row:
            cell = self._grid[self.current_row][self.current_col]
            self._increment_indexes_for_next_iteration()
            return Square(cell=cell, alive_neighbours=self._alive_counter.count_for_cell(cell=cell))
        raise StopIteration

    def _increment_indexes_for_next_iteration(self):
        self._update_current_column_index()
        if self.current_col == self._dimensions.num_of_columns:
            self._go_to_next_row()

    def _update_current_column_index(self):
        self.current_col += 1

    def _go_to_next_row(self) -> None:
        self.current_col = 0
        self.current_row += 1


class AliveCounter:
    CACHE_NEIGHBOURS = NeighborhoodPositionsCollection()

    def __init__(self, all_cells: AllCells):
        self._grid = all_cells
        self.i = 0

    def count_for_cell(self, cell):
        return self._count_alive_neighbours_for(cell=cell)

    def _count_alive_neighbours_for(self, cell: Cell) -> int:
        neighbours = self.CACHE_NEIGHBOURS.find(position=cell.position)
        if neighbours is None:
            neighborhood = Neighborhood(cell=cell)
            neighbours = neighborhood.get_neighbours()
            self.CACHE_NEIGHBOURS.register(position=cell.position, neighbours_positions=neighbours)
        alive_neighbours = 0
        for position in neighbours:
            alive_neighbours += self._is_alive_cell_at(position)
        return alive_neighbours

    def _is_alive_cell_at(self, position: Position) -> bool:
        try:
            if self._is_out_of_bounds(position=position):
                return False
            return self._grid[position.row_index][position.column_index].is_alive()
        except IndexError as _:
            return False

    @staticmethod
    def _is_out_of_bounds(position: Position) -> bool:
        return position.row_index < 0 or position.column_index < 0
