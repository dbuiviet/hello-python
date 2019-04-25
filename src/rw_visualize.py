# import sys

# #sys.path.append('/home/dbuiviet/Workspaces/Python/hello-python/src')
# sys.path.insert(0, '/home/dbuiviet/Workspaces/Python/hello-python/src')

import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    point_num = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_num, cmap=plt.cm.Blues, edgecolors='none', s=1)

    #Emphasize the starting and ending points
    plt.scatter(0,0,c='green',edgecolors='none',s=10)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=10)

    #Remove the axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    #Make another walk?
    keep_running = input("Make another walk?. (y/n): ")
    if keep_running == 'n':
        break