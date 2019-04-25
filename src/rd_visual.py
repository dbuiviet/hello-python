import sys

#sys.path.append('/home/dbuiviet/Workspaces/Python/hello-python/src')
sys.path.insert(0, '/home/dbuiviet/Workspaces/Python/hello-python/src')

import pygal

#Relative import
from roll_die import RollDie

#Create a D6
rd1 = RollDie(6)
rd2 = RollDie(6)

#Make some rolls, store results in a list
results = []
for roll_num in range(1000):
    result = rd1.roll() + rd2.roll()
    results.append(result)

#Analyze the results
frequencies = []
max_result = rd1.num_sides + rd2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#print(results)
print(frequencies)

#Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6+D6', frequencies)
hist.render_to_file('dice_visual.svg')