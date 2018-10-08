import numpy as np
from generator import Generator, KerasGenerator


def test_generator():
    x_data = np.array([
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ]).transpose()
    y_data = np.array([
        [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    ]).transpose()
    gen = Generator(x_data=x_data,
                    y_data=y_data,
                    x_num_steps=3,
                    y_num_steps=2,
                    f_step=2,
                    skip_step=3)

    for g in gen.generate():
        print(g)


def test_keras_generator():
    x_data = np.array([
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ]).transpose()
    y_data = np.array([
        [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    ]).transpose()

    gen = KerasGenerator(x_data=x_data,
                         y_data=y_data,
                         x_num_steps=3,
                         y_num_steps=2,
                         f_step=2,
                         skip_step=3,
                         batch_size=2)

    print(len(gen))
    print(gen[0])

test_keras_generator()