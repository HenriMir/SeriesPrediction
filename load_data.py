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
    load the csv in data
    date format of the output is YYYY-MM-DD
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

    print(df.keys())
    df[cst.DATE] = pd.to_datetime(df[cst.DATE], yearfirst=True)

    return df



if __name__ == '__main__':

    names_dict = {}
    names_dict["Date"] = "2018.01.01"
    names_dict["Hour"] = "2018.01.01"

    df = load_csv(csv_name="DAT_MT_EURUSD_M1_201801.csv")




    print(df.shape)
    print(df.keys())


