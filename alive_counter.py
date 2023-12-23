from __future__ import annotations

import dataclasses
from typing import Set, Optional

from cell import Cell
from collections_rows_of_cells import CollectionRowOfCells
from direction import Directions
from position import Position


@dataclasses.dataclass
class Neighborhood:
    cell: Cell
    neighbours: Optional[Set[Position]] = None

    def get_neighbours(self):
        if self.neighbours is None:
            self._compute_neighbours_positions()
        return self.neighbours

    def _compute_neighbours_positions(self):
        self.neighbours = set()
        for direction in Directions():
            self.neighbours.add(self.cell.neighbour_at(direction=direction))


class CacheNeighboursPositions:

    def __init__(self) -> None:
        self._neighbours = {}

    def register(self, position: Position, neighbours_positions : Set[Position]) -> None:
        self._neighbours[position] = neighbours_positions

    def find(self, position: Position) -> Set[Position] | None:
        return self._neighbours.get(position, None)


class NeighboursAliveCounter:
    CACHE_NEIGHBOURS = CacheNeighboursPositions()

    def __init__(self, all_cells: CollectionRowOfCells) -> None:
        self._all_cells = all_cells

    def for_a(self, cell: Cell) -> int:
        neighbours_positions = self.CACHE_NEIGHBOURS.find(position=cell.position)
        if neighbours_positions is None:
            neighbours_positions = self._register_in_cache(cell)
        return self._compute_alive_neighbours(neighbours_positions)

    def _register_in_cache(self, cell: Cell):
        neighborhood = Neighborhood(cell=cell)
        neighbours = neighborhood.get_neighbours()
        self.CACHE_NEIGHBOURS.register(position=cell.position, neighbours_positions=neighbours)
        return neighbours

    def _compute_alive_neighbours(self, neighbours: Set[Position]) -> int:
        alive_neighbours = 0
        for position in neighbours:
            alive_neighbours += self._is_alive_cell_at(position)
        return alive_neighbours

    def _is_alive_cell_at(self, position: Position) -> bool:
        try:
            cell = self._all_cells.find_cell_at(position=position)
            return cell.is_alive()
        except IndexError as _:
            return False
