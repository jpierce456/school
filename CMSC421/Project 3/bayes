#!/usr/bin/env python
import sys
import math

args = (sys.argv)

trainingFileName = args[1]
trainingFile = open(trainingFileName, "r")
trainingData = []

for line in trainingFile:
	representative = line.strip().split(",")
	trainingData.append(representative)

trainingFile.close()

dems = 0 # democrats
reps = 0 # republicans
total = 0 # total
demsData = []
repsData = []
totalData = []

for r in trainingData:
	if r[0] == "democrat":
		dems += 1
	if r[0] == "republican":
		reps += 1
	total += 1

for t in range(1, len(trainingData[0])):
	demsTopicData = [0, 0, 0]
	repsTopicData = [0, 0, 0]
	totalTopicData = [0, 0, 0]
	for r in trainingData:
		if r[0] == "democrat":
			if r[t] == "y":
				demsTopicData[0] += 1
			if r[t] == "n":
				demsTopicData[1] += 1
			if r[t] == "?":
				demsTopicData[2] += 1
		if r[0] == "republican":
			if r[t] == "y":
				repsTopicData[0] += 1
			if r[t] == "n":
				repsTopicData[1] += 1
			if r[t] == "?":
				repsTopicData[2] += 1
		if r[t] == "y":
			totalTopicData[0] += 1
		if r[t] == "n":
			totalTopicData[1] += 1
		if r[t] == "?":
			totalTopicData[2] += 1
	demsData.append(demsTopicData)
	repsData.append(repsTopicData)
	totalData.append(totalTopicData)

# print("num of democrats: " + str(dems))
# for t in demsData:
# 	print("votes: " + str(t) + "\t total: " + str(t[0] + t[1] + t[2]))

# print("num of republicans: " + str(reps))
# for t in repsData:
# 	print("votes: " + str(t) + "\t total: " + str(t[0] + t[1] + t[2]))

# print("num of representatives: " + str(total))
# for t in totalData:
# 	print("votes: " + str(t) + "\t total: " + str(t[0] + t[1] + t[2]))


classifyFileName = args[2]
classifyFile = open(classifyFileName, "r")
classifyData = []

for line in classifyFile:
	representative = line.strip().split(",")
	classifyData.append(representative)

classifyFile.close()

demsPrior = float(dems)/float(total)
repsPrior = float(reps)/float(total)

for r in classifyData:
	demsLikelihood = 1.0
	repsLikelihood = 1.0
	for t in range(1, len(r)):
		if r[t] == "y":
			demsLikelihood *= float(demsData[t-1][0])/float(dems)
			repsLikelihood *= float(repsData[t-1][0])/float(reps)
		if r[t] == "n":
			demsLikelihood *= float(demsData[t-1][1])/float(dems)
			repsLikelihood *= float(repsData[t-1][1])/float(reps)
		if r[t] == "?":
			demsLikelihood *= float(demsData[t-1][2])/float(dems)
			repsLikelihood *= float(repsData[t-1][2])/float(reps)
	demsLikelihood *= demsPrior
	repsLikelihood *= repsPrior

	demsProb = demsLikelihood/(demsLikelihood + repsLikelihood)
	repsProb = repsLikelihood/(demsLikelihood + repsLikelihood)
	print(demsProb)
	# print(repsProb)