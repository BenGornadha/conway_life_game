import random
import time

import pygame

from cell import AliveCell
from dimension import Dimension
from grid import Grid
from interface import Interface
from position import Position
from world import World


def generate_first_grid(dimension: Dimension):
    grid = Grid(dimensions=dimension)
    for row_idx in range(dimension.number_of_row):
        for col_idx in range(dimension.num_of_columns):
            if random.choice(["X", "O"]) == "O":
                grid.register_cell(cell=AliveCell(position=Position(row_index=row_idx, column_index=col_idx)))
    return grid


if __name__ == '__main__':
    dimension = Dimension(100, 100)
    grid = generate_first_grid(dimension=dimension)
    world = World(grid=grid)
    interface = Interface(dimension=dimension)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        interface.display_all_cells(world.display())
        world = world.tick()
        time.sleep(0.016)
