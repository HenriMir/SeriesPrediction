import numpy as np
import pandas as pd


"""
script used to compute the data

"""

data_path = "./data/"
date = "Date"
close = "Dernier"
opening = "Ouv."
high = "Haut"
low = "+ Bas"
volume = "Vol."
variation = "Variation %"

data_names = [date, close, opening, high]


def load_range(start_date,
               end_date,
               data_names,
               csv_path=data_path+"BTC_EUR GDAX - Données Historiques .csv"):
    """

    :param start_date: str: "10/09/2018"
    :param end_date: idem
    :param data_names: list de str: ['Date', 'Dernier', 'Ouv.', 'Haut', '
    :return: array numpy de shape (T,n) avec T l'intervalle de temps et n la taille
             de data_names. array de string
    """

    data = pd.read_csv(csv_path, encoding='utf-8').set_index("Date")
    data = data.loc[end_date:start_date]
    data = data[data_names][::-1]  # le -1 pour lire dans l'autre sens sur la date
    return data.values


if __name__ == '__main__':

    data = load_range(start_date="01/09/2018",
                      end_date="10/09/2018",
                      data_names=[opening, close, high, low])

