from matplotlib import pyplot as plt

def plot_points(p):
    x = [i[0] for i in p]
    y = [i[1] for i in p]
    plt.scatter(x, y)
    plt.show()


def plot_KP2(p, L, title):
    x = [i[0] for i in p]
    y = [i[1] for i in p]
    plt.scatter(x, y)
    for i in range(len(L)-1):
        plt.plot([L[i][0], L[i+1][0]], [L[i][1], L[i+1][1]], color='r')

    plt.plot([L[-1][0], L[0][0]], [L[-1][1], L[0][1]], color='r')
    plt.title(title)
    plt.show()
