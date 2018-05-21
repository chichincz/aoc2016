import sys
import time

class Screen(object):

	def __init__(self,w,h):
		self.pixels = [False for x in range(w*h)]
		self.w = w
		self.h = h

	def rect(self,a,b):
		for y in range(b):
			for x in range(a):
				index = y*self.w + x
				self.pixels[index] = True

	def getRow(self,y):
		return self.pixels[y*self.w : y*self.w+self.w]

	def getColumn(self,x):
		return self.pixels[x::self.w]

	def getPixels(self):
		return self.pixels

	def getHeight(self):
		return self.h

	def getWidth(self):
		return self.w

	def rotateRow(self,y,value):
		row = self.getRow(y)
		row = row[-value:] + row[:-value]
		self.pixels = self.pixels[:y * self.w] + row + self.pixels[y * self.w+self.w:]

	def rotateColumn(self,x,value):
		column = self.getColumn(x)
		column = column[-value:] + column[:-value]
		# scuffed
		for y in range(self.h):
			self.pixels[y * self.w + x] = column[y]

	def countPixelsOn(self):
		return len([p for p in self.pixels if p])


def solve(part=1):
	screen = Screen(w=50, h=6)
	with open("aoc16d08.in") as fp:
		for line in fp:
			line = line.split(" ")
			if line[0] == "rect":
				a,b = [int(e) for e in line[1].split("x")]
				screen.rect(a,b)
			elif line[1] == "row":
				y = int(line[2].split("=")[1])
				value = int(line[4])
				screen.rotateRow(y,value)
			elif line[1] == "column":
				x = int(line[2].split("=")[1])
				value = int(line[4])
				screen.rotateColumn(x,value)
			p = screen.getPixels()


	if part == 1:
		print(screen.countPixelsOn())
	elif part == 2:
		p = screen.getPixels()
		for y in range(screen.getHeight()):
			for x in range(screen.getWidth()):
				if p[y * screen.getWidth() + x]:
					sys.stdout.write("#")
				else:
					sys.stdout.write(" ")
			sys.stdout.write("\n")

solve(part=1)
solve(part=2)