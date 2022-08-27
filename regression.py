# class responsible for isolating several statistics that are to be used for tests/regressions

import numpy as np
import pandas as pd
from extractor import data_extractor
import scipy.stats as sci
from sklearn.linear_model import LinearRegression

# the isolator class will take the table as argument and extract the required set of stats (depending on the type of table)
class data_regressor:

    def __init__(self, whole_set_x = None, whole_set_y = None, type_stat = ["W","L","SRS","ORtg","DRtg","NRtg","Pace","FTr","3PAr"]):
        self.whole_set_x = whole_set_x
        self.whole_set_y = whole_set_y
        self.type_stat = type_stat

    def nba_data_regressor(self):
        self.whole_set_y, self.whole_set_x = np.array(self.whole_set_y), np.array(self.whole_set_x)
        self.whole_set_x = np.transpose(self.whole_set_x)

        model = LinearRegression().fit(self.whole_set_x, self.whole_set_y)
        score = model.score(self.whole_set_x, self.whole_set_y)

        return score