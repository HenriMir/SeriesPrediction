import pandas as pd

def read_data(file_path):
    data = pd.read_csv(file_path)
    return data

def select_data(data, start="", stop=""):
    data['date'] = pd.to_datetime(data['Timestamp'],unit="s")

    # generate an index full of true
    index = ~data['date'].isnull()
    if start != "":
        index *= data['date'] >= pd.to_datetime(start,format="%Y-%m-%d")
    if stop != "":
        index *= data['date'] <  pd.to_datetime(stop,format="%Y-%m-%d")
    data = data.loc[index,:]
    return data

def format_time_step(data, step):
    """
    step must be M, D, H, min
    """
    data = data.set_index("date")
    data = data.asfreq(step,method='bfill')
    data = data.reset_index()
    return data