import pandas as pd
import os
import constants as cst


def load_csv(csv_name, names_dict=None):
    """
    load the csv in data
    date format of the output is YYYY-MM-DD
    :param csv_name: str
    :param names_dict: dictionnaire de clés: Date, Price, Open, High, Low et Change avec en valeur
                        le nom de la variable associee. Ses clés doivent etre les noms voulues des colonnes
                        et les valeurs, les noms actuels
                        ex:     names_dict = {cst.CLOSE: 'EUR/USD Close',
                                              cst.HIGH: 'EUR/USD High',
                                              cst.LOW: 'EUR/USD Low'}

    :return: pandas df with column names: Date, Price, Open, High, Low et Change

    """

    if names_dict is None:
        names_dict = {}
        for name in cst.possible_column_names:
            names_dict[name] = name

    loading_path = os.path.join(cst.DATA_PATH, csv_name)
    df = pd.read_csv(loading_path, encoding='utf-8')

    for key in names_dict:
        print(names_dict[key], key)
        df = df.rename(index=str, columns={names_dict[key]: key})

    # df = df.set_index(cst.DATE)

    for key in df.keys():
        if key not in cst.possible_column_names:
            print(key)
            print(df.keys())
            raise Exception("column names")

    df[cst.DATE] = pd.to_datetime(df[cst.DATE], yearfirst=True)

    df[cst.YEAR] = df[cst.DATE].apply(lambda x: x.year).astype(str)
    df[cst.MONTH] = df[cst.DATE].apply(lambda x: x.month).astype(str)
    df[cst.DAY] = df[cst.DATE].apply(lambda x: x.day).astype(str)

    return df


def double_date_detected(df):

    """
    take the df output of load_csv and return True if a double date has been detected, False otherwise
    :param df:
    :return:
    """

    df_date = df[cst.DATE]
    n_rows = df_date.shape[0]
    df_date = df_date.drop_duplicates()
    n_rows_without_duplicate = df_date.shape[0]

    return n_rows != n_rows_without_duplicate


if __name__ == '__main__':

    names_dict = { cst.CLOSE: 'EUR/USD Close',
                  cst.HIGH: 'EUR/USD High',
                  cst.LOW: 'EUR/USD Low'}

    df = load_csv(csv_name="EURUSD_20180101_20190101_D.csv", names_dict=names_dict)
    print(double_date_detected(df))


    print(df.shape)
    print(df.keys())
    print(df.head(50))

