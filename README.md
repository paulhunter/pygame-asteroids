# Summary
This project is built on [PyGame](https://www.pygame.org/wiki/about) and inspired by the [Build Asteroids](https://www.boot.dev/lessons/5be3e3bd-efb5-4664-a9e9-7111be783271) guided project on [Boot.dev](https://www.boot.dev/tracks/backend).

After completing the lessons of a project I have further enriched the game with 
features, optimizations, and additional gameplay aspects - some of which will be 
discussed below in this README.

# How to run this project

This project uses Python 3, Python Virtual Environments, and the Package Installer for Python, PIP

1. Install `python`
1. Clone this repository
1. Activate the Virtual Environment by running `source ./venv/bin/activate`
    - Your shell should now show `(venv)` as a prefix in your prompt
1. Install packages by running `pip install -r requirements.txt`
1. Launch the game by running `python main.py`


# Gameplay

## Controls
- W / UP - Thrust Forward
- S / DOWN - Thrust Backward
- A / LEFT - Rotate Counter Clockwise
- D / RIGHT - Rotate Clockwise
- Q - Retro Thrusters (Brakes)
- SPACE - Fire Blaster

## Asteroids
Asteroids come in multiple sizes. When larger asteroids are blasted, they often break into small pieces. 

## Ship Modifiers
Periodically you will spot non-asteroid objects floating through space. These are ship modifiers, upgrades to your ship.

### Fire Rate Increase
[NEED AN IMAGE HERE]()
This will increase your blasters fire rate. The effect stacks are more modifiers are collected. 

### Shield Generators
[NEED AN IMAGE HERE]()
Adds a shield field to your ship. Shields collapse when the come into contact with an asteroid, disipating its total energy into the rock and destroying it completely.


# Behind the Scenes

## Collision Detection

## Circles

Collision detection of two circles, given their respective centers and radii is rather trivial.

Simply compare the distance between the two centers with the value of the combined radii, if the distance, `d` is greater than the total combined radii, the circles do not intersect, and thus do no collide. However if the sum of the radii is greater than the distance between the centers, the cirlces do intersect.

## Line Segments


## Circle and a Line Segment


### Dot Product of Vectors


## Optimizations via Geometry Constraints

### Circles First