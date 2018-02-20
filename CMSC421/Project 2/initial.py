#!/usr/bin/env python
import sys
import json
from expression import *

maxNum = 2147483647
maxHeight = 8

expression = randomExpression(0, maxHeight, maxNum)

print(json.dumps(expression))