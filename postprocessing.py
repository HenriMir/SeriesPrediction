import matplotlib.pyplot as plt
import numpy as np


def mse(prediction, truth):
    return np.sum((prediction-truth)**2)

def plot_curbs(time_index, prediction, truth):
    fig, ax = plt.subplots()

    ax.plot(time_index, prediction, label="prediction")
    ax.plot(time_index, truth, label="truth")
    ax.set_title("prediction vs truth")
    ax.legend()
    plt.show()