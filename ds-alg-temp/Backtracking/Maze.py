# Python3 program to solve Rat in a Maze
# problem using backracking

# Maze size
N = 4

# A utility function to print solution matrix sol
def printSolution( sol ):
	for i in sol:
		for j in i:
			print(str(j) + " ", end ="")
		print("")

# A utility function to check if x, y is valid
# index for N * N Maze
def isSafe( maze, x, y ):
	if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
		return True
	return False

def solveMaze( maze ):
	# Creating a 4 * 4 2-D list
	sol = [ [ 0 for j in range(4) ] for i in range(4) ]
	
	if solveMazeUtil(maze, 0, 0, sol) == False:
		print("Solution doesn't exist")
		return False
	
	printSolution(sol)
	return True
	
# A recursive utility function to solve Maze problem
def solveMazeUtil(maze, x, y, sol):
	# if (x, y is goal) return True
	if x == N - 1 and y == N - 1 and maze[x][y]== 1:
		sol[x][y] = 1
		return True
	
	# Check if maze[x][y] is valid
	if isSafe(maze, x, y) == True:
		# Check if the current block is already part of solution path.
		if sol[x][y] == 1:
			return False
		
		# mark x, y as part of solution path
		sol[x][y] = 1
		
		# Move forward in x direction
		if solveMazeUtil(maze, x + 1, y, sol) == True:
			return True
			
		# If moving in x direction doesn't give solution
		# then Move down in y direction
		if solveMazeUtil(maze, x, y + 1, sol) == True:
			return True
		
		# If moving in y direction doesn't give solution then
		# Move back in x direction
		if solveMazeUtil(maze, x - 1, y, sol) == True:
			return True
			
		# If moving in backwards in x direction doesn't give solution
		# then Move upwards in y direction
		if solveMazeUtil(maze, x, y - 1, sol) == True:
			return True
		
		# If none of the above movements work then
		# BACKTRACK: unmark x, y as part of solution path
		sol[x][y] = 0
		return False

# Driver program to test above function
if __name__ == "__main__":
	# Initialising the maze
	maze = [ [1, 0, 0, 0],
			[1, 1, 0, 1],
			[0, 1, 0, 0],
			[1, 1, 1, 1] ]
			
	solveMaze(maze)

# This code is contributed by Shiv Shankar

# - Backtrack: 정답이라 표시해두고 찾아 들어가다가, 더 이상 답이 없으면 되돌리기.

# - 배열은 2개. (maze, sol)
# - 인덱스 방향 주의: sol[x][y]에서 x가 세로, y가 가로.
#   - 주석에 설명이 잘못 쓰여있음. x가 down, y가 forward임.
