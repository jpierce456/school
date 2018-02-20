This project takes an initial sample of data and randomly creates an expression to model the data.
There are 4 files to run: initial, mutate, crossover, and error

initial randomly generates an expression tree.  
The expression can have a varialble (x) or an integer (1, -10, 2000, etc) or an operator.  The operator can be either a single degree (e^x, cos(x), sin(x)) or two degrees (x*x, x+x, x-x).
The expression is printed as a json object.  For example, the expression f(x) = 2*(x+1) + 3 would be printed as [+, [*, [x, 1], 2], 3] 

mutate randomly changes a node in the expression tree to a new tree
For example, the tree [*, 2, 3] could mutate to [*, [+, x, 3], 2]

crossover randomly swaps nodes between two different expression tress
For example, the trees [*, x, 4] and [cos, 5] could be swapped to become [5] and [cos, [*, x, 4]]

error calculates the error between the expression and the given data