import numpy as np
import pandas as pd
from extractor import data_extractor, data_aggregator

class model_storer:

    def __init__(self, structure=None, starting_year=None, ending_year=None, iter=None, elapsed_time=None,
                 input_variables=None, score=None, coeffs=None, const=None):
        self.structure = structure
        self.starting_year = starting_year
        self.ending_year = ending_year
        self.iter = iter
        self.elapsed_time = elapsed_time
        self.input_variables = input_variables
        self.score = score
        self.coeffs = coeffs
        self.const = const

    def nba_model_storer(self):
        bool_store = input("Type yes if you would like to save your structure, so as to use it later : ")

        if bool_store == "yes":
            address_list = [np.random.choice(a = ["a", "b", "c", "d", "e", "1", "2", "3", "4", "5"]) for i in range(10)]
            address = "structure_"

            # generating a random name for us to store our structure in
            for i in range(len(address_list)):
                address = address + address_list[i]
            address = address + '.txt'

            with open(address, 'w') as f:
                f.write(str(self.structure))
                f.write('\n')
                f.write(str(self.const))
                f.write('\n')
                f.write(str(self.coeffs))
                f.write('\n')
                f.write(str(self.starting_year))
                f.write('\n')
                f.write(str(self.ending_year))
                f.write('\n')
                f.write(str(self.iter))
                f.write('\n')
                f.write(str(np.round(self.elapsed_time, 2)))
                f.write('\n')
                f.write(str(self.input_variables))
                f.write('\n')
                f.write(str(self.score))

            print('Your structure was successfully stored under the name ' + address)