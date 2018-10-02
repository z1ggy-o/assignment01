"""k-means algorithm

k-means algorithm will help clustering datas.

This program will generate the random points, then group them into given k
clusters

TODO:
visualisation:
    - input data
    - initial label
    - initial centroid
    - final label
    - final centroid
    - energy per each iteration

write short descriptions for each graphical result
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
import math


class KMeans:
    """k-means algorithm

    generate random 2d points,
    group these points into k clusters
    """

    def __init__(self, k=3, num_points=100, num_dims=2):
        self.k = k
        self.num_points = num_points
        self.num_dims = num_dims
        self.energy_history = []
        self.points = []
        self.centroids = []
        self.colors = list(cm.rainbow(np.linspace(0, 1, k)))
        self.clusters = []
        for _ in range(k):
            self.clusters.append([])

    def getNumOfClusters(self):
        return self.k

    def getColors(self):
        return self.colors

    def getEnergyHistory(self):
        return self.energy_history

    def getPoints(self):
        return self.points

    def getClusters(self):
        return self.clusters

    def getCentroids(self):
        return self.centroids

    def run(self):
        """Run algorithm

        Repeatly assign labels to points and compute new centroids.
        Iterate until the energy of the result not change.
        """

        energy_prev = 0
        energy_thisTurn = self._computeEnergy()  # initialization result
        while(energy_thisTurn != energy_prev):
            energy_prev = energy_thisTurn
            energy_thisTurn = self._clustering()

    def generatePointCluster(self):
        """Generate random points

        1. Generate random points
        2. Randomly assgin label to each points
        3. Disperse points by cluster one more time
        4. Return the initial energy
        """

        self._generatePoints()
        self._initialLabel()
        self._dispersePoints()
        self._computeCentroid()

    def plotGraph(self):
        """Plot current clustering result"""

        plt.title('k-means')
        plt.xlabel('X')
        plt.ylabel('Y')

        for i in range(len(self.clusters)):
            for x, y in self.clusters[i]:
                plt.scatter(x, y, marker='.', color=self.colors[i])
            x_centroid = self.centroids[i][0]
            y_centroid = self.centroids[i][1]
            plt.scatter(x_centroid, y_centroid, marker='s', color=self.colors[i])
        plt.show()

    def _generatePoints(self):
        randoms = np.random.rand(self.num_points, self.num_dims)
        for x, y in randoms:
            point = [int(x*100), int(y*100)]
            self.points.append(point)

    def _initialLabel(self):
        for i in range(len(self.points)):
            index = i % self.k
            self.clusters[index].append(self.points[i])

    def _dispersePoints(self):
        # move each cluster's point with random offset
        for i in range(self.k):
            x_off = np.random.randint(-50, 50)
            y_off = np.random.randint(-50, 50)
            # x_off = np.random.randint(0, 10)
            # y_off = np.random.randint(0, 10)
            points_moved = []
            for x, y in self.clusters[i]:
                points_moved.append([x+x_off, y+y_off])
            self.clusters[i] = points_moved

        # update result back to points list
        new_points = []
        for i in range(self.k):
            for point in self.clusters[i]:
                new_points.append(point)
        self.points = new_points

    def _computeDistance(self, x, y):
        """Compute the distance between two points

        root of (x1-x2)^2 + (y1-y2)^2
        """

        a = np.array(x)
        b = np.array(y)

        return np.linalg.norm(a - b)

    def _computeCentroid(self):
        """ Compute each groups centroid then update self.controids """

        new_centroids = []
        for cluster in self.clusters:
            x_cod = [point[0] for point in cluster]
            y_cod = [point[1] for point in cluster]
            # there are may some clusters is empty
            # this means sometimes k != #clusters
            try:
                centroid_x = int(sum(x_cod)/len(x_cod))
                centroid_y = int(sum(y_cod)/len(y_cod))
                new_centroids.append([centroid_x, centroid_y])
            except:
                pass

        self.centroids = new_centroids

    def _assignLabel(self):
        """ Assign labels to points for generating new groups

        Compute distance between each point with each centroid,
        assign it to the closest centroid's group.
        """

        # self.points as object
        # for each point, compute the distance, get the closest centroid
        # generate k new cluster
        # no change to self.points and centroid (centroid fixed) 
        new_clusters = []
        for _ in range(len(self.clusters)):
            new_clusters.append([])

        for point in self.points:
            min = math.inf
            closest = 0
            # find the closest centroid
            for i in range(len(self.centroids)):
                dist = self._computeDistance(point, self.centroids[i])
                if dist < min:
                    min = dist
                    closest = i
            # put point into new group
            new_clusters[closest].append(point)

        self.clusters = new_clusters

    def _computeEnergy(self):
        """ Compute the cost of the clustering result

        Return:
            energy(float): the energy of this clustering.
        """

        energy = 0
        for i in range(len(self.centroids)):
            centroid = self.centroids[i]
            part_energy = 0
            for point in self.clusters[i]:
                part_energy += (
                    math.pow(self._computeDistance(point, centroid), 2)
                )
            energy += part_energy
        energy = energy / len(self.points)
        self.energy_history.append(energy)

        return energy

    def _clustering(self):
        """Run algorithm one iteration

        Return:
            energy: This iteration's result energy
        """

        self._assignLabel()
        # After re-grouping if there are any empty cluster, delete it from 
        # list also delete corresponding centroid.
        for i in range(len(self.clusters)):
            if (len(self.clusters[i]) == 0):
                self.clusters.pop(i)
                self.centroids.pop(i)
                self.colors.pop(i)
        self._computeCentroid()
        energy = self._computeEnergy()

        return energy


# plot functions
def plot_p(cluster):
    """Plot given points

    Parameter:
        points: list of points
    """

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('k-means')
    for x, y in cluster.getPoints():
        plt.scatter(x, y, color='red', marker='.')

    for x, y in cluster.getCentroids():
        plt.scatter(x, y, color='blue', marker='s')

    ax = plt.gca()  # get current axis
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    plt.show()


def plotInputData(data):
    """Plot the randomly generated points from KMeans

    Parameter:
        data(list): a list of 2d vectors
    """

    plt.title('Input Data')
    plt.xlabel('X')
    plt.ylabel('Y')

    for x, y in data:
        plt.scatter(x, y, color='black', marker='.')
    plt.show()


def plotEnergy(data):
    """Plot energy history

    Parameter:
        data(list): a list of energy
    """

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')

    plt.title('Energy Variation')
    plt.xlabel('Iteration')
    plt.ylabel(r'$J^{clust}$')
    plt.xticks(range(len(data)+1))

    ite = [i for i in np.arange(1, len(data)+1, 1)]
    plt.plot(ite, data, 'o-', color='b')
    plt.show()


def plotLabel(kmeans):
    """Plot initial clusters"""

    plt.title('Label')
    plt.xlabel('X')
    plt.ylabel('Y')

    for i in range(kmeans.getNumOfClusters()):
        clusters = kmeans.getClusters()
        colors = kmeans.getColors()
        for x, y in clusters[i]:
            plt.scatter(x, y, marker='.', color=colors[i])
    plt.show()


if __name__ == '__main__':
    kmeans = KMeans(3, 100)
    kmeans.generatePointCluster()
    plotInputData(kmeans.getPoints())  # input data
    plotLabel(kmeans)  # initial label
    kmeans.plotGraph()  # initial centroids

    kmeans.run()

    plotLabel(kmeans)  # final label
    kmeans.plotGraph()  # final result
    plotEnergy(kmeans.getEnergyHistory())
