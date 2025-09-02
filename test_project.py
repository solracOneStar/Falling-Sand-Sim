import pytest
from grid import Grid
from particle import SandParticle, RockParticle
from simulation import Simulation

def test_add_and_remove_particle():
    # GRID SHOULD ADD AND REMOVE PARTICLES CORRECTLY
    grid = Grid(100, 100, 10)  # 10x10 GRID
    grid.add_particle(2, 2, SandParticle)
    assert grid.get_cell(2, 2) is not None
    grid.remove_particle(2, 2)
    assert grid.get_cell(2, 2) is None

def test_is_cell_empty():
    # IS_CELL_EMPTY SHOULD RETURN TRUE IF NO PARTICLE IS PRESENT
    grid = Grid(100, 100, 10)
    assert grid.is_cell_empty(0, 0) == True
    grid.add_particle(0, 0, RockParticle)
    assert grid.is_cell_empty(0, 0) == False

def test_sand_particle_update_falls_down():
    # SAND PARTICLES SHOULD FALL IF THE CELL BELOW IS EMPTY
    grid = Grid(100, 100, 10)
    particle = SandParticle()
    grid.set_cell(0, 0, particle)

    # CALL UPDATE ON SAND PARTICLE AT ROW 0, COL 0
    new_row, new_col = particle.update(grid, 0, 0)

    # SHOULD TRY TO MOVE DOWN TO (1, 0)
    assert (new_row, new_col) == (1, 0)

def test_restart_clears_grid():
    # SIMULATION.RESTART SHOULD CLEAR ALL PARTICLES
    sim = Simulation(100, 100, 10)
    sim.grid.add_particle(0, 0, SandParticle)
    assert sim.grid.get_cell(0, 0) is not None
    sim.restart()
    assert sim.grid.get_cell(0, 0) is None

