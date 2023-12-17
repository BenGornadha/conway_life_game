import random

import pygame

from cell import AliveCell
from dimension import Dimension
from grid import Grid
from interface import Interface
from position import Position
from world import World


def generate_first_grid(size: int):
    grid = Grid(dimensions=Dimension(size, size))
    for row_idx in range(size):
        for col_idx in range(size):
            if random.choice(["X", "O", "X"]) == "O":
                grid.register_cell(cell=AliveCell(position=Position(row_index=row_idx, column_index=col_idx)))
    return grid


if __name__ == '__main__':
    grid = generate_first_grid(size=100)
    world = World(grid=grid)
    interface = Interface(dimension=Dimension(100, 100))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        interface.display_grid(world.display())
        world = world.tick()
