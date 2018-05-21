
def part1():
	idSum = 0

	with open("aoc16d04.in","r") as infile:
		for line in infile:
			line = line.replace("\n","")
			chksumStart = line.find("[")
			chksum = line[chksumStart+1:-1]
			rooms = line[:chksumStart]
			rooms = rooms.split("-")
			sectorNum = rooms[-1]
			rooms = rooms[:-1]

			failed=False
			dc = {}
			for room in rooms:
				for c in room:
					if c in dc:
						dc[c] += 1
					else:
						dc[c] = 1
			for a in chksum:
				best = ('_', 0)
				for key, value in dc.items():
					if value > best[1]:
						best = (key,value)
				if a != best[0]:
					failed=True 
				print(best)
				del dc[best[0]]
				if failed:
					break
			if not failed:
				idSum += int(sectorNum)

	print(idSum)

import re, collections, string

def caesar_cipher(n):
    az = string.ascii_lowercase
    x = n % len(az)
    return str.maketrans(az, az[x:] + az[:x])

def solutions():
	ans1 = 0
	regex = r'([a-z-]+)(\d+)\[(\w+)\]'
	with open("aoc16d04.in","r") as fp:
	    for code, sid, checksum in re.findall(regex, fp.read()):
	        sid = int(sid)
	        letters = code.replace("-","")
	        tops = [(-n,c) for c,n in collections.Counter(letters).most_common()]
	        ranked = ''.join(c for n,c in sorted(tops))
	        if ranked.startswith(checksum):
	            ans1 += sid
	            decoded = code.translate(caesar_cipher(sid))
	            if 'northpole' in decoded:
	                print(decoded, sid)
	print(ans1)

solutions()

					