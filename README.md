# Maze Solver

This repository contains Python code that implements a Breadth-First Search (BFS) algorithm to find the shortest path from a source point (marked as "S") to a destination point (marked as "D") in a maze represented by text files.

## Usage

**1. Create Maze Text Files:**

- Create three text files named `maze1.txt`, `maze2.txt`, and `maze3.txt`.
- Each file should represent a maze using the following characters:
  - `.`: Empty space (a valid path)
  - `S`: Starting point (source)
  - `D`: Destination point
  - Other characters: Walls (considered impassable)
- Ensure the mazes are rectangular and have the same dimensions (e.g., 10x10 grid).

**2. Run the Script:**

- Save the code in a Python file (e.g., `maze_solver.py`).
- Open a terminal or command prompt and navigate to the directory containing the script and maze files.
- Run the script using the command:

  ```bash
  python maze_solver.py
Output
The script will:

Read each maze file (maze1.txt, maze2.txt, and maze3.txt).
Print the maze for each file.
Calculate the shortest path distance from source to destination using BFS.
Print the shortest path distance for each maze.
Example Maze Files
Here's an example structure for the maze text files:

maze1.txt (similar structure for maze2.txt and maze3.txt)

.S..
....
..#.
....
.D..
Limitations
This code assumes the maze is a rectangular grid with the same dimensions for all three files.
It only considers characters '.', 'S', and 'D' as valid for the maze representation.
Further Enhancements
You can modify the code to handle different maze sizes.
You could improve the output to visualize the shortest path within the maze.
Explore other pathfinding algorithms like A* search for potentially better efficiency.
