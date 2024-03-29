import numpy as np
import pandas as pd
from extractor import data_extractor, data_aggregator

# transforming data, from raw extracted variables to nonlinear combinaisons of these raw variables
class data_transformator:

    def __init__(self, entire_set=None, type_stat=None, new_structure=None):
        self.entire_set = entire_set
        self.type_stat = type_stat
        self.new_structure = new_structure

    # we want to randomly generate a variable
    def variable_generator(self, whole_x=None, nb_stat=None, existing_structure=None):
        # gives the total pool of variables
        list_var = [i for i in range(1, nb_stat + 1)]

        # randomly select variables to use in the one transformed variable
        binary_var = [np.random.randint(0, 2) for i in range(nb_stat)]

        # gives the final selection of variables
        considered_var = [list_var[i] for i in range(nb_stat) if binary_var[i] != 0]

        # we isolate the case where we have no variable to consider (very simple bypass)
        if len(considered_var) == 0:
            considered_var = [np.random.randint(1, nb_stat + 1)]

        # gives the power of each variable
        self_rel = [np.random.choice(a = [0.5, 1.0, 2.0, 3.0, 4.0], p = [0.2, 0.4, 0.2, 0.1, 0.1]) for i in range(len(considered_var))]

        # gives the operations between each variable
        other_rel = [np.random.choice(a = ["+", "-", "*", "/"], p = [0.15, 0.15, 0.4, 0.3]) for i in range(len(considered_var) - 1)]

        # in the case where we do not want to generate a new structure, but rather test an existing one
        if self.new_structure != None:
            considered_var = existing_structure[0]
            self_rel = existing_structure[1]
            other_rel = existing_structure[2]

        generated_variable = pd.Series(whole_x[considered_var[0] - 1].astype(float, errors = 'raise')) ** self_rel[0]

        for i in range(1, len(considered_var)):
            temp_var = pd.Series(whole_x[considered_var[i] - 1].astype(float, errors = 'raise')) ** self_rel[i]

            if other_rel[i - 1] == "+":
                generated_variable = generated_variable + temp_var
            elif other_rel[i - 1] == "-":
                generated_variable = generated_variable - temp_var
            elif other_rel[i - 1] == "*":
                generated_variable = generated_variable * temp_var
            elif other_rel[i - 1] == "/":
                generated_variable = generated_variable / temp_var

        variable_structure = []
        variable_structure.append(considered_var)
        variable_structure.append(self_rel)
        variable_structure.append(other_rel)

        return generated_variable, variable_structure

    # we want to randomly generate a structure comprising the given data-set
    def structure_generator(self, whole_x=None, nb_stat=None):
        # gives the random number of new variables
        nb_transformed_var = np.random.randint(1, 4)
        transformed_x = []
        structure_x = []
        existing_structure = [None, None, None]

        # in the case where we do not want to generate a new structure, but rather test an existing one
        if self.new_structure != None:
            existing_structure = self.new_structure
            nb_transformed_var = len(existing_structure)

        for i in range(nb_transformed_var):
            random_var = data_transformator.variable_generator(self, whole_x = whole_x, nb_stat = nb_stat, existing_structure = existing_structure[i])
            transformed_x.append(random_var[0])
            structure_x.append(random_var[1])

        return transformed_x, structure_x

    def nba_data_transformator(self):
        whole_x = []
        whole_y = self.entire_set["Overall"]
        nb_stat = np.count_nonzero(self.type_stat)

        for stat in range(nb_stat):
            whole_x.append(self.entire_set[self.type_stat[stat]])

        random_structure = data_transformator.structure_generator(self, whole_x = whole_x, nb_stat = nb_stat)
        variable = random_structure[0]
        structure = random_structure[1]

        return variable, whole_y, structure