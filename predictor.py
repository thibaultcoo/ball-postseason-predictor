import numpy as np
import pandas as pd
from extractor import data_extractor, data_aggregator

class model_predictor:

    def __init__(self, chosen_year=None, nb_variables=None, input_variables=None, coeffs=None, const=None, structure=None):
        self.chosen_year = chosen_year
        self.nb_variables = nb_variables
        self.input_variables = input_variables
        self.coeffs = coeffs
        self.const = const
        self.structure = structure

    def nba_model_predictor(self):
        print("Here is the power ranking for the year " + str(self.chosen_year) + " based on the previously generated function : \n")

        # extracts the data of a given year (initial input by the user)
        test_set = data_aggregator(starting_year=self.chosen_year, ending_year=self.chosen_year).nba_data_aggregator()
        final_set = pd.Series(test_set['Team'])

        # for each transformed variable -> computes the value for each team
        for var in range(self.nb_variables):
            generated_variable = pd.Series(test_set[self.input_variables[self.structure[var][0][0] - 1]].astype(float, errors='raise')) ** self.structure[var][1][0]

            for i in range(1, len(self.structure[var][0])):
                temp_var = pd.Series(test_set[self.input_variables[self.structure[var][0][i] - 1]].astype(float, errors='raise')) ** self.structure[var][1][i]

                if self.structure[var][2][i - 1] == "+":
                    generated_variable = generated_variable + temp_var
                elif self.structure[var][2][i - 1] == "-":
                    generated_variable = generated_variable - temp_var
                elif self.structure[var][2][i - 1] == "*":
                    generated_variable = generated_variable * temp_var
                elif self.structure[var][2][i - 1] == "/":
                    generated_variable = generated_variable / temp_var

            final_set = pd.concat([final_set, generated_variable], axis=1)

        # then taking the coefficients given by the regression -> aggregates all variables for all teams
        set = final_set.iloc[:, 1] * self.coeffs[0]

        if self.nb_variables != 1:
            for var in range(1, self.nb_variables):
                temp_set = final_set.iloc[:, 1] * self.coeffs[var]
                set = set + temp_set

        set = set + self.const

        set = pd.concat([final_set.iloc[:, 0], set], axis=1)
        set.columns = ['Team', 'Power ranking']
        sum_col = set.iloc[:, 1].sum()

        # ranks the teams
        set['Power ranking'] = set['Power ranking'].div(sum_col)
        set = set.sort_values(by=['Power ranking'], ascending=True)
        print(set)
        print('\n')