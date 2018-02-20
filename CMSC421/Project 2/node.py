#!/usr/bin/env python
import sys
import random 
import json

class FunctionNode:
	def __init__(self, parent, maximum, maxHeight):
		self.height = 0
		if parent != None:
			self.height = parent.height + 1
		self.parent = parent
		self.type = None
		self.operator = None
		self.arguments = []
		oper = random.randint(0, maxHeight)
		if oper >= self.height:
			# operator
			degree = random.randint(1, 2)
			if degree == 1:
				# unary operator
				self.type = "u"
				u = random.randint(0, 2)
				if u == 0:
					# e
					self.operator = "e"
				elif u == 1:
					# sin
					self.operator = "sin"
				elif u == 2:
					# cos
					self.operator = "cos"
				else:
					sys.exit(0)
				self.arguments.append(FunctionNode(self, maximum, maxHeight))
			elif degree == 2:
				# binary operator
				self.type = "b"
				b = random.randint(0, 2)
				if b == 0:
					# addition
					self.operator = "+"
				elif b == 1:
					# subtraction
					self.operator = "-"
				elif b == 2:
					# multiplication
					self.operator = "*"
				else:
					sys.exit(0)
				self.arguments.append(FunctionNode(self, maximum, maxHeight))
				self.arguments.append(FunctionNode(self, maximum, maxHeight))
			else:
				sys.exit(0)
		else:
			# variable
			self.type = "v"
			num = random.randint(0, 1)
			if num == 0:
				# x
				self.operator = "x"
			elif num == 1:
				# real number
				self.operator = '{:.5f}'.format(random.gauss(0, maximum))
			else:
				sys.exit(0)

	def listFunction(self):
		l = [self.operator]
		if self.type == "b" or self.type == "u":
			for arg in self.arguments:
				if arg.type == "v":
					l.append(arg.operator)
				else:
					next = arg.listFunction()
					l.append(next)
		return l

def stringToNode(exp):
	l = json.loads(exp)
	print(l)
	print(len(l))
	print(l[0])
