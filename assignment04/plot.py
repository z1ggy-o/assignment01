
import numpy as np
import matplotlib.pyplot as plt


def plot(kmeans):

    f = plt.figure(1)

    k = len(kmeans.clusters)
    size = kmeans.data.len_vec

    im_average = np.zeros((size, k), dtype=float)
    im_count = np.zeros(k, dtype=int)

    # plot each cluster's average image
    for i in range(len(kmeans.cluster)):
        for img in kmeans.clusters[i]:
            im_average[:, i] += kmeans.data.list_image[img]

    for i in range(kmeans.clusters):
        im_count[i] = len(kmeans.clusters[i])

    for i in range(kmeans.k):
        im_average[:, i] /= im_count[i]

        plt.subplot(2, 5, i+1)
        plt.title(i)
        plt.imshow(im_average[:, i].reshape((kmeans.size_row, kmeans.size_col)),
                   cmap='Greys', interpolation='None')

        frame = plt.gca()
        frame.axes.get_xaxis().set_visible(False)
        frame.axes.get_yaxis().set_visible(False)

    plt.show()
