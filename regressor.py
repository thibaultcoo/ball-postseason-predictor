import numpy as np
import pandas as pd
import statsmodels.api as sm
from extractor import data_extractor
import scipy.stats as sci
from sklearn.linear_model import BayesianRidge, LinearRegression # https://scikit-learn.org/stable/modules/linear_model.html#generalized-linear-regression

# performing the necessary regression on a given transformed data set
class data_regressor:

    def __init__(self, whole_set_x = None, whole_set_y = None):
        self.whole_set_x = whole_set_x
        self.whole_set_y = whole_set_y

    def nba_data_regressor(self):
        self.whole_set_y, self.whole_set_x = np.array(self.whole_set_y), np.array(self.whole_set_x)
        self.whole_set_x = np.transpose(self.whole_set_x)

        n_obs = np.shape(self.whole_set_x)[0]
        n_expl = np.shape(self.whole_set_x)[1]

        model_tr = LinearRegression().fit(self.whole_set_x, self.whole_set_y)
        rsq = model_tr.score(self.whole_set_x, self.whole_set_y)
        params = model_tr.coef_
        const = model_tr.intercept_

        def adjusted_rsq(rsq = None, n_obs = None, n_expl = None):
            return 1 - ((1 - rsq) * (n_obs - 1) / (n_obs - n_expl - 1))

        score = adjusted_rsq(rsq = rsq, n_obs = n_obs, n_expl = n_expl)

        return score, params, const