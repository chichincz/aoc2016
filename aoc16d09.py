import re

def solve(part=1):
	with open("aoc16d09.in") as fp:
		if part == 1:
			final = ""
			ci = 0
			for line in fp:
				for m in re.finditer(r"(\(\d+x\d+\))", line):
					if m.start() < ci:
						continue
					size, repeat = map(int, m.groups(0)[0].replace("(","").replace(")","").split("x"))
					subs = line[m.end():m.end()+size] * repeat
					final += subs
					ci = m.end() + size
			# dont even need the decompressed string lol
			print(len(final))
		elif part == 2:
			# this part is hard
			for line in fp:
				strvalues = [1 for c in line]
				for m in re.finditer(r"(\(\d+x\d+\))", line):
					size, repeat = map(int, m.groups(0)[0].replace("(","").replace(")","").split("x"))
					strvalues[m.end():m.end()+size] = [x*repeat for x in strvalues[m.end():m.end()+size]]
					strvalues[m.start():m.end()] = [0]*(m.end()-m.start())
				print(sum(strvalues)) # 11,052,855,125


#solve(part=1)
solve(part=2)
