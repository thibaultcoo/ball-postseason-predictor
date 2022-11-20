# will give the equation, as well as various information well put together
# idea is to finalize our project, so that the equation found by the algo is instantly readable
# work in progress

import numpy as np
import ast

# class that will convert our randomly generated nonlinear structure into a readable latex model
class model_convertor:

    def __init__(self, address=None):
        self.address = address

    def nba_model_convertor(self):
        print("Converting the randomly generated model into a readable LaTeX equation...")
        print("\r")

        def indiv_var_convertor(greeks=None, var=None, bs=None):

            # we isolate the specific input variables considered for this transformed nonlinear variable
            input_var_considered = [greeks[i-1] for i in structure[var][0]]

            # we consider the power at which the input variables were elevated
            input_var_powered = []

            for i in range(len(structure[var][1])):
                if str(structure[var][1][i])[0] == "0":
                    input_var_powered += [bs + "sqrt{" + bs + input_var_considered[i - 1] + "}"]
                elif str(structure[var][1][i])[0] == "1":
                    input_var_powered += [bs + input_var_considered[i - 1]]
                else:
                    input_var_powered += [bs + input_var_considered[i - 1] + "^{" + str(structure[var][1][i])[0] + "}"]

            # we finalise the complete variable
            variable_line = input_var_powered[0]

            for rel in range(len(structure[var][2])):
                if structure[var][2][rel] == '/':
                    variable_line = bs + "frac{" + variable_line + "}{" + input_var_powered[rel+1] + "}"
                elif structure[var][2][rel] == '*':
                    variable_line += " " + bs + "cdot " + input_var_powered[rel + 1]
                else:
                    variable_line += " " + structure[var][2][rel] + " " + input_var_powered[rel+1]

            return variable_line

        with open(self.address) as f:
            file = f.readlines()
            structure = ast.literal_eval(file[0])
            constant = float(file[1])
            # params = ast.literal_eval(file[2]) --- still something to fix here
            starting_year = int(file[3])
            ending_year = int(file[4])
            iter = int(file[5])
            time = float(file[6])
            type_stat = ast.literal_eval(file[7])
            rsq = float(file[8])

        nb_input_var = len(type_stat)
        nb_output_var = len(structure)
        greek_letters = ['tau', 'rho', 'varepsilon', 'beta', 'gamma', 'sigma', 'omega', 'mu', 'delta', 'vartheta', 'upsilon', 'kappa', 'nu', 'xi']
        converted_variables = ['var0', 'var1', 'var2']

        # small tweak to write a backslash in python
        bs = str(r'\"')[:1]
        input_var = [greek_letters[i] for i in range(1,nb_input_var)]

        for i in range(3):
            converted_variables[i] = indiv_var_convertor(greeks=input_var, var=i, bs=bs)

        # print("(" + converted_variables[0] + ") + (" + converted_variables[1] + ") + ( " + converted_variables[2] + ")") --- still a work in progress

address = "structure_4e4e14bb1a.txt"
model_convertor(address=address).nba_model_convertor()
