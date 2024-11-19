# README 

## Summary
This project is built on [PyGame](https://www.pygame.org/wiki/about) and inspired by the [Build Asteroids](https://www.boot.dev/lessons/5be3e3bd-efb5-4664-a9e9-7111be783271) guided project on [Boot.dev](https://www.boot.dev/tracks/backend).

After completing the lessons of a project I have further enriched the game with 
features, optimizations, and additional gameplay aspects - some of which will be 
discussed below in this README.

## How to run this project

This project uses Python 3, Python Virtual Environments, and the Package Installer for Python, PIP

1. Install `python`
1. Clone this repository
1. Activate the Virtual Environment by running `./venv/bin/activate`
    - Your shell should now show `(venv)` as a prefix in your prompt
1. Install packages by running `pip install -r requirements.txt`
1. Launch the game by running `python main.py`


# Collision Detection in 2D

## Circles

Collision detection of two circles, given their respective centers and radii is rather trivial.

Simply compare the distance between the two centers with the value of the combined radii, if the distance, `d` is greater than the total combined radii, the circles do not intersect, and thus do no collide. However if the sum of the radii is greater than the distance between the centers, the cirlces do intersect.

## Line Segments


## Circle and a Line Segment


### Dot Product of Vectors


## Optimizations via Geometry Constraints

### Circles First