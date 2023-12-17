from __future__ import annotations
import dataclasses

from v4.direction import Direction


@dataclasses.dataclass(frozen=True)
class Position:
    row_index: int
    column_index: int

    def neighbour_at(self, direction: Direction) -> Position:
        return Position(row_index=self.row_index + direction.relative_x,
                        column_index=self.column_index + direction.relative_y)
