# Robot Movement GUI

This repository contains a Python-based graphical user interface (GUI) for controlling a robot's movement. The program allows users to send commands to a robot to move forward, backward, left, or right through an intuitive button-based interface. It uses **Tkinter** for the GUI and **Requests** for sending HTTP requests to the robot's server.

## Features

- **Directional Control**  
  Control the robot's movement with buttons for:
  - Forward
  - Backward
  - Left
  - Right

- **GUI Interface**  
  A simple and user-friendly GUI built with Tkinter, featuring labeled buttons for each movement.

- **HTTP Communication**  
  Sends HTTP GET requests to the robot's server to execute movement commands.

## File Descriptions

- **Robot_GUI.py**  
  The main Python script that:
  - Implements the GUI using Tkinter.
  - Defines functions for sending HTTP requests to control the robot's movements.
  - Creates buttons for directional control and displays them in the GUI.

- **README.md**  
  Provides an overview of the project, its features, file descriptions, and usage instructions.

## How to Use

1. Clone this repository to your local machine:
git clone https://github.com/muditm006/Robot-Movement-GUI.git
cd Robot-Movement-GUI

2. Install the required Python library:
pip install requests
3. Run the program:
python Robot_GUI.py
4. Use the GUI to control the robot:
- Click the **Forward**, **Backward**, **Left**, or **Right** buttons to send movement commands to the robot.

5. Ensure that the robot's server is running and accessible at `http://192.168.1.116:8080`. Update the IP address in `Robot_GUI.py` if necessary.

## Libraries Used

- **Tkinter**: For building the graphical user interface.
- **Requests**: For sending HTTP GET requests to control the robot.

## Notes

- The robot's server must be configured to accept HTTP GET requests at the specified endpoints (`/fwd`, `/rev`, `/left`, `/right`).
- Customize button styles (e.g., colors, fonts) by editing the `Robot_GUI.py` script.
- Ensure that your device is connected to the same network as the robot's server.

This project demonstrates how to combine Python's Tkinter and Requests libraries to create a functional GUI for robotic control.
