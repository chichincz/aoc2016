from collections import Counter

def solve(part=1):
	with open("aoc16d06.in","r") as fp:
		cols = ["" for x in range(9)]
		for line in fp:
			for index, ch in enumerate(line):
					cols[index] += ch
		corrected = ""
		for i in cols:
			if part == 1:
				corrected += Counter(i).most_common(1)[0][0]
			elif part == 2:
				corrected += Counter(i).most_common()[-1][0]
		print(corrected)

solve(part=1)
solve(part=2)


					