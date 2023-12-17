from __future__ import annotations

import dataclasses
from typing import Optional, Set

from cell import Cell
from direction import Directions
from position import Position


@dataclasses.dataclass
class Neighborhood:
    cell: Cell
    neighbours: Optional[Set[Position]] = None

    def get_neighbours(self):
        if not self.neighbours:
            self.neighbours = set()
            for direction in Directions():
                self.neighbours.add(self.cell.neighbour_at(direction=direction))
        return self.neighbours


class NeighborhoodPositionsCollection:

    def __init__(self):
        self._neighbours = {}

    def register(self, position: Position, neighbours_positions) -> None:
        self._neighbours[position] = neighbours_positions

    def find(self, position: Position) -> Set[Position] | None:
        return self._neighbours.get(position, None)
