from random import choice
from copy import deepcopy

class SlidePuzzle(object):
    left, right, up, down = range(4)
    def __init__(self, n=3):
	grid = [[None] * n for _ in range(n)]
	# For the moment a fix initial state
	numbers = range(1, n**2)
	l = 0
	for i in range(n):
	    for j in range(n):
		if i == n - 1 and j == n - 1:
		    break
		grid[i][j] = numbers[l]
		l += 1
	self.space = (n - 1, n - 1)
	self.grid = grid
        self.goal_grid = deepcopy(grid)
        # dicttionary with the goal positions
        tile_goals = {}
        for i in range(n):
            for j in range(n):
                tile = grid[i][j]
                if tile:
                    tile_goals[tile] = (i, j)
        self.tile_goals = tile_goals
	self.n = n

    def __str__(self):
        h_line = (2 * self.n + 1) * '-'
        s = [h_line]
        for i in range(self.n):
	    line = ['|']
	    for j in range(self.n):
		g = self.grid[i][j]
		if g:
		    line.append(str(g))
		else:
		    line.append(' ')
		line.append('|')
	    s.append(''.join(line))
	    s.append(h_line)

        return '\n'.join(s)

    def actions(self):
	acts = []
	i, j = self.space
	grid = self.grid
	n = self.n
	if i - 1 >= 0: # check to the left
	    acts.append(((i-1, j), (i,j)))
	if i + 1 < n: # check to the right
	    acts.append(((i+1, j), (i, j)))
	if j - 1 >= 0: # check up
	    acts.append(((i, j-1), (i, j)))
	if j + 1 < n: # check down
	    acts.append(((i, j+1), (i, j)))
        return acts

    def move(self, location):
	i, j = location[0]
	p, q = self.space
	self.grid[i][j], self.grid[p][q] = self.grid[p][q], self.grid[i][j]
	self.space = (i, j)

    def shuffle(self):
	n_moves = 1000
	for _ in range(n_moves):
	    self.move(choice(self.actions()))

    def is_solved(self):
        return self.grid == self.goal_grid

    def get_state(self):
        return tuple(tuple(row) for row in self.grid)

    def h(self):
        """Return the heuristic cost of the current state.

        Use the sum of the Manhattan distances from current position to the goal.
        """
        h = 0
        for i in range(self.n):
            for j in range(self.n):
                tile = self.grid[i][j]
                if tile:
                    i_goal, j_goal = self.tile_goals[tile]
                    h += abs(i - i_goal) + abs(j - j_goal)
        return h
                

def solve(puzzle):
    print 'Solving'
    print puzzle
    print

    u = {}
    while True:
        if puzzle.is_solved():
            print 'Solved!'
            return
        state = puzzle.get_state()
        actions = puzzle.actions
        # update u for the current state
        
        
def experiment_1():

    print 'Testing slide puzzle'
    puzzle = SlidePuzzle()
    print puzzle
    puzzle.shuffle()
    print puzzle
    n_moves = 5
    print puzzle
    for _ in range(n_moves):
	a = puzzle.actions()
	puzzle.move(choice(a))
	print puzzle

def experiment_2():
    puzzle = SlidePuzzle()
    puzzle.shuffle()
    solve(puzzle)
    
if __name__ == '__main__':
    experiment_1()
