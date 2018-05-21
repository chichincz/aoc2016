import hashlib
from collections import OrderedDict

def part1():	
	result = ""
	i = 0
	for runs in range(8):
		h = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"	
		while h[:5] != "00000":
			code = "ugkcyxxp" + str(i)
			code = str.encode(code)
			h = hashlib.md5(code).hexdigest()
			i += 1
		result += h[5]
	print(result)

def part2():	
	result = {}
	i = 0
	while len(result) < 8:
		h = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"	
		while h[:5] != "00000":
			code = "ugkcyxxp" + str(i)
			code = str.encode(code)
			h = hashlib.md5(code).hexdigest()
			i += 1
		if h[5] < '8':
			if h[5] not in result:
				result[h[5]] = h[6]
				
	#result = OrderedDict(sorted(result.items(), key=lambda t: t[0]))
	stri = ""
	for c in "01234567":
		stri += result[c]
	print(stri)

part1()
part2()

					