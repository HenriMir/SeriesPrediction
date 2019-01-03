import pandas as pd
import os
import constants as cst

data_path = "./data/"
date = "Date"
close = "Dernier"
opening = "Ouv."
high = "Haut"
low = "+ Bas"
volume = "Vol."
variation = "Variation %"

data_names = [date, close, opening, high]


def load_csv(csv_name, names_dict=None):
    """
    load the csv in data and set the index on the date
    :param csv_name: str
    :param names_dict: dictionnaire de clés: Date, Price, Open, High, Low et Change avec en valeur
                        le nom de la variable associee
    :return: pandas df with column names: Date, Price, Open, High, Low et Change

    """

    if names_dict is None:
        names_dict = {}
        names_dict[cst.DATE] = cst.DATE
        names_dict[cst.PRICE] = cst.PRICE
        names_dict[cst.OPEN] = cst.HIGH
        names_dict[cst.LOW] = cst.LOW
        names_dict[cst.CHANGE] = cst.CHANGE

    loading_path = os.path.join(cst.DATA_PATH, csv_name)
    df = pd.read_csv(loading_path, encoding='utf-8')

    for key in names_dict:
        df.rename(index=str, columns={names_dict[key]: key})

    #df = df.set_index(cst.DATE)

    return df


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
    return data


if __name__ == '__main__':

    df = load_csv(csv_name="EUR_USD Historical Data.csv")
    print(df.keys())
    print(df["Date"].head())