# Graviational Field Simulator
Easy to use environment allowing to place physic bodies in space and watch how they behave.

## Features
### Adding bodies
You can use our pre-defined planet objects like earth or sun.

### Adding bigger number of objects
Things turn exciting when it is possible to observe multiple objects reacting to each other.

## How to use it
### Dependencies
This project requires Python 3 with Panda3d, scipy and numpy

### Default simulation
Clone this repo on your local machine and go into project folder

    git clone https://github.com/FranciszekPin/gravity-field-simulator
    cd <bleble>


To see default simulation just run

    python3 GameManager.py

You should see few planets orbiting sun

### Making own simulation
#### Add single planet
In `BallManager.py` there is function `render()`. It should contain all 
