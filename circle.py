#!/bin/python3

import math

class Circle():
	def __init__(self,radius=1):
		self.radius = radius

	def __repr__(self):
		return("Circle({:.0f})".format(self.radius))

	def new_radius(self,name):
		if name < 0:
			raise ValueError("Radius cannot be negative")
		self.radius1 = name

	def get_new_radius(self):
		return(self.radius1)

	def new_diameter(self,name):
		self.radius = name/2

	def get_new_diameter(self):
		return(self.radius*2)

	def new_area(self,name):
		raise AttributeError("can\'t set attribute")

	def get_new_area(self):
		return(math.pi*self.radius**2)

	radius = property(get_new_radius,new_radius)
	diameter = property(get_new_diameter,new_diameter)
	area = property(get_new_area,new_area)
	