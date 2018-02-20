#!/usr/bin/env python
class Square:
    def __init__(self, terrain, y, x, cost, path):
        self.terrain = terrain
        self.y = y
        self.x = x
        self.cost = cost
        self.path = path
        
    def getLeftNeighbor(self, map):
        left = None
        leftX = self.x - 1
        leftY = self.y
        if leftX >= 0:
            leftTerrain = map[leftY][leftX]
            if leftTerrain != "w":
                leftCost = self.cost
                if leftTerrain == "r":
                    leftCost += 1
                elif leftTerrain == "f":
                    leftCost += 2
                elif leftTerrain == "h":
                    leftCost += 5
                elif leftTerrain == "m":
                    leftCost += 10
                else:
                    sys.exit(0)
                leftPath = list(self.path)
                leftPath.append("l")
                left = Square(leftTerrain, leftY, leftX, leftCost, leftPath)
        return left
        
    def getRightNeighbor(self, map):
        right = None
        rightX = self.x + 1
        rightY = self.y
        if rightX < len(map[rightY]):
            rightTerrain = map[rightY][rightX]
            if rightTerrain != "w":
                rightCost = self.cost
                if rightTerrain == "r":
                    rightCost += 1
                elif rightTerrain == "f":
                    rightCost += 2
                elif rightTerrain == "h":
                    rightCost += 5
                elif rightTerrain == "m":
                    rightCost += 10
                else:
                    sys.exit(0)
                rightPath = list(self.path)
                rightPath.append("r")
                right = Square(rightTerrain, rightY, rightX, rightCost, rightPath)
        return right
        
    def getUpNeighbor(self, map):
        up = None
        upX = self.x
        upY = self.y - 1
        if upY >= 0:
            upTerrain = map[upY][upX]
            if upTerrain != "w":
                upCost = self.cost
                if upTerrain == "r":
                    upCost += 1
                elif upTerrain == "f":
                    upCost += 2
                elif upTerrain == "h":
                    upCost += 5
                elif upTerrain == "m":
                    upCost += 10
                else:
                    sys.exit(0)
                upPath = list(self.path)
                upPath.append("u")
                up = Square(upTerrain, upY, upX, upCost, upPath)
        return up
        
    def getDownNeighbor(self, map):
        down = None
        downX = self.x
        downY = self.y + 1
        if downY < len(map):
            downTerrain = map[downY][downX]
            if downTerrain != "w":
                downCost = self.cost
                if downTerrain == "r":
                    downCost += 1
                elif downTerrain == "f":
                    downCost += 2
                elif downTerrain == "h":
                    downCost += 5
                elif downTerrain == "m":
                    downCost += 10
                else:
                    sys.exit(0)
                downPath = list(self.path)
                downPath.append("d")
                down = Square(downTerrain, downY, downX, downCost, downPath)
        return down

    def getNeighbors(self, map):
        n = []
        left = self.getLeftNeighbor(map)
        right = self.getRightNeighbor(map)
        up = self.getUpNeighbor(map)
        down = self.getDownNeighbor(map)
        if left != None:
            n.append(left)
        if right != None:
            n.append(right)
        if up != None:
            n.append(up)
        if down != None:
            n.append(down)
        return n

def taxiDist(sq, y, x):
    return abs(sq.x - x) + abs(sq.y + y)
        
import sys

args = (sys.argv)

fileName = args[1]
initialY = int(args[2])
initialX = int(args[3])
goalY = int(args[4])
goalX = int(args[5])

map = []

visited = []
frontier = []
complete = False

file = open(fileName, "r")
for line in file:
    row = []
    for c in line:
        if c != "\n" and c != "\r":
            row.append(c)
    map.append(row)

start = Square(map[initialY][initialX], initialY, initialX, 0, [])

frontier.append(start)

while not complete and frontier:
    next = frontier[0]
    nextDist = next.cost + taxiDist(next, goalY, goalX)
    for s in frontier:
        sDist = s.cost + taxiDist(s, goalY, goalX)
        if sDist < nextDist:
            next = s
            nextDist = sDist
    frontier.remove(next)
    visited.append(next)
    if next.y == goalY and next.x == goalX:
        complete = True
        print(next.path)
    else:
        n = next.getNeighbors(map)
        for s in n:
            coordVisited = False
            for v in visited:
                if s.x == v.x and s.y == v.y:
                    coordVisited = True
            if not coordVisited:
                frontier.append(s)
if not complete:
    print(None)