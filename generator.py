import numpy as np
import keras


class Generator(object):
    """
    Generates data from x,y data into (num_steps, dimension) generator
    """

    def __init__(self, x_data, y_data, x_num_steps, y_num_steps, f_step, skip_step):
        self.x_data = x_data
        self.y_data = y_data
        self.x_dim = self.x_data.shape[1]
        self.y_dim = self.y_data.shape[1]

        self.skip_step = skip_step
        self.f_step = f_step
        self.x_num_steps = x_num_steps
        self.y_num_steps = y_num_steps

        self.num_batch = (len(y_data)-y_num_steps -
                          self.f_step) // self.skip_step
        print(self.num_batch)
        # this will track the progress of the batches sequentially through the
        # data set - once the data reaches the end of the data set it will reset
        # back to zero
        self.current_idx = 0
        # skip_step is the number of words which will be skipped before the next
        # batch is skimmed from the data set
        self.skip_step = skip_step

    def generate(self):
        x = np.zeros((self.num_batch, self.x_num_steps, self.x_dim))
        y = np.zeros((self.num_batch, self.y_num_steps, self.y_dim))

        for i in range(self.num_batch):
            if self.current_idx + self.y_num_steps + self.f_step > len(self.y_data):
                # reset the index back to the start of the data set
                self.current_idx = 0
            x[i, :, :] = self.x_data[self.current_idx:self.current_idx +
                                     self.x_num_steps, :]
            y[i, :, :] = self.y_data[self.current_idx + self.f_step:self.current_idx +
                                     self.y_num_steps + self.f_step, :]
            self.current_idx += self.skip_step
        yield x, y


class KerasGenerator(keras.utils.Sequence):
    """
    Generates data from x,y data into (batch_size, num_steps, dimension) generator
    """

    def __init__(self, x_data, y_data, x_num_steps, y_num_steps, f_step, skip_step, batch_size):
        """
        initialize the generator
        x_data (numpy.ndarray): input data of shape (x_len,x_dim)
        y_data (numpy.ndarray): target data of shape (y_len,y_dim)
        x_num_steps (int) size of the window for x
        y_num_steps (int) size of the window for y
        f_step (int) nb of step to shift for the prediction
        skip_step (int) nb of step to skip for the next step
        batch_size (int) nb of windows in one batch

        for example :   gen = KerasGenerator(x_data=x_data,
                         y_data=y_data,
                         x_num_steps=3,
                         y_num_steps=1,
                         f_step=2,
                         skip_step=3,
                         batch_size=2)
        Create a generator with a window of size 3 as inputs and a window of size 1 as output.
        """
        if len(x_data.shape) == 1:
            x_data = x_data[:, np.newaxis]
        (self.x_len, self.x_dim) = x_data.shape

        if len(y_data.shape) == 1:
            y_data = y_data[:, np.newaxis]
        (self.y_len, self.y_dim) = y_data.shape

        self.x_data = x_data
        self.y_data = y_data

        self.x_num_steps = x_num_steps
        self.y_num_steps = y_num_steps
        self.batch_size = batch_size

        self.current_idx = 0
        self.skip_step = skip_step
        self.f_step = f_step

    def __len__(self):
        'Denotes the number of batches per epoch'
        return (len(self.y_data)-self.y_num_steps-self.f_step) // (self.skip_step*self.batch_size)

    def __getitem__(self, index):
        'Generate one batch of data'
        # Generate indexes of the batch

        X, y = self.__data_generation(index)
        return X, y

    def __data_generation(self, index):
        X = np.zeros((self.batch_size, self.x_num_steps, self.x_dim))
        y = np.zeros((self.batch_size, self.y_num_steps))

        for i in range(self.batch_size):
            current_idx = index * self.batch_size + self.skip_step * i
            X[i, :, :] = self.x_data[current_idx:current_idx+self.x_num_steps, :]
            y[i, :] = self.y_data[current_idx +
                                  self.f_step:current_idx+self.y_num_steps+self.f_step]

        return X, y
