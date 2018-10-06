import numpy as np


class DataSet:
    """Read data from files

    Read image datas from data files.
    Normalize the data then change the data to vector from
    """

    def __init__(self, file="mnist_test.csv"):
        self.size_row = 28  # height of the image data
        self.size_col = 28  # width of the image data
        self.len_vec = self.size_row * self.size_col

        # read data from file
        _handle_file = open(file, 'r')
        _data = _handle_file.readlines()
        _handle_file.close()

        self.num_image = len(_data)
        # test
        # print(self.num_image)

        self.list_image = np.empty((self.len_vec, self.num_image), dtype=float)
        self.list_label = np.empty(self.num_image, dtype=int)

        # change the image datas into vector forms
        _count = 0
        for line in _data:
            line_data = line.split(',')
            label = line_data[0]
            img_vector = np.asfarray(line_data[1:])
            img_vector = self._normalize(img_vector)

            self.list_label[_count] = label
            self.list_image[:, _count] = img_vector  # [:, i] get ith col
            _count += 1

    def _normalize(self, data):
        """Normalize the values of the input data into [0, 1]"""
        data_normalized = (data - min(data)) / (max(data) - min(data))

        return data_normalized
