#!/usr/bin/env python
import sys
import json
import math
from expression import *
def decodeExp(exp):
	l = []
	for arg in exp:
		if type(arg) is list:
			l.append(decodeExp(arg))
		else:
			if type(arg) is unicode:
				l.append(str(arg))
			else:
				l.append(arg)
	return l

args = (sys.argv)

data = []

with open('line.json') as data_file:
	data = json.load(data_file)

expTree = ExpressionTree(decodeExp(json.loads(args[2])))

error = 0

for i in range(len(data)):
	f = expTree.evaluate(i)
	y = data[i]
	error += math.pow(y - f, 2)

print(error)