#!/bin/python3

import math

class Circle():
	def __init__(self, radius=1):
		self.radius = radius
		self.diameter = radius*2
		self.area = (math.pi)*(radius**2)
	def __repr__(self):
		return("Circle({:.0f})".format(self.radius))