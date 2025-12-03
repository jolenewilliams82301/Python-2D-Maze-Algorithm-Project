# Python Pathfinding Algorithm Analysis using 2D Mazes
_Implement the A* algorithm, Depth First Search, and Breadth First Search to solve 2D mazes and compare the efficiency of each algorithm. This project was developed as part of the Capstone Project for the NCLab Python Developer Course._

<img width="1536" height="754" alt="capstoneexampleimage2" src="https://github.com/user-attachments/assets/62bc1a53-1b30-4a9f-8580-1a1f836aa217" />

## Features
### Maze Generation
This program uses a maze generation algorithm that incorporates iteration to randomly generate a 2D maze. First, an empty 2D NumPy array is created to represent the maze grid. Next, the maze generation algorithm iterates over each position, randomly choosing adjacent positions to carve an open space until a complete maze path is formed.

### Algorithm Implementation
The A* algorithm, Depth First Search, and Breadth First Search are implemented to solve the generated maze. Each algorithm returns its solution path represented as a list of (x,y) positions.

### Maze Visualization 
The maze and each of the algorithm's solution paths are visualized using Matplotlib. 

### Performance Data Visualization
The number of steps of each algorithm's path and the execution time of each algorithm are recorded. Then, the data is displayed in two bar graphs. 

## Installation instructions
Open a Git Bash terminal and use the following command. This will create a local clone of the repository to your machine.
```
git clone https://github.com/jolenewilliams82301/Python-2D-Maze-Algorithm-Project.git
```
After cloning, navigate to the new directory.
```
cd Python-2D-Maze-Algorithm-Project
```
In order to run this program, Python and pip must be installed on your machine. 

This program also requires importing the Matplotlib, NumPy, and Pandas libraries. Use this command to install the required modules:
```
pip install matplotlib numpy pandas
```
Run the program:
```
python main.py
```
## Author
Jolene Williams

jolenewilliams450@gmail.com
