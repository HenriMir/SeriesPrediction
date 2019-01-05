import pandas as pd
import numpy as np
from load_data import load_csv


file_path = "./data/bitstampUSD_1-min_data_2012-01-01_to_2018-06-27.csv"


def read_data(file_path):
    data = pd.read_csv(file_path)
    return data


def select_data(data, start="", stop=""):
    data['date'] = pd.to_datetime(data['Timestamp'], unit="s")

    # generate an index full of true
    index = ~data['date'].isnull()
    if start != "":
        index *= data['date'] >= pd.to_datetime(start, format="%Y-%m-%d")
    if stop != "":
        index *= data['date'] < pd.to_datetime(stop, format="%Y-%m-%d")
    data = data.loc[index, :]
    return data


def format_time_step(data, step):
    """
    step must be M, D, H, min
    """
    data = data.set_index("date")
    data = data.asfreq(step, method='bfill')
    data = data.reset_index()
    return data

def train_test_split(data, train_ratio, method=0):
    train = []
    test = []

    if method == 0:
        n_rows = int(train_ratio * len(data))
        train.append(data.iloc[:n_rows,:])
        test.append(data.iloc[n_rows:,:])
    
    return train,test

def convert2array(data, values):

    """

    :param data: panda dataframe, output de format_time_step
    :param values: list de str: ['date', 'Timestamp', 'Open', 'High', 'Low',
                   'Close', 'Volume_(BTC)', 'Volume_(Currency)', 'Weighted_Price']
    :return: np.array, de shape (T,k) T le timestep de data, et k = len(values), dans
             le même ordre
    """
    if "date" in values:
        raise Exception("date format not supported by numpy array")
    
    possible_values = ['date', 'Timestamp', 'Open', 'High', 'Low',
                       'Close', 'Volume_(BTC)', 'Volume_(Currency)', 'Weighted_Price']
    index_to_extract = []
    for value in values:
        if value in possible_values:
            index_to_extract.append(possible_values.index(value))
        else:
            raise Exception("value: ", value, "not in: ", possible_values)

    data = data.values
    time_range = len(data)
    data = np.split(data, indices_or_sections=len(possible_values), axis=1)
    extracted_data = np.zeros((len(values), time_range))
    for i, index in enumerate(index_to_extract):
        extracted_data[i] = np.reshape(data[index], (time_range))

    return np.rollaxis(extracted_data, 0, 1)


if __name__ == "__main__":
    data = load_csv(csv_name="EUR_USD Historical Data.csv")
    data = select_data(data=data, start="2016/08/10", stop="2016/08/11")
    data = format_time_step(data=data, step="H")

    data = convert2array(data=data, values=["High", "Weighted_Price"])
    print(data.shape)
