# Plot a stacked bar chart of matches won of all teams over all the years of IPL.

import csv
import numpy as np
import pandas as pn
from collections import defaultdict
import matplotlib
from collections import Counter
from matplotlib import pyplot as plt

winner_ipl=[]
year_ipl=[]
with open('matches.csv') as matches:
    matches_dict=csv.DictReader(matches)

    for i in matches_dict:
        winner_ipl.append(i['winner'])
        year_ipl.append(i['season'])

year_team_dict= defaultdict(list)

for i, j in zip(year_ipl, winner_ipl):
    year_team_dict[i].append(j)
print(year_team_dict)
year_team_count={}
for i in year_team_dict:
    temp={}
    for j in year_team_dict[i]:
        temp[j]=year_team_dict[i].count(j)
    year_team_count[i]=temp
print(year_team_count)
X_axis=tuple(year_team_count['2014'].keys())
index=pn.Index(X_axis, name='test')

df=pn.DataFrame(year_team_count, index=index)
matplotlib.style.use('fivethirtyeight')
plt.style.available
ax=df.plot(kind='bar', stacked=True  , figsize=(100,5))
matplotlib.style.use('ggplot')
plt.style.available
plt.show()









