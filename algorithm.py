# core of the research
# algorithm that will optimally try as many combinations possible of variables
# we will start easily and then implement gradually more complex features

from extractor import data_extractor, data_aggregator
from regression import data_regressor
from transformator import data_transformator

# general algo (work in progress)
class nba_algorithm:

    def __init__(self, starting_year = 2000, ending_year = 2022, type_stat = ["W","L","ORtg","DRtg","NRtg","Pace","FTr"]):
        self.starting_year = starting_year
        self.ending_year = ending_year
        self.type_stat = type_stat

    def main_nba(self): # for now there is only one iteration, but we will want a loop to isolate the best model from many combinations
        entire_set = data_aggregator(starting_year = self.starting_year, ending_year = self.ending_year).nba_data_aggregator()
        transformed_set = data_transformator(entire_set = entire_set, type_stat = self.type_stat).nba_data_transformator()
        score = data_regressor(whole_set_x = transformed_set[0], whole_set_y = transformed_set[1]).nba_data_regressor()

        return score

print(nba_algorithm().main_nba())