import preprocessing
import postprocessing
from models import dummy_echo

FILE_PATH = "data/coinbaseUSD_1-min_data_2014-12-01_to_2018-06-27.csv"
OUTPUT = 'Close'

# open data
data = preprocessing.read_data(FILE_PATH)
# select time scope
data = preprocessing.select_data(data, "2015-01-01","")
# reformat time step, not doing anything if already the right time format (to check)
data = preprocessing.format_time_step(data,"min")

# set timestamp as index
data = data.set_index("Timestamp")

time_indices = [1420680300,1420680360]
truth = data.loc[time_indices, OUTPUT]

model = dummy_echo.Model(1)
model.train(data)
prediction = model.predict([1420680300,1420680360])

# output prediction vs ground truth
postprocessing.plot_curbs(truth.index, prediction.values, truth.values)