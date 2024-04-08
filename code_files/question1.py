from sys import stdin

class Solution:
    def __init__(self):
        self.m = []
        self.s = (0, 0) # initialize the row/column index of the source S
        self.d = (0, 0) # initialize the row/column index of the destination D

    def readMaze(self, fn):
        with open(fn, 'r') as file:
            self.m = file.read().splitlines()
        for i, row in enumerate(self.m):
            for j, cell in enumerate(row):
                if cell == 'S':
                    self.s = (i, j)
                elif cell == 'D':
                    self.d = (i, j)

    def printMaze(self):
        '''Prints the maze self.m'''
        for i in range(10):
            print(self.m[i], end="")
        print("\n")

    def neighbors(self, i, j):
        '''Returns the list of self.m[i][j]'s neighbors index (ni, nj) where self.m[ni][nj] is a path'''
        result = []
        # Write your code here
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < 10 and 0 <= nj < 10 and self.m[ni][nj] in ('.', 'S', 'D'):
                result.append((ni, nj))
        return result
    
    def bfs(self):
        '''Returns the shortest path distance from S to D using breadth-first search'''
        dist = [[None for i in range(10)] for j in range(10)]
        queue = []
        queue.append(self.s)
        si, sj = self.s  # Unpacking the tuple
        dist[si][sj] = 0
        while queue:
            i, j = queue.pop(0)  # Extract current position
            if (i, j) == self.d:  # Check if it's the destination
                return dist[i][j]
            for ni, nj in self.neighbors(i, j):  # Explore neighbors
                if dist[ni][nj] is None:  # If not visited
                    dist[ni][nj] = dist[i][j] + 1  # Update distance
                    queue.append((ni, nj))  # Add to queue for further exploration
        return -1  # Return -1 if no path is found

if __name__ == '__main__':
    sol = Solution()
    sol.readMaze("maze3.txt")
    sol.printMaze()
    print(f"The shortest path distance is {sol.bfs()}.")
