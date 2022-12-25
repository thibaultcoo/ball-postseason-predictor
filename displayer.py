import os
import numpy as np

# displaying nicely all the final results
class model_displayer:

    def __init__(self, score=None, nb_variables=None, input_variables=None, coeffs=None, const=None, structure=None, \
                 starting_year=None, ending_year=None, iter=None, elapsed_time=None):
        self.score = score
        self.nb_variables = nb_variables
        self.input_variables = input_variables
        self.coeffs = coeffs
        self.const = const
        self.structure = structure
        self.starting_year = starting_year
        self.ending_year = ending_year
        self.iter = iter
        self.elapsed_time = elapsed_time

    def nba_model_displayer(self):
        os.system('cls')
        print("\n" * 100)
        print("The following non-linear structure is supposedly best able to predict the NBA postseason:")
        print("Considering a set of data going from " + str(self.starting_year) + " to " + str(self.ending_year))
        print("Number of iterations required to obtain the result : " + str(self.iter))
        print("Elapsed time (in seconds) : " + str(np.round(self.elapsed_time, 2)))
        print("With a coefficient of determination = " + str(np.round(self.score, 4)))
        print("\n")
        print("Our model is composed of " + str(self.nb_variables) + " variable(s), which were (was) built as nonlinear combinaison(s) of our input variables")
        print("Our input variables were the following : " + str(self.input_variables))
        print("\n")
        print("With a constant coefficient of : " + str(np.round(self.const,5)))

        for var in range(self.nb_variables):
            print("\n")
            print("Variable " + str(var + 1) + " (multiplying coefficient of " + str(np.round(self.coeffs[var], 5)) + ") :")
            var_list = [self.input_variables[self.structure[var][0][u] - 1] for u in range(len(self.structure[var][0]))]
            print("Randomly considered subset of variables : " + str(var_list))

            print("Randomly considered power operations on each variable : " + str(self.structure[var][1]))
            print("Randomly considered operations between those variables : " + str(self.structure[var][2]))

        print("\n")