# python libs
from keras.layers import Dense, Input
from keras import models

# project modules
from .tcn import TCN


class Model:
    def __init__(self, timesteps, input_dim, nb_stacks, kernel_size=2, nb_filters=64, dropout_rate=0):
        self.timesteps = timesteps

        i = Input(shape=(timesteps, input_dim))

        o = TCN(i, return_sequences=False, nb_stacks=nb_stacks,
                kernel_size=kernel_size, nb_filters=nb_filters,dropout_rate=dropout_rate)  # regression problem here.
        o = Dense(1)(o)

        self.m = models.Model(inputs=[i], outputs=[o])
        self.m.compile(optimizer='adam', loss='mse')

    def train(self, train_data, test_data):
        self.m.fit(train_data[0], train_data[1], epochs=10,
                   validation_data=(test_data[0], test_data[1]))

    def train_generator(self, train_gen, test_gen, epochs):
        self.m.fit_generator(train_gen, epochs=epochs,
                             validation_data=train_gen)

    def predict(self, data):
        return self.m.predict(data)
