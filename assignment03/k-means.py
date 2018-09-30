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


class KMeans:
    """k-means algorithm

    generate random 2d points,
    group these points into k clusters
    """

    def __init__(self, k=3):
        self.k = k
        self.centroids = []
        self.clusters = []
        for _ in range(k):
            centroid = [[0, 0], []]
            self.clusters.append(centroid)

    def _generatePoints(self, num_points=100, num_dims=2):
        randoms = np.random.rand(num_points, num_dims)
        self.points = []
        for x, y in randoms:
            point = [int(x*100), int(y*100)]
            self.points.append(point)

    # def _initialLabels(self):
    #         self.clusters.append([0, 0])

    def assignLabel(self):
        for i in range(len(self.points)):
            index = i % self.k
            self.clusters[index][1].append(self.points[i])

    def generatePointCluster(self, num_points):
        """Generate random points

        1. Generate random points
        2. Randomly assgin label to each points
        3. Disperse points by cluster one more time

        Parameter:
            k(int): number of clusters
            num_points(int): number of points

        Returns:
            2d list: element is the list of points in each cluster
        """
        pass


if __name__ == '__main__':
    kmeans = KMeans()
    kmeans._generatePoints()
    kmeans.assignLabel()
    for i in range(len(kmeans.clusters)):
        print('cluster {}'.format(i + 1))
        for x, y in kmeans.clusters[i][1]:
            print('point: {}, {}'.format(x, y))
        print('\n')


def computeDistance(x, y):
    """Compute the distance between two points

    root of (x1-x2)^2 + (y1-y2)^2
    """

    return np.linalg.norm(x - y)




def computeCentroid(k):
    """ Compute this group's represent point """

    # compute the mean of points
    pass


def assignLabel(k, distances):
    """ Assign labels to points for generating new groups """

    # depends on distance, assign closest represent's label to each point
    pass


def computeEnergy(data, labels):
    """ Compute the cost of the clustering result"""

    # the sum of distance between points and their group represent point.
    pass
