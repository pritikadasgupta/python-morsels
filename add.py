#!/bin/python3

def add(*mats):
	return([[sum(values) for values in zip(*rows)]for rows in zip(*mats)])