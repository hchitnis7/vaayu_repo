from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
x = [0]
y = [3]
plt.xlim(0, 200)
plt.ylim(0, 50)
plt.grid()
plt.plot(x, y, marker="o", markersize=10, markeredgecolor="red", markerfacecolor="black")
plt.show()