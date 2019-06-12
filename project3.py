# For the year 2016 plot the extra runs conceded per team.

import csv
from collections import Counter
from collections import defaultdict
from matplotlib import pyplot as plt
id_ipl=[]
extra_run={}
team_ipl=[]
with open ('deliveries.csv') as delivery:
    with open('matches.csv') as matches:
        delivery_dict=csv.DictReader(delivery)
        matches_dict=csv.DictReader(matches)

        for i in matches_dict:
            if i['season']=='2016':
                id_ipl.append(i['id'])

        print(list(id_ipl))

        for i in delivery_dict:
            if i["match_id"] in id_ipl:
                extra_run.setdefault(i['batting_team'],0)
                extra_run[i['batting_team']]=extra_run[i['batting_team']]+int(i['extra_runs'])

            else:
                continue
print(extra_run)
team_ipl=[y for y in extra_run.keys() ]
total_extra_run=[m for m in extra_run.values()]
plt.plot(team_ipl,total_extra_run)
plt.xticks(rotation=30)
plt.show()





