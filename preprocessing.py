import pandas as pd
import numpy as np
from load_data import load_csv
import constants as cst
import sys

file_path = "./data/bitstampUSD_1-min_data_2012-01-01_to_2018-06-27.csv"


def select_data(dataframe, start=None, stop=None):

    """

    :param dataframe: df pandas
    :param start: str, min date to considerate, format: "YYYY/MM/DD", default value is the min date
    :param stop: str, max date to considerate
    :return: dataframe dans les dates

    :raise null dataframe exception if start and stop leaves a null dataframe

    """

    if start is not None:
        dataframe = dataframe[dataframe[cst.DATE] >= pd.to_datetime(start, format="%Y-%m-%d")]

    if stop is not None:
        dataframe = dataframe[dataframe[cst.DATE] <= pd.to_datetime(stop, format="%Y-%m-%d")]

    if dataframe.shape[0] == 0:
        raise Exception("null dataframe")

    return dataframe


def fill_data(dataframe, step=None):
    """

    fill the dataframe with NaN based on step.

    :param dataframe:
    :param step: str: M, D, H if None, will detect the minimum step in the
    :return:
    """

    raise Exception("TO DO")


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

    names_dict={"Date" : "Local time"}
    data = load_csv(csv_name="EURCAD_Ticks_05.12.2017-05.12.2017.csv", names_dict=names_dict)

    print(data["Date"].head())
    sys.exit(0)
    print(data.shape)
    data = select_data(dataframe=data, start="2017/05/13", stop="2017/05/20")
    print(data.shape)
    print(data["Date"].head())
