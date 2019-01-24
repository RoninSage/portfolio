import numpy
import matplotlib.pyplot as pyplot
import random
import time
import console

startTime = time.time() # program start time

# paramaters
width = 31 # must be odd
height = 31 # must be odd
runTime = 3 # define computation time
#random.seed(290) # set randomisation seed for repeatable results

shape = ((height // 2) * 2 + 3, (width // 2) * 2 + 3) # total maze dimensions
complexity = int(width + height) # length of wall sections

# Build actual maze
Z = numpy.ones(shape) # maze starts as all 1's or completely transversible

# Fill borders
Z[0, :] = Z[-1, :] = 0 # 0's in maze represent walls
Z[:, 0] = Z[:, -1] = 0

# Making the maze
for i in range(100): # run program a set number of times (use to watch maze grow)
#while sum(sum(Z))>1377: # run program until length of walkable path reached (use to minimise time of creation)
#while time.time()-startTime < runTime: # run program for set time (use first when length unknown)
   pyplot.imshow(Z, cmap=pyplot.cm.gist_gray, interpolation='nearest') # use to watch maze grow
   pyplot.xticks([]), pyplot.yticks([]) # use to watch maze grow
   pyplot.show() # use to watch maze grow
   time.sleep(0.2) # use to watch maze grow
   console.clear() # use to watch maze grow
   x, y = random.randint(0, shape[1] // 2) * 2, random.randint(0, shape[0] // 2) * 2 # pick a random even position as a starting place for a path
   Z[y, x] = 0
   for j in range(complexity):
      neighbours = []
      if x > 1:             neighbours.append((y, x - 2))
      if x < shape[1] - 2:  neighbours.append((y, x + 2))
      if y > 1:             neighbours.append((y - 2, x))
      if y < shape[0] - 2:  neighbours.append((y + 2, x))
      if len(neighbours):
         y_,x_ = neighbours[random.randint(0, len(neighbours) - 1)]
         if Z[y_, x_] == 1:
            Z[y_, x_] = 0
            Z[y_ + (y - y_) // 2, x_ + (x - x_) // 2] = 0
            x, y = x_, y_
print("The total length of the walkable path is ",sum(sum(Z)),".")

# look for dead ends in the maze
dead=[]
inter=[]
path=[]
for m in range(0,width+1):
   for n in range(0, height+1):
      if Z[m,n]==1:
         path.append((m,n))
         near=[]
         if Z[m+1,n]==0:
            near.append((m+1,n))
         if Z[m-1,n]==0:
            near.append((m-1,n))
         if Z[m,n+1]==0:
            near.append((m,n+1))
         if Z[m,n-1]==0:
            near.append((m,n-1))
         if len(near) == 3: # if 3 of the neighbours are walls then it is a dead end
            dead.append((m,n))
            Z[(m,n)]=0.3
         if len(near) == 0: # if 0 of the neighbours are walls then it is an intersection
            inter.append((m,n))
            Z[(m,n)]=0.6

# draw maze
def drawMaze(mazeMap):
   pyplot.imshow(mazeMap, cmap=pyplot.cm.gist_gray, interpolation='nearest')
   pyplot.xticks([]), pyplot.yticks([])
   pyplot.show()

# summary data
print("List of dead ends")
print()
print(dead)
print()
print("There are a total of",len(dead), "dead ends.")
print()
print("List of intersections")
print()
print(inter)
print()
print("There are a total of",len(inter), "intersections.")
print()
print("The starting position is",random.choice(inter))
print()
print("The finishing position is",random.choice(dead))
drawMaze(Z)
