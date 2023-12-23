from __future__ import annotations
import unittest

from cell import AliveCell, DeadCell
from collections_rows_of_cells import CollectionRowOfCells, RowOfCells
from dimension import Dimension
from position import Position


class MyTestCase(unittest.TestCase):

    def test_eq_row_of_cells(self):
        self.assertEqual(RowOfCells(), RowOfCells())

    def test_not_eq_row_of_cells(self):
        r1 = RowOfCells(number_of_cells=2)
        r1.register_alive_at(position=Position(0, 0))

        r2 = RowOfCells(number_of_cells=2)
        r2.register_alive_at(position=Position(0, 1))

        self.assertNotEqual(r1, r2)

    def test_eq_row_of_cells_with_cells_at_same_column(self):
        a_unique_position = Position(0, 4)
        r1 = RowOfCells(number_of_cells=8)
        r1.register_alive_at(position=a_unique_position)

        r2 = RowOfCells(number_of_cells=8)
        r2.register_alive_at(position=a_unique_position)

        self.assertEqual(r1, r2)

    def test_ideas_api(self):
        row_of_cells = RowOfCells(index=3, number_of_cells=1)
        row_of_cells.register_alive_at(position=Position(3, 0))

        iter_row_of_cells = iter(row_of_cells)
        sut = next(iter_row_of_cells)

        self.assertIsInstance(sut, AliveCell)
        self.assertEqual(Position(3, 0), sut.position)

    def test_collection_is_iterable(self):
        collection_of_rows_cells = CollectionRowOfCells(dimension=Dimension(number_of_row=1, num_of_columns=1))
        an_iterator = iter(collection_of_rows_cells)
        sut = next(an_iterator)

        self.assertEqual(RowOfCells(index=0, number_of_cells=1), sut)

    def test_collection_iter_gives_row(self):
        collection_of_rows_cells = CollectionRowOfCells(dimension=Dimension(number_of_row=1, num_of_columns=8))

        collection_of_rows_cells.register_alive_at(position=Position(0, 4))
        an_iterator = iter(collection_of_rows_cells)
        sut = next(an_iterator)

        expected = RowOfCells(index=0, number_of_cells=8)
        expected.register_alive_at(position=Position(0, 4))
        self.assertEqual(expected, sut)

    def test__find_cell_in_row(self):
        row = RowOfCells(index=0, number_of_cells=5)
        sut = row.find_cell_at(column=4)

        self.assertEqual(DeadCell(position=Position(0, 0)), sut)

    def test__find_cell_in_row_collection(self):
        c = CollectionRowOfCells(Dimension(10, 10))
        sut = c.find_cell_at(position=Position(8, 2))

        self.assertFalse(sut.is_alive())
        self.assertEqual(DeadCell(position=Position(8, 2)), sut)
