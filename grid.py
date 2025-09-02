import pygame

# MAKES 2D GRID
class Grid:
    def __init__(self, width, height, cell_size):
        self.rows = height // cell_size
        self.columns = width // cell_size
        self.cell_size = cell_size
        # INITIALIZE ALL CELLS AS EMPTY
        self.cells = [[None for _ in range(self.columns)] for _ in range(self.rows)]

    # DRAW ALL PARTICLES IN GRID
    def draw(self, display_screen):
        for row in range(self.rows): # ITERATE THROUGH CELLS
            for column in range(self.columns):
                particle = self.cells[row][column]
                if particle is not None: # IF PARTILE EXISTS USER PARTICLES COLOR TO DRAW ON SCREEN
                    color = particle.color
                    pygame.draw.rect(display_screen, color,
                    (column * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size))

    # ADD PARTICLE IF CELL IS EMPTY AND IN BOUNDS
    def add_particle(self, row, column, particle_type):
        if 0 <= row < self.rows and 0 <= column < self.columns and self.is_cell_empty(row, column):
            self.cells[row][column] = particle_type()

    # REMOVES PARTICLES IN CELL
    def remove_particle(self, row, column):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            self.cells[row][column] = None

    # CHECKS FOR EMPTY CELL
    def is_cell_empty(self, row, column):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            if self.cells[row][column] is None:
                return True # IF INSIDE BOUNDS AND CONTAINS NO PARTICLES
        return False

    # PLACES PARTICLE DIRECTLY ON GRID
    def set_cell(self, row, column, particle):
        if not(0 <= row < self.rows and 0 <= column < self.columns):
            return
        self.cells[row][column] = particle

    # GETS PARTICLE AT GRID LOCATION
    def get_cell(self, row, column):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            return self.cells[row][column]
        return None # IF OUT OF BOUNDS OR CELL IS EMPTY

    # CLEARS ENTIRE GRID
    def clear(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.remove_particle(row, column)