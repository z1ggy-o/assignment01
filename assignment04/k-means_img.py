"""k-means algorithm

k-means algorithm will help clustering datas.

This program will generate the random points, then group them into given k
clusters

TODO:
    try varying k
    compute the accuracy with k=10

    visualization:
        initial centroid images
        final centroid images
        energy per each iteration
        accuracy per each iteration
"""
import math

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm

import DataSet


class KMeans:
    """k-means algorithm for images

    Clustring the image datas into k groups.
    Compute each iteration's energy.
    End of the algorithm, compute the accuracy. 
    """

    def __init__(self, data, k=10):
        self.k = k
        self.data = data
        self.energy_history = []
        self.centroids = []
        self.clusters = [[]] * k  # store image's index in list_image
        self.accuracy_history = []

    def initialCluster(self):
        self._initialLabel()
        self._computeCentroid()

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

    def computeAccuracy(self):
        pass

    def _initialLabel(self):
        for i in range(self.data.num_image):
            index = i % self.k
            self.clusters[index].append(i)

    def _computeCentroid(self):
        """ Compute each groups centroid then update self.controids """

        new_centroids = []
        n = self.data.len_vec

        for cluster in self.clusters:
            centroid = [[0]] * n
            num_elements = 0

            # sum of the cluster's elements
            for index in cluster:
                num_elements += 1
                for i in n:
                    centroid[i] += self.data.list_image[index][i]

            # new_list = [expression(i) for i in old_list if filter(i)]
            centroid = [row/num_elements for row in centroid]
            new_centroids.append(centroid)

        self.centroids = new_centroids

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
        self._computeCentroid()

        return self._computeEnergy()

    def _assignLabel(self):
        """ Assign labels to elemetns for generating new groups

        Compute distance between each element with each centroid,
        assign it to the closest centroid's group.
        """

        # for each element, compute the distance, get the closest centroid
        # generate k new cluster
        new_clusters = [[]] * len(self.clusters)

        for index in range(self.data.num_image):
            min = math.inf
            closest = 0
            # find the closest centroid
            for j in range(len(self.centroids)):
                dist = self._computeDistance(
                    x=self.data.list_image[index], y=self.centroids[j])
                if dist < min:
                    min = dist
                    closest = j
            # put point into new group
            new_clusters[closest].append(index)

        self.clusters = new_clusters

    def _computeDistance(self, x, y):
        """Compute the distance between two points

        (x1-x2)^2 + (y1-y2)^2
        """

        # convert python list to np.array
        y = np.array(y)

        d = (x - y)**2
        s = np.sum(d)

        return s

    def _computeEnergy(self):
        """ Compute the cost of the clustering result

        Return:
            energy(float): the energy of this clustering.
        """

        energy = 0
        for i in range(len(self.centroids)):
            centroid = np.array(self.centroids[i])
            part_energy = 0
            for index in self.clusters[i]:
                part_energy += self._computeDistance(
                    x=self.data.list_image[index], y=centroid)
            energy += part_energy
        energy = energy / self.data.num_image
        self.energy_history.append(energy)

        return energy

    def _computeAccuracy(self):
        """Compute the arrcuracy of the result

        In each group, let the largest number of elements to be the group label.
        """

        # for each cluster
        # find the most numerous elements.
        # compute each cluster's accuracy
        # compute the average accuracy value
        for cluster in self.clusters:
