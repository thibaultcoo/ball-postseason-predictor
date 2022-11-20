# Enhanced power ranking function and basketball postseason brackets prediction through a non-linear regression approach

#### Written by Thibault Collin

*Paper and algorithm produced in September 2022, Beta version*

The aim of our research is to design an algorithm capable of modelling an optimal and non-linear power ranking function for professional teams from the *National Basketball Association* based on their regular season performance, with the final objective being to predict the outcome of the postseason tournament. The algorithm shall be made such that the correct equation be available and usable. To the best of our knowledge, the following techniques used to design the algorithm were not used in the past literature. The power ranking function given by the algorithm is to be found at the end of this paper.

The complete paper will also available inside the repository (last update: 9/17/22)

The code can be used and modified by anyone freely. Download the whole repository and run the main program named `algorithm.py` under your favourite Python IDE. Select the starting and ending year for the data extraction and select your determination coefficient threshold, let the program find the nonlinear structure that fits best your data, and analyze your results at the end.

Save your structure if you are satisfied with the result, it will take the same form as the one proposed in `structure_4e4e14bb1a.txt`. The program also allows you to load an existing structure instead of generating a random one. The file `result-example.txt` details what the algorithm outputs for a randomly generated structure.


Versions for the libraries used (use latest version if not mentionned): Python 3.10
