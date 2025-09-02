import pygame
from simulation import Simulation

#region
# SETUP
pygame.init()
pygame.mouse.set_visible(False) # HIDE MOUSE CURSOR IN SIM

# WINDOW AND SIM CONSTS
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 6 # SIZE OF GRID CELL IN PIXELS
FPS = 120
GREY = (29, 29, 29) # DISPLAY SCREEN BACKGROUND COLOR

# MAIN DISPLAY
display_screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Falling Sand Sinulation!")

# CONTROL FPS
clock = pygame.time.Clock()

# INSTANCE OF SIM (HABDLES PARTICLE AND GRID LOGIC)
simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

#endregion

#region
# SIMULATION LOOP
while True:

    # EVENT HANDLING
    simulation.handle_controls() # KEYBOARD/MOUSE INPUT

    # UPDATING STATE
    simulation.update() #UPDATE GRID AND PARTICLES

    # DRAWING
    display_screen.fill(GREY)
    simulation.draw(display_screen)
    
    pygame.display.flip() # DRAW UPDATED FRAMES
    clock.tick(FPS) # TARGET FPS
#endregion