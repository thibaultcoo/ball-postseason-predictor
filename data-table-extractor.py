# this program allows you to extract any stat table from any year (regular and postseason, from 1980)
# box score and advanced tables (close to fifty statistics)

# required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def nba_data_extractor(year = "2021", step = "playoffs", type = "game", export="no"):

    # select the appropriate table given the wanted table
    if type == "game":
        table = "switcher_per_game_team-opponent"
    elif type == "adv":
        table = "div_advanced-team"

    # we extract the html page given the year and phase of the tournament
    url = "https://www.basketball-reference.com/" + step + "/NBA_" + year + ".html"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, features='html.parser')
    content = soup.find('div', {'id' : table})

    # we isolate the headers
    head = content.find('thead')
    col_raw = [head.text for item in head][0]
    col_clean = col_raw.split()

    # we take into consideration the NBA successive team expansions
    if int(year) > 2004:
        total_teams = 30
    elif 1995 < int(year) < 2005:
        total_teams = 29
    elif 1989 < int(year) < 1996:
        total_teams = 27
    elif 1988 < int(year) < 1990:
        total_teams = 25
    elif 1980 < int(year) < 1989:
        total_teams = 23
    else:
        print("Please select a more recent year")
        quit()

    # we arrange the tables properly
    if table == "div_advanced-team":
        if step == "playoffs":
            col_clean = col_clean[7:29]
            nb_stats = 24
            nb_teams = 16
        else:
            col_clean = col_clean[7:31]
            nb_stats = 26
            nb_teams = total_teams
    else:
        if step == "playoffs":
            nb_teams = 16
        else:
            nb_teams = total_teams
        nb_stats = 24
        col_clean.pop(0)

    col_clean[0] = "Team"
    cont = content.find('tbody')

    indiv_team = []
    total_team = []

    # we fill our stats tables
    for i in range(nb_teams):
        teams = cont.find_all('tr')[i]
        indiv_team = []

        for j in range(nb_stats):
            if step == "leagues" and j == 0:
                indiv_team.append(teams.find_all('a')[0].string)
            elif teams.find_all('td')[j].string != None:
                indiv_team.append(teams.find_all('td')[j].string)

        total_team.append(indiv_team)
    stats = pd.DataFrame(total_team, columns=col_clean)

    # we append the playoff ranking of each team
    url = 'https://www.basketball-reference.com/playoffs/NBA_' + year + '_standings.html'
    page = requests.get(url)

    pagecontent = str(page.content)
    pagecontent = pagecontent.replace('<!--', "")
    pagecontent = pagecontent.replace("-->", "")
    pagecontent = pagecontent.replace("\n", "")
    pagecontent = pagecontent.replace("\\n", "")
    soup = BeautifulSoup(pagecontent, 'html.parser')

    content = soup.find('div', {'id': 'all_expanded_standings'})
    head = content.find('thead')
    body = content.find('tbody')

    col_raw = [head.text for item in head][0]
    col_clean = col_raw.split()[6:8]
    nb_teams = 16

    indiv_team = []
    total_team = []

    # we will want to transform that
    rank = [0, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4]

    for i in range(nb_teams):
        teams = body.find_all('tr')[i]
        indiv_team = []

        indiv_team.append(teams.find_all('td')[0].string)
        indiv_team.append(rank[i])

        total_team.append(indiv_team)

    ranking = pd.DataFrame(total_team, columns=col_clean)
    stats = stats.merge(ranking, how='left')
    stats = stats.replace(np.nan, 5)

    # we export the table
    if export == "yes":
        adress = year + "_" + step + "_" + type + ".csv"
        stats.to_csv(adress, index=False, header=True, sep=';')

    return stats

print(nba_data_extractor(year="2007",step="leagues",type="game",export="yes"))