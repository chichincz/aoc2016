pads = (
	('_','_','_','_','_','_','_'),
	('_','_','_','1','_','_','_'),
	('_','_','2','3','4','_','_'),
	('_','5','6','7','8','9','_'),
	('_','_','A','B','C','_','_'),
	('_','_','_','D','_','_','_'),
	('_','_','_','_','_','_','_')
)

def moveAgent(agent, c):
	if c == 'U':
		if pads[agent[0]-1][agent[1]] != '_':
			new = (agent[0]-1, agent[1])
			return new
	elif c == 'D':
		if pads[agent[0]+1][agent[1]] != '_':
			new = (agent[0]+1, agent[1])
			return new
	elif c == 'L':
		if pads[agent[0]][agent[1]-1] != '_':
			new = (agent[0], agent[1]-1)
			return new
	elif c == 'R':
		if pads[agent[0]][agent[1]+1] != '_':
			new = (agent[0], agent[1]+1)
			return new
	return agent

def part2():
	agent = (3, 1)
	
	with open("aoc16d02.in","r") as infile:
		for line in infile:
			for c in line:
				agent = moveAgent(agent, c)
				
			# line finished
			print(pads[agent[0]][agent[1]])

part2()

					