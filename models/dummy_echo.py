class Model:
    def __init__(self, lag):
        self.lag = lag
        self.output = 'Close'

    def train(self, data):
        self.data = data

    def predict(self, time_indices):
        result = self.data.shift(self.lag)
        result = result.loc[time_indices, self.output]
        return result