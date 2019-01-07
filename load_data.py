import pandas as pd
import os
import constants as cst


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
        for name in cst.possible_column_names:
            names_dict[name] = name

    loading_path = os.path.join(cst.DATA_PATH, csv_name)
    df = pd.read_csv(loading_path, encoding='utf-8')

    for key in names_dict:
        df = df.rename(index=str, columns={names_dict[key]: key})

    # df = df.set_index(cst.DATE)

    for key in df.keys():
        if key not in cst.possible_column_names:
            print(key)
            raise Exception("column names")

    df[cst.DATE] = pd.to_datetime(df[cst.DATE], yearfirst=True)
    # x = pd.DatetimeIndex(df[cst.DATE]).year
    # print(type(x))
    # print(x)

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


    names_dict={"Date":"Local time"}

    df = load_csv(csv_name="EURCAD_Ticks_05.12.2017-05.12.2017.csv", names_dict=names_dict)
    print(double_date_detected(df))


    print(df.shape)
    print(df.keys())


