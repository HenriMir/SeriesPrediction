import pandas as pd
import numpy as np
from load_data import load_csv
import constants as cst

file_path = "./data/bitstampUSD_1-min_data_2012-01-01_to_2018-06-27.csv"


def select_data(dataframe, start=None, stop=None):

    """

    :param dataframe: df pandas
    :param start: str, min date to considerate, format: "YYYY/MM/DD", default value is the min date
    :param stop: str, max date to considerate
    :return: dataframe dans les dates

    :raise null dataframe exception if start and stop leaves a null dataframe

    """

    # generate an index full of true
    index = ~dataframe[cst.DATE].isnull()
    if start is not None:
        index *= dataframe[cst.DATE] >= pd.to_datetime(start, format="%Y-%m-%d")
    if stop is not None:
        index *= dataframe[cst.DATE] < pd.to_datetime(stop, format="%Y-%m-%d")

    dataframe = dataframe.loc[index, :]

    if dataframe.shape[0] == 0:
        raise Exception("null dataframe")

    return dataframe


def format_time_step(data, step):
    """
    step must be M, D, H, min
    """

    print(data.shape)

    data = data.set_index(cst.DATE)
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



if __name__ == "__main__":
    data = load_csv(csv_name="EUR_USD Historical Data.csv")
    print(data["Date"].head())

    data = select_data(dataframe=data, start=None, stop=None)
    print(data["Date"].head())

    print(data.keys())

    data = format_time_step(data=data, step="D")
    print(data["Date"].head())

