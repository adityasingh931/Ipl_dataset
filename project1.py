# Plot the number of matches played per year of all the years in IPL.

import time
start_time = time.time()
import csv
from collections import Counter
from matplotlib import pyplot as plt
season_ipl=[]
with open('matches.csv') as matches:
    matches_dict=csv.DictReader(matches)

    for i in matches_dict:
        season_ipl.append(i['season'])

count_season=(Counter(season_ipl))
season=[y for y in count_season.keys() ]
no_of_matches=[m for m in count_season.values()]
plt.plot(season,no_of_matches)
print(time.time() - start_time)
plt.show()





