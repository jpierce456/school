This program implements a* search to find the optimal path between the initial coordinates and the goal coordinates
The program takes a text file, as well as the integer values for the start and goal x and y coordinates respectively.
The map file has a combination of 5 unique characters representing 5 different terrains arranged in a n x m grid.
The 5 different terrains have a different cost associated with traversing that square.
w (water) = unable to cross
r (road) = 1
f (field) = 2
h (hill) = 5
m (mountain) = 10
The program finds the path with the least cost from the start to the goal and prints it as a list.
If there is no possible path, the program prints NULL
