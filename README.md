# Perfect circle

This is a simple drawing app built using Django that allows users to draw circles on a canvas using their mouse. The app calculates the accuracy of the drawn circle and displays it on the screen. The stroke color of the circle changes based on the change in accuracy.

## Prerequisites

Before using the app, you'll need to have Python 3 and Django installed on your computer.

## Installation

To install Python 3, visit the [Python website](https://www.python.org/downloads/) and follow the instructions for your operating system.

Once you have Python 3 installed, you can install Django by opening a command prompt or terminal and running the following command:

pip install Django


## Running the App

To run the app, navigate to the directory where the app's code is located and run the `python manage.py runserver` command. This will start the app and make it available at `http://localhost:8000` in your web browser.

## Using the App

To use the app, open your web browser and navigate to `http://localhost:8000`. Click and hold your mouse button down on the canvas and move your mouse to draw a circle. Release the mouse button to stop drawing. The accuracy of the drawn circle will be displayed on the screen.

The stroke color of the circle will change based on the change in accuracy. If the accuracy is increasing, the stroke color will transition from red to green through yellow and orange. If the accuracy is decreasing, the stroke color will transition from green to red through yellow and orange.

