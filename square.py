from __future__ import annotations

import dataclasses

from v5.cell import Cell
from v5.position import Position


@dataclasses.dataclass(frozen=True)
class Square:
    cell: Cell
    alive_neighbours: int

    def position(self) -> Position:
        return self.cell.position

    def is_alive(self) -> bool:
        return self.cell.is_alive()
