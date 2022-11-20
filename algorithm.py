from extractor import data_extractor, data_aggregator
from regressor import data_regressor
from transformator import data_transformator
from displayer import model_displayer
from predictor import model_predictor
from storer import model_storer
import time
import ast
import numpy as np

# algorithm that will optimally try as many combinations of variables as possible, until the threshold is reached
class nba_algorithm:

    def __init__(self, starting_year=None, ending_year=None, testing_year=None, type_stat=None, threshold=None, new_structure="yes"):
        self.starting_year = starting_year
        self.ending_year = ending_year
        self.testing_year = testing_year
        self.type_stat = type_stat
        self.threshold = threshold
        self.new_structure = new_structure

    def main_nba(self):
        start_time = time.time()
        structure = None
        score = 0.0
        iter = 0
        void = ""

        if self.new_structure == "no":
            address = input("What is the complete file name of the structure chosen : ")
            with open(address) as f:
                file = f.readlines()
                self.threshold = 0.01
                structure = ast.literal_eval(file[0])
                self.starting_year = int(file[3])
                self.ending_year = int(file[4])
                self.type_stat = ast.literal_eval(file[7])

        print("Fetching data from " + str(self.starting_year) + " to " + str(self.ending_year))
        entire_set = data_aggregator(starting_year=self.starting_year, ending_year=self.ending_year).nba_data_aggregator()

        while score < self.threshold:
            transformed_set = data_transformator(entire_set = entire_set, type_stat = self.type_stat, new_structure = structure).nba_data_transformator()
            regression = data_regressor(whole_set_x = transformed_set[0], whole_set_y = transformed_set[1]).nba_data_regressor()
            score = regression[0]
            print("Structure " + str(iter) + " has a score below " + str(self.threshold))
            iter += 1

        elapsed_time = time.time() - start_time

        if self.new_structure == "no":
            iter = int(file[3])
            elapsed_time = float(file[4])

        model_displayer(score=score, nb_variables=len(regression[1]), input_variables=self.type_stat, coeffs=regression[1], const=regression[2],
                        structure=transformed_set[2], starting_year=self.starting_year, ending_year=self.ending_year,
                        iter=iter, elapsed_time=elapsed_time).nba_model_displayer()

        model_predictor(chosen_year=self.testing_year, nb_variables=len(regression[1]), input_variables=self.type_stat, coeffs=regression[1], const=regression[2],
                        structure=transformed_set[2]).nba_model_predictor()

        model_storer(structure=transformed_set[2], starting_year=self.starting_year, ending_year=self.ending_year, iter=iter, elapsed_time=elapsed_time,
                     input_variables=self.type_stat, score=score, coeffs=regression[1], const=regression[2]).nba_model_storer()

        return void

type_stat = ["ORtg","DRtg","FTr","Pace","eFG%","TOV%","ORB%","FT/FGA","advFG%","advTOV%","DRB%","advFT/FGA"]
starting_year = 2021
ending_year = 2021
testing_year = 2022
threshold = 0.50
new_structure = "yes"

result = nba_algorithm(type_stat=type_stat, starting_year=starting_year, ending_year=ending_year, testing_year=testing_year, threshold=threshold, new_structure=new_structure).main_nba()
print(result)