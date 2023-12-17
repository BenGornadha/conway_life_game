from __future__ import annotations
import dataclasses


@dataclasses.dataclass(frozen=True)
class North:
    relative_x = 1
    relative_y = 0


@dataclasses.dataclass(frozen=True)
class East:
    relative_x = 0
    relative_y = 1


@dataclasses.dataclass(frozen=True)
class South:
    relative_x = -1
    relative_y = 0


@dataclasses.dataclass(frozen=True)
class West:
    relative_x = 0
    relative_y = -1


@dataclasses.dataclass(frozen=True)
class NorthEast:
    relative_x = 1
    relative_y = 1


@dataclasses.dataclass(frozen=True)
class NorthWest:
    relative_x = 1
    relative_y = -1


@dataclasses.dataclass(frozen=True)
class SouthEast:
    relative_x = -1
    relative_y = 1


@dataclasses.dataclass(frozen=True)
class SouthWest:
    relative_x = -1
    relative_y = -1


class Directions:

    def __iter__(self):
        self._directions = {North, West, East, South, NorthEast, NorthWest, SouthEast, SouthWest}
        return iter(self._directions)

Direction = North | East | West | South | NorthWest | NorthEast | SouthWest | SouthEast
