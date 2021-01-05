#!/bin/python3

import math

class Circle():
	def __init__(self, radius=1):
		self.radius = radius
	def __repr__(self):
		return("Circle({:.0f})".format(self.radius))
	@property
	def diameter(self):
		return(float("{}".format((self.radius*2))))
	@property
	def area(self):
		return(float("{}".format((math.pi)*(self.radius**2))))