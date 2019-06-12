# Total number of extra runs, noball runs, legbye runs given by each team per year.

import csv
from collections import Counter
from collections import defaultdict
import numpy as np
from matplotlib import pyplot as plt
def function_1(year):
    id_ipl=[]
    extra_run={}
    team_ipl=[]
    with open ('deliveries.csv') as delivery:
        with open('matches.csv') as matches:
            delivery_dir=csv.DictReader(delivery)
            delivery_list=list(delivery_dir)
            matches_dir=csv.DictReader(matches)

            for i in matches_dir:
                if i['season']==year:
                    id_ipl.append(i['id'])

            print(list(id_ipl))

            for i in delivery_list:
                try:
                    if i["match_id"] in id_ipl:
                        extra_run.setdefault(i['batting_team'], [0, 0, 0])
                        extra_run[i['batting_team']][0] = extra_run[i['batting_team']][0] + int(i['extra_runs'])
                        extra_run[i['batting_team']][1] = extra_run[i['batting_team']][1] + int(i['noball_runs'])
                        extra_run[i['batting_team']][2] = extra_run[i['batting_team']][2] + int(i['legbye_runs'])
                except TypeError:
                    print("type error")

    print(extra_run)
    year=[y for y in extra_run.keys() ]
    matches=[m for m,nn,pr in extra_run.values()]
    print(matches)
    z=[nn for m,nn,pr in extra_run.values()]
    legbye_run=[pr for m,nn,pr in extra_run.values()]
    print(legbye_run)
    xpos=np.arange(len(year))
    plt.xticks(xpos,year)
    plt.bar(xpos-0.2,matches,width=0.4, label="extra_runs")
    plt.bar(xpos+0.2,z,width=0.4, label="noball_runs")
    plt.bar(xpos +0.4, legbye_run, width=0.4, label="legbye_runs")
    plt.legend()
    plt.xticks(rotation=25)
    plt.show()


function_1("2011")


