# test file for econometrics/statistics models

import numpy as np
import pandas as pd
from extractor import data_extractor
import scipy.stats as sci # we can also consider statsmodels
from sklearn.linear_model import LinearRegression

# providing data
table = data_extractor(year="2001", step="leagues", type="game", export="yes").nba_data_extractor()
x_two = table["FG"]
y = table["Overall"]
y, x_two = np.array(y), np.array(x_two)
x_two = x_two.reshape((-1, 1))

model = LinearRegression().fit(x_two, y)
score = model.score(x_two, y)
print(model.intercept_)
print(model.coef_)

print(table)