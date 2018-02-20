#!/usr/bin/env python
import sys
import random 
import math
import json

class ExpressionNode:
	def __init__(self, exp, parent):
		self.parent = parent
		self.expression = ""
		self.children = []
		self.height = 0
		self.numNodes = 0
		self.type = "variable"
		if type(exp) is list:
			self.expression = exp.pop(0)
			self.type = "operator"
			for args in exp:
				self.children.append(ExpressionNode(args, self))
		else:
			self.expression = exp

	def toList(self):
		l = [self.expression]
		if self.children:
			for child in self.children:
				if child.children:
					l.append(child.toList())
				else:
					next = child.expression
					l.append(next)
		return l

	def printDetail(self):
		print("node expression: " + str(self.expression))
		if self.parent is None:
			print("node parent: " + str(self.parent))	
		else:
			print("node parent: " + str(self.parent.expression))
		print("node type: " + str(self.type))
		print("node height: " + str(self.height))
		print("node children: ")
		for child in self.children:
			print(child.expression)
		if self.children:
			for child in self.children:
				child.printDetail()

	def updateHeight(self):
		if not self.children:
			self.height = 0
		else:
			for child in self.children:
				child.updateHeight()
			maxHeight = 0;
			for child in self.children:
				if child.height > maxHeight:
					maxHeight = child.height
			self.height = maxHeight + 1

	def updateNumNodes(self):
		if not self.children:
			self.numNodes = 1
		else:
			for child in self.children:
				child.updateNumNodes()
				self.numNodes += child.numNodes
			self.numNodes += 1


	def equal(self, expNode):
		equal = True
		if self.expression != expNode.expression:
			equal = False
		else:
			if len(self.children) != len(expNode.children):
				equal = False;
			else:
				for i in range(len(self.children)):
					if not self.children[i].equal(expNode.children[i]):
						equal = False
		return equal

	def evaluate(self, var):
		value = 0
		if self.type is "variable":
			if self.expression == "x":
				value = float(var)
			else:
				value = float(self.expression)
		else:
			if ((self.expression == "+") or
			    (self.expression == "-") or
			    (self.expression == "*")): 
				print("here")
				arg1 = self.children[0].evaluate(var)
				arg2 = self.children[1].evaluate(var)
				if self.expression == "+":
					value = arg1 + arg2
				elif self.expression == "-":
					value = arg1 - arg2
				elif self.expression == "*":
					value = arg1 * arg2
				else:
					sys.exit(0)
			elif ((self.expression == "e") or
			      (self.expression == "cos") or
			      (self.expression == "sin")):
				arg1 = self.children[0].evauate(var)
				if self.expression == "e":
					value = math.exp(arg1)
				elif self.expression == "cos":
					value = math.cos(arg1)
				elif self.expression == "sin":
					value = math.sin(arg1)
				else:
					sys.exit(0)
			else:
				sys.exit(0)
		return value;


class ExpressionTree:
	def __init__(self, expList):
		self.root = ExpressionNode(expList, None)
		self.updateHeight()
		self.height = self.root.height
		self.updateNumNodes()
		self.numNodes = self.root.numNodes

	def toList(self):
		return self.root.toList()

	def printTree(self):
		print(self.toList())

	def printDetailTree(self):
		print("tree height: " + str(self.height))
		self.root.printDetail()

	def updateHeight(self):
		self.root.updateHeight()

	def updateNumNodes(self):
		self.root.updateNumNodes()

	def selectRandomSubtree(self):
		subtree = None
		possible = []
		prob = self.numNodes
		for child in self.root.children:
			possible.append(child)
		while subtree is None and possible:
			r = random.randint(0, len(possible) - 1)
			node = possible.pop(r)
			n = random.randint(1, prob)
			possible.extend(node.children)
			if (n == 1) or (not possible):
				subtree = node
		return subtree

	def mutate(self):
		oldNode = self.selectRandomSubtree()
		newExp = randomExpression(0, self.height, 2147483647)
		newTree = ExpressionTree(newExp)
		newNode = newTree.root
		newNode.parent = oldNode.parent
		for i in range(len(oldNode.parent.children)):
			if oldNode.equal(oldNode.parent.children[i]):
				oldNode.parent.children[i] = newNode
		self.updateHeight()
		self.updateNumNodes()

	def crossover(self, otherTree):
		node1 = self.selectRandomSubtree()
		node2 = otherTree.selectRandomSubtree()
		tempParent = node1.parent
		node1.parent = node2.parent
		node2.parent = tempParent
		for i in range(len(node2.parent.children)):
			if node1.equal(node2.parent.children[i]):
				node2.parent.children[i] = node2
		for i in range(len(node1.parent.children)):
			if node2.equal(node1.parent.children[i]):
				node1.parent.children[i] = node1
		
	def evaluate(self, var):
		return self.root.evaluate(var)

	def equal(self, expTree):
		return self.root.equal(expTree.root)

def randomExpression(curHeight, maxHeight, maxNum):
	expression = []
	prob = random.randint(0, maxHeight)
	if prob > curHeight:
		# operator
		degree = random.randint(1, 2)
		operator = random.randint(0, 2)
		if degree == 1:
			if operator == 0:
				expression.append("e")
			elif operator == 1:
				expression.append("sin")
			elif operator == 2:
				expression.append("cos")
			else:
				sys.exit(0)
			arg = randomExpression(curHeight + 1, maxHeight, maxNum)
			expression.append(arg)
		elif degree == 2:
			if operator == 0:
				expression.append("+")
			elif operator == 1:
				expression.append("-")
			elif operator == 2:
				expression.append("*")
			else:
				sys.exit(0)
			firstArg = randomExpression(curHeight + 1, maxHeight, maxNum)
			secondArg = randomExpression(curHeight + 1, maxHeight, maxNum)
			expression.append(firstArg)
			expression.append(secondArg)
		else:
			sys.exit(0)
	else:
		# variable
		num = random.randint(0, 1)
		if num == 0:
			# x
			expression = "x"
		elif num == 1:
			# real number
			expression = (random.gauss(0, maxNum))
		else:
			sys.exit(0)
		if curHeight == 0:
			expression = [expression]
	return expression