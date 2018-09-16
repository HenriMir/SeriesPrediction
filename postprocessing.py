import matplotlib.pyplot as plt

def plot_curbs(time_index, prediction, truth):
    fig, ax = plt.subplots()
    print(prediction)
    print(time_index)
    ax.plot(time_index, prediction, label="prediction")
    ax.plot(time_index, truth, label="truth")
    ax.set_title("prediction vs truth")
    ax.legend()
    plt.show()