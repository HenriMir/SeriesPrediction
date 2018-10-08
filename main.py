import numpy as np
import preprocessing
import postprocessing
from generator import KerasGenerator

from models import dummy_echo
from models.conv1D import temporal_conv

FILE_PATH = "data/coinbaseUSD_1-min_data_2014-12-01_to_2018-06-27.csv"
OUTPUT = 'Close'
INPUTS = ['Close']

# open data
data = preprocessing.read_data(FILE_PATH)
# select time scope
data = preprocessing.select_data(data, "2015-01-01","")
# reformat time step, not doing anything if already the right time format (to check)
data = preprocessing.format_time_step(data,"H")

# set timestamp as index
data = data.set_index("Timestamp")
data = data[INPUTS]

# train/test split
train, test = preprocessing.train_test_split(data, 0.7)
train = train[0]
test = test[0]

time_indices = [1420680240,1421120280]
truth = train.loc[time_indices, OUTPUT]

# dummy echo model
model = dummy_echo.Model(1)
model.train(train)
prediction = model.predict([1420680240])

train_gen = KerasGenerator(train[INPUTS].values,train[OUTPUT].values,10,1,10,1,32)
test_gen = KerasGenerator(test[INPUTS].values,test[OUTPUT].values,10,1,10,1,32)

# tcn

model = temporal_conv.Model(timesteps=10,input_dim=1, nb_stacks = 2, dropout_rate=0)
model.train_generator(train_gen, test_gen, 1000)

(pred_data, truth) = test_gen[0]
prediction = model.predict(pred_data)

truth = np.hstack([truth[i,:] for i in range(truth.shape[0])])
prediction = np.hstack([prediction[i,:] for i in range(prediction.shape[0])])

# output prediction vs ground truth
postprocessing.plot_curbs(np.arange(truth.shape[0]), prediction, truth)

# compute mse
#mse = postprocessing.mse(prediction, truth)
#print(mse)