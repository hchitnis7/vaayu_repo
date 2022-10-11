import matplotlib.pyplot as plt
def plot_chkpts(checkpoints):
    x = [lis[0] for lis in checkpoints]
    y = [i[1] for i in checkpoints]
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.grid()
    plt.plot(x, y, marker="o", markersize=10, markeredgecolor="red", markerfacecolor="black")
    plt.show()


def plot_points(x, y):
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.grid()
    plt.plot(x, y, marker="o", markersize=10, markeredgecolor="red", markerfacecolor="black")
    plt.show()