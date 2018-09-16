class Model:
    def __init__(self, lag):
        self.lag = lag # nb of time steps
        self.output = "Close"
    def train(self, data, set_index=""):
        self.data = data
        if set_index != "":
            self.data = self.data.set_index([set_index])
        self.data = self.data.shift(self.lag)
    
    def predict(self, timestamp):
        """
        return the prediction for the given time index (timestamp)
        """
        return self.data.loc[timestamp,self.output]