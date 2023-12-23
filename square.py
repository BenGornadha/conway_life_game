import dataclasses

from cell import Cell
from position import Position


@dataclasses.dataclass(frozen=True)
class Square:
    cell: Cell
    alive_neighbours: int

    def position(self) -> Position:
        return self.cell.position

    def is_alive(self) -> bool:
        return self.cell.is_alive()
