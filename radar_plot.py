from math import pi
import matplotlib.pyplot as plt


def create_radar_chart(data, cluster, categories):
    N = len(categories)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    values = data.loc[cluster].tolist()
    values += values[:1]

    ax = plt.subplot(111, polar=True)
    plt.xticks(angles[:-1], categories, color='grey', size=8)
    ax.plot(angles, values, linewidth=1, linestyle='solid')
    ax.fill(angles, values, 'b', alpha=0.1)
    plt.title(f'Cluster {cluster}')
    plt.show()