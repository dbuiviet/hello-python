import matplotlib.pyplot as plt

#input_values = [1, 2, 3, 4, 5]
#squares = [1, 4, 9, 16, 25]

x_values = list(range(1,100))
y_values = [x**2 for x in x_values]

#plt.plot(input_values, squares, linewidth=5)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=20)

#Set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#Set size of tick label
#plt.tick_params(axis='both', labelsize=14)
plt.axis([0, 100, 0, 10000])

plt.show()
plt.savefig('mpl_squares.png', bbox_inches='tight')