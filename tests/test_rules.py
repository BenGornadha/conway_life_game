import unittest

from cell import AliveCell, DeadCell, Cell
from square import Square
from position import Position


class GameOfLifeRules:
    def apply(self, square: Square) -> Cell:
        position = square.position()
        if square.alive_neighbours == 3:
            return AliveCell(position=position)
        if square.alive_neighbours == 2:
            if square.is_alive():
                return AliveCell(position=position)
        return DeadCell(position=position)


class MyTestCase(unittest.TestCase):
    def test_a_alive_cell_with_1_alive_neighbours_will_stays_dead(self):
        rules = GameOfLifeRules()
        sut = rules.apply(square=Square(cell=AliveCell(Position(0, 0)), alive_neighbours=1))
        self.assertFalse(sut.is_alive())

    def test_a_alive_cell_with_2_alive_neighbours_will_stays_alive(self):
        rules = GameOfLifeRules()
        sut = rules.apply(square=Square(cell=AliveCell(Position(0, 0)), alive_neighbours=2))
        self.assertTrue(sut.is_alive())

    def test_a_alive_cell_with_3_alive_neighbours_will_stays_alive(self):
        rules = GameOfLifeRules()
        sut = rules.apply(square=Square(cell=AliveCell(Position(0, 0)), alive_neighbours=3))
        self.assertTrue(sut.is_alive())

    def test_a_alive_cell_with_4_alive_neighbours_will_die(self):
        rules = GameOfLifeRules()
        sut = rules.apply(square=Square(cell=AliveCell(Position(0, 0)), alive_neighbours=4))
        self.assertFalse(sut.is_alive())

    def test_a_dead_cell_with_3_alive_neighbours_will_come_to_life(self):
        rules = GameOfLifeRules()
        sut = rules.apply(square=Square(cell=DeadCell(Position(0, 0)), alive_neighbours=3))
        self.assertTrue(sut.is_alive())

    def test_a_dead_cell_with_2_alive_neighbours_will_stay_dead(self):
        rules = GameOfLifeRules()
        sut = rules.apply(square=Square(cell=DeadCell(Position(0, 0)), alive_neighbours=2))
        self.assertFalse(sut.is_alive())
