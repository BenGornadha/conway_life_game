import pygame

from collections_rows_of_cells import CollectionRowOfCells
from dimension import Dimension
from grid import Grid
from position import Position


class Interface:
    BLACK = (255, 255, 255)
    WHITE = (0, 0, 0)
    CELL_SIZE = 4

    def __init__(self, dimension: Dimension) -> None:
        pygame.init()
        self._world_dimension = dimension
        self._height = self._world_dimension.number_of_row * Interface.CELL_SIZE
        self._width = self._world_dimension.number_of_columns * Interface.CELL_SIZE
        self._window = pygame.display.set_mode((self._width, self._height))

    def display_all_cells(self, all_cells: CollectionRowOfCells) -> None:
        for row_number, row in enumerate(range(self._world_dimension.number_of_row)):
            for column_number, _ in enumerate(range(self._world_dimension.number_of_columns)):
                couleur = Interface.WHITE if all_cells.find_cell_at(
                    Position(row_number, column_number)).is_alive() else Interface.BLACK

                pygame.draw.rect(self._window, couleur,
                                 (column_number * Interface.CELL_SIZE, row_number * Interface.CELL_SIZE,
                                  Interface.CELL_SIZE, Interface.CELL_SIZE))
        pygame.display.flip()
