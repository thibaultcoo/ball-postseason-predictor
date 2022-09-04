# core of the research
# algorithm that will optimally try as many combinations of variables
# we will start easily and then implement gradually more complex features

from extractor import data_extractor, data_aggregator
from regression import data_regressor
from transformator import data_transformator
from displayer import model_displayer
import time
import numpy as np

# general algo
class nba_algorithm:

    def __init__(self, starting_year=None, ending_year=None, type_stat=None, threshold=None):
        self.starting_year = starting_year
        self.ending_year = ending_year
        self.type_stat = type_stat
        self.threshold = threshold

    def main_nba(self):
        start_time = time.time()
        score = 0.0
        iter = 0
        void = ""
        entire_set = data_aggregator(starting_year=self.starting_year,ending_year=self.ending_year).nba_data_aggregator()

        while score < self.threshold:
            transformed_set = data_transformator(entire_set = entire_set, type_stat = self.type_stat).nba_data_transformator()
            regression = data_regressor(whole_set_x = transformed_set[0], whole_set_y = transformed_set[1]).nba_data_regressor()
            score = regression[0]
            print("Structure " + str(iter) + " has a score below " + str(self.threshold))
            iter += 1

        elapsed_time = time.time() - start_time

        model_displayer(score=score, nb_variables=len(regression[1]), input_variables=self.type_stat, coeffs=regression[1], const=regression[2],
                        structure=transformed_set[2], starting_year=self.starting_year, ending_year=self.ending_year,
                        iter=iter, elapsed_time=elapsed_time).nba_model_displayer()

        return void

type_stat = ["ORtg","DRtg","FTr","Pace","eFG%","TOV%","ORB%","FT/FGA","advFG%","advTOV%","DRB%","advFT/FGA"]
starting_year = 2000
ending_year = 2022
threshold = 0.60
print(nba_algorithm(type_stat=type_stat, starting_year=starting_year, ending_year=ending_year, threshold=threshold).main_nba())