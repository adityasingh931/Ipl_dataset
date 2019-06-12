# For the year 2015 plot the top economical bowlers.

import csv
from collections import Counter
from collections import defaultdict
from matplotlib import pyplot as plt
id_ipl=[]
total_run={}
team_ipl=[]
bowler_name=[]
with open ('deliveries.csv') as delivery:
    with open('matches.csv') as matches:
        delivery_dir=csv.DictReader(delivery)
        matches_dir=csv.DictReader(matches)

        for i in matches_dir:
            if i['season']=='2015':
                id_ipl.append(i['id'])

        print(list(id_ipl))

        for i in delivery_dir:
            if i["match_id"] in id_ipl:
                bowler_name.append(i['bowler'])
                total_run.setdefault(i['bowler'],0)
                total_run[i['bowler']]=total_run[i['bowler']]+int(i['total_runs'])

print(total_run)
bowler_ball_count=(Counter(bowler_name))
print(bowler_ball_count)
economy={}
for i in total_run:
    if bowler_ball_count.keys()==total_run.keys():
        economy[i]=float("{0:.2f}".format((total_run[i]/int(bowler_ball_count[i]))*6))
print(economy)
economy=sorted(economy.items(),key=lambda x:x[1])
top_10_bowler=dict(economy[0:10])
bowler_name=[y for y in top_10_bowler.keys() ]
bowler_economy=[m for m in top_10_bowler.values()]
plt.plot(bowler_name, bowler_economy)
plt.xticks(rotation=50)
plt.show()




