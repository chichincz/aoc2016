import re
def abba(s):
	# zip makes all 4 letter sequences ("pipeline")
	# sequences are joined with '#' symbol so should never get 
	#   false positive in end-start overlap
	z = zip(s, s[1:], s[2:], s[3:])
	# if there is "abba" sequence return True
	return any((a1 == a2) and (a1 != b1) and (b1 == b2) for a1, b1, b2, a2 in z)

def aba_bab(even, odd):
	# zip to make all 3 letter sequences
	z = zip(even, even[1:], even[2:])
	# "find "aba" sequence and also find related "bab" sequence in bracketed sequences
	return any((a1 == a2) and (a1 != b1) and (b1 + a1 + b1 in odd) for a1, b1, a2 in z)

def solve(part=1):
	lines = [re.findall(r"\w+", line) for line in open('aoc16d07.in')]
	# (odd seq, even seq)
	seqs = [( '#'.join(line[1::2]), '#'.join(line[::2]) ) for line in lines]
	# even sequences (those in "[]" brackets) must not contain "abba"
	# odd must have "abba" sequence
	# sum all positives
	if part==1:
		res = sum(not abba(even) and abba(odd) for even, odd in seqs)
	# even sequences (those in "[]" brackets) must not contain "bab"
	# odd must have "aba" sequence
	# b and a letters in odd and even sequences must match
	elif part==2:
		res = sum(aba_bab(even, odd) for even, odd in seqs)
	print(res)
	

solve(part=1)
solve(part=2)