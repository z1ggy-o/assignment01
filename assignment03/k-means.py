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
        self.points = []
        self.centroids = []
        self.clusters = []
        for _ in range(k):
            self.clusters.append([])

    def _generatePoints(self):
        randoms = np.random.rand(self.num_points, self.num_dims)
        for x, y in randoms:
            point = [int(x*500), int(y*500)]
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

        return np.linalg.norm(x - y)

    def _computeCentroid(self):
        """ Compute each groups centroid then update self.controids """

        new_centroids = []
        for cluster in self.clusters:
            x_cod = [point[0] for point in cluster]
            y_cod = [point[1] for point in cluster]
            centroid_x = int(sum(x_cod)/len(x_cod))
            centroid_y = int(sum(y_cod)/len(y_cod))
            new_centroids.append([centroid_x, centroid_y])

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
        new_cluster = []
        for _ in range(self.clusters):
            new_clusters.append([])

        for point in self.points:
            min = math.inf
            closest = 0
            # find the closest centroid
            for i in range(len(self.clusters)):
                dist = self._computeDistance(point, self.clusters[i])
                if dist < min:
                    min = dist
                    closest = i
            # put point into new group
            new_clusters[closest].append(point)

        self.clusters = new_clusters

    def getPoints(self):
        return self.points

    def getClusters(self):
        return self.clusters

    def getCentroids(self):
        return self.centroids

    def generatePointCluster(self):
        """Generate random points

        1. Generate random points
        2. Randomly assgin label to each points
        3. Disperse points by cluster one more time

        Parameter:
            k(int): number of clusters
            num_points(int): number of points
            num_dims(int): the dimension of vectors

        Returns:
            2d list: element is the list of points in each cluster
        """

        self._generatePoints()
        self._initialLabel()
        self._dispersePoints()
        self._computeCentroid()

### plot function
def plot_points(cluster):
    """Plot given points

    Parameter:
        points: list of points
    """

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('k-means')
    for x, y in cluster.getPoints():
        plt.scatter(x, y, color='red', marker='o')

    for x, y in cluster.getCentroids():
        plt.scatter(x, y, color='blue', marker='s')

    ax = plt.gca()  # get current axis
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    plt.show()

if __name__ == '__main__':
    kmeans = KMeans(3, 100)
    kmeans.generatePointCluster()
    for i in range(len(kmeans.clusters)):
        print('cluster {}'.format(i + 1))
        for x, y in kmeans.clusters[i]:
            print('point: {}, {}'.format(x, y))
        print('\n')
    
    for point in kmeans.points:
        print(point)

    print('centroids: ')
    print(kmeans.getCentroids())

    plot_points(kmeans)
#################################3




def computeEnergy(data, labels):
    """ Compute the cost of the clustering result

    Return:
        energy(float): the energy of this clustering. 
    """

    # the sum of distance between points and their group represent point.
    pass
