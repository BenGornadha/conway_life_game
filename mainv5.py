import random
import time
from timeit import timeit

import pygame

from v5.cell import AliveCell
from v5.dimension import Dimension
from v5.grid import Grid
from v5.position import Position
from v5.world import World


class Interface:
    BLACK = (255, 255, 255)
    WHITE = (0, 0, 0)
    CELL_SIZE = 4

    def __init__(self, dimension: Dimension) -> None:
        pygame.init()
        self._world_dimension = dimension
        self._height = self._world_dimension.number_of_row * Interface.CELL_SIZE
        self._width = self._world_dimension.num_of_columns * Interface.CELL_SIZE
        self._window = pygame.display.set_mode((self._width, self._height))

    def display_grid(self, a_grid) -> None:
        for row_number, row in enumerate(range(self._world_dimension.number_of_row)):
            for column_number, _ in enumerate(range(self._world_dimension.num_of_columns)):
                couleur = Interface.WHITE if a_grid[row_number][column_number].is_alive() else Interface.BLACK

                pygame.draw.rect(self._window, couleur,
                                 (column_number * Interface.CELL_SIZE, row_number * Interface.CELL_SIZE,
                                  Interface.CELL_SIZE, Interface.CELL_SIZE))
        pygame.display.flip()


def generate_first_grid(size: int):
    grid = Grid(dimensions=Dimension(size, size))
    for row_idx in range(size):
        for col_idx in range(size):
            if random.choice(["X", "O", "X"]) == "O":
                grid.register_cell(cell=AliveCell(position=Position(row_index=row_idx, column_index=col_idx)))
    return grid

def loop_world():
    grid = generate_first_grid(size=1000)
    world = World(grid=grid)
    for i in range(10):
        world = world.tick()

if __name__ == '__main__':
    # grid = generate_first_grid(size=200)
    # world = World(grid=grid)
    # interface = Interface(dimension=Dimension(200, 200))
    # running = True
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    #     interface.display_grid(world.display())
    #     world = world.tick()
    print(timeit(loop_world,number=1))
    #117 secondes pour 10 iteration d'un monde 1000 (opti nulle)
    #106 secondes pour 10 iteration d'un monde 1000 (sans opti)

