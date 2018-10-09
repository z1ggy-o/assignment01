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

import data_set


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
        self.accuracy_history = []
        self.centroids = []
        self.clusters = [[] for _ in range(k)]
        self.labels = []

    def getEnergyHistory(self):
        return self.energy_history

    def getAccuracyHistory(self):
        return self.accuracy_history

    def initialCluster(self):
        self._initialLabel()
        self._computeCentroid()
        self._computeEnergy()
        self._computeAccuracy()

    def run(self):
        """Run algorithm

        Repeatly assign labels to points and compute new centroids.
        Iterate until the energy of the result not change.
        """

        energy_prev = 0
        energy_this = self.energy_history[0]
        while(energy_this != energy_prev):
            energy_prev = energy_this
            energy_this = self._clustering()
            self._computeAccuracy()

    def _initialLabel(self):
        # for i in range(100):
        for i in range(self.data.num_image):
            index = i % self.k
            self.clusters[index].append(i)

    def _computeCentroid(self):
        """ Compute each groups centroid then update self.controids """

        new_centroids = []
        n = self.data.len_vec

        for cluster in self.clusters:
            centroid = [0] * n
            num_elements = 0

            # sum of the cluster's elements
            for img in cluster:
                num_elements += 1
                for row in range(n):
                    centroid[row] += self.data.list_image[row][img]

            centroid = [row/num_elements for row in centroid]
            new_centroids.append(centroid)

        self.centroids = new_centroids

    def _clustering(self):
        """Run algorithm one iteration

        Return:
            energy: This iteration's result energy
        """

        self._assignLabel()
        # After re-grouping if there are any empty cluster, delete it from list
        self.clusters = [list for list in self.clusters if list]
        self._computeCentroid()

        return self._computeEnergy()

    def _assignLabel(self):
        """ Assign labels to elemetns for generating new groups

        Compute distance between each element with each centroid,
        assign it to the closest centroid's group.
        """

        # for each element, compute the distance, get the closest centroid
        # generate k new cluster
        new_clusters = [[] for _ in range(len(self.clusters))]

        for index in range(self.data.num_image):
            min = math.inf
            closest = 0
            # find the closest centroid
            for j in range(len(self.centroids)):
                dist = self._computeDistance(
                    x=self.data.list_image[:, index], y=self.centroids[j])
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
        x = np.array(x)
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
            centroid = self.centroids[i]
            part_energy = 0
            for index in self.clusters[i]:
                part_energy += self._computeDistance(
                    x=self.data.list_image[:, index], y=centroid)
            energy += part_energy
        energy = energy / self.data.num_image
        self.energy_history.append(energy)

        return energy

    def _computeAccuracy(self):
        """Compute the arrcuracy of the result

        In each group, let the largest number of elements to be the group label.
        """

        accuracy = 0
        labels_clusters = []

        for cluster in self.clusters:
            labels = []

            # get all the labels in the cluster
            for index in cluster:
                labels.append(self.data.list_label[index])

            # get the largest number of lable, count the occurences
            labels.sort()
            count = 0
            count_max = 0
            label_prev = -1
            label_max = -1
            for label in labels:
                if label == label_prev:
                    count += 1
                else:
                    if count > count_max:
                        count_max = count
                        label_max = label_prev
                    label_prev = label
                    count = 1
            # check the last item
            if count > count_max:
                count_max = count
                label_max = label_prev

            labels_clusters.append(label_max)
            accuracy_part = count_max / len(cluster)
            accuracy += accuracy_part

        accuracy = accuracy / len(self.clusters)
        self.labels = labels_clusters
        self.accuracy_history.append(accuracy)


def plotImages(kmeans):
    """Plot the graph of clusters average value"""
    k = len(kmeans.clusters)
    size = kmeans.data.len_vec

    im_average = np.zeros((size, k), dtype=float)
    im_count = np.zeros(k, dtype=int)

    # add each cluster's image value together
    for i in range(k):
        for img in kmeans.clusters[i]:
            im_average[:, i] += kmeans.data.list_image[:, img]

    # count number of each cluster's elements
    for i in range(k):
        im_count[i] = len(kmeans.clusters[i])

    for i in range(k):
        im_average[:, i] /= im_count[i]

        plt.subplot(2, 5, i+1)
        plt.title(kmeans.labels[i])
        plt.imshow(im_average[:, i].reshape(
                                            (kmeans.data.size_row,
                                             kmeans.data.size_col)),
                   cmap='Greys', interpolation='None')

        frame = plt.gca()
        frame.axes.get_xaxis().set_visible(False)
        frame.axes.get_yaxis().set_visible(False)

    plt.show()

if __name__ == '__main__':
    data = data_set.DataSet()
    kmeans = KMeans(data, 10)
    kmeans.initialCluster()
    plotImages(kmeans)

    kmeans.run()
    print('After')
    print('energy histoty:')
    print(kmeans.getEnergyHistory())
    print('\naccuracy history: ')
    print(kmeans.getAccuracyHistory())
    plotImages(kmeans)
