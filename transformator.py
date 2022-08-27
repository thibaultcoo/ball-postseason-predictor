# key part of the code
# we feed raw variables with data -> will transform them

import numpy as np
import pandas as pd
from extractor import data_extractor, data_aggregator

# transforming data that is fed as inputs (work in progress)
class data_transformator:

    def __init__(self, entire_set = None, type_stat = None):
        self.entire_set = entire_set
        self.type_stat = type_stat

    def nba_data_transformator(self):
        whole_x = []
        whole_y = self.entire_set["Overall"]

        nb_stat = np.count_nonzero(self.type_stat)
        for stat in range(nb_stat):
            whole_x.append(self.entire_set[self.type_stat[stat]])

        return whole_x, whole_y