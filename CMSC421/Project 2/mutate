#!/usr/bin/env python
import sys
import json
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

expTree = ExpressionTree(decodeExp(json.loads(args[1])))

expTree.mutate()

print(json.dumps(expTree.toList()))