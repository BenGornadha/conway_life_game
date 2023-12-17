import unittest

from cell import AliveCell
from neighborhood import Neighborhood
from position import Position


class MyTestCase(unittest.TestCase):
    def test_position_0_0_has_8_neighbours(self):
        neighborhood = Neighborhood(cell=AliveCell(position=Position(0,0)))
        all_neighbours_position = neighborhood.get_neighbours()
        expected = {Position(-1, -1), Position(-1, 0), Position(-1, 1),
                    Position(0, -1), Position(0, 1),
                    Position(1, -1), Position(1, 0), Position(1, 1)
                    }
        self.assertEqual(expected, all_neighbours_position)
