# Falling Sand Simulation!

#### video demo: https://www.youtube.com/watch?v=cLyRFSHrfFY

## Description
This falling sand simulator was made using Pygame.ce 2.5.5!

What is pygame?
Pygame-ce is a free open-source Python library used primarily for making games! It's built upon the SDL libary for use of a computers graphics, audio and input devices!

How I used Pygame:
I used Pygames ability to handle input, as well as its ability to render graphics for this project. Getting both mouse and keyboard input to render sand and rock. As well as getting input for erasing the grid and completely clearing it

There are 3 "modes" in this simulator! Sand, Rock, and erase!:
- when in Sand mode, you can place sand anywhere on the grid and watch it fall down. The sand will also trickle down the sides, not just stack ontop of itself!
- When in Rock mode, you can place rock pixels on the grid and it won't fall! Allowing the sand to rest ontop of it and trickle off of it as well!
- When in Erase mode, you can remove particles from the grid!

### CONTROLS
- Left Mouse Button | Add/Remove Particles (sand and rock)
- s key | Change mode to sand
- r key | Change mode to rock
- e key | Change mode to erase
- space key | Clear entire grid

## Project Structure
- project.py | Pygame setup, main logic, and game loop
- grid.py | Handles grid logic
- particle.py | Handles particle logic (sand, rock)
- simulation.py | Handles core game logic (adding/removing particles, and input)
- test_project.py | Project Unit tests
- requirements.txt | Project dependencies
- README.md | Project doc

### Installation
Acquire the repository by with Clone Repository or Download Zip
```bash
git clone https://github.com/solracOneStar/Falling-Sand-Sim

cd Falling-Sand-Sim

pip install -r requirements.txt
```
## Usage
Run the project by executing the main Python file
```bash
python project.py
```

## Tests
Run unit tests for the project:
```bash
pytest test_project.py
```
