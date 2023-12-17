from typing import Optional

from direction import Direction
from position import Position
from abc import ABC, abstractmethod

class Cell(ABC):
    @abstractmethod
    def __init__(self):
        self._position: Optional[Position] = None
    @property
    def position(self) -> Position:
        return self._position

    def neighbour_at(self, direction: Direction) -> Position:
        return self._position.neighbour_at(direction=direction)

    def is_alive(self) -> bool:
        raise NotImplemented

    def __eq__(self, other) -> bool:
        return isinstance(other, self.__class__)




class AliveCell(Cell):
    def __init__(self, position: Position):
        self._position = position

    def is_alive(self) -> bool:
        return True

    def __repr__(self) -> str:
        return "O"


class DeadCell(Cell):
    def __init__(self, position: Position):
        self._position = position

    def is_alive(self) -> bool:
        return False

    def __repr__(self) -> str:
        return "X"
