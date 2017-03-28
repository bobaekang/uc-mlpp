'''
------------------------------------------------------------------------
This is Bobae's PS4:
The current script contains the codes for exercises 2, part (b).
The data in this script is from one of the Kaggle datasets:
https://www.kaggle.com/joelwilson/2012-2016-presidential-elections.
------------------------------------------------------------------------
'''
# import packages
import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

# read in the data
votes = DataFrame(pd.read_csv('votes.csv'))

# get and tidy the 2016 vote data
votes16 = votes.ix[:,2:12]
votes16.columns = ['id', 'votesDem', 'votesRep', 'votesTotal', 'percentDem',
    'percentRep', 'votesDiff', 'percentDiff', 'state', 'county']
votes16['year'] = '2016'
votes16 = votes16[['year', 'id', 'state', 'county', 'votesTotal', 'votesDem',
    'votesRep', 'votesDiff', 'percentDem', 'percentRep', 'percentDiff']]

# get and tidy the 2012 vote data
votes12 = votes.ix[:,13:25]
votes12.columns = ['votesTotal', 'votesDem', 'votesRep', 'id', 'stateid',
    'percentDem', 'percentRep', 'votesDiff', 'percentDiff', 'x', 'county', 'state']
votes12['year'] = '2012'
votes12 = votes12[['year', 'id', 'state', 'county', 'votesTotal', 'votesDem',
    'votesRep', 'votesDiff', 'percentDem', 'percentRep', 'percentDiff']]

# combine the two
votesAll = votes16.append(votes12)

# compare the differences in the number of votes between two elections
TotalCompare = DataFrame(votesAll.groupby('year')['votesTotal'].sum())
DemCompare = DataFrame(votesAll.groupby('year')['votesDem'].sum())
RepCompare = DataFrame(votesAll.groupby('year')['votesRep'].sum())
DiffCompare = DataFrame(votesAll.groupby('year')['votesDiff'].sum())

# plot
fig, axs = plt.subplots(2,2)
axs = axs.ravel()

# assign objects to be plotted
data = [TotalCompare.votesTotal, DemCompare.votesDem,
    RepCompare.votesRep, DiffCompare.votesDiff]
xticks = [1, 2]
xticklabels = ['2012', '2016']
color = ['green', 'blue', 'red', 'yellow']
subtitles = ['Votes total', 'Votes Democrat', 'Votes Republican', 'Votes difference']

# use iteration to make four subplots
for i in range(4):
    axs[i].bar(xticks, data[i], color = color[i], align = 'center') # bar graph
    # set the xticks to be '2012' and '2016'
    axs[i].set_xticks(xticks)
    axs[i].set_xticklabels(xticklabels)
    axs[i].set_ylim([0, 150000000]) # common ylim
    axs[i].set_title(subtitles[i], size =12) # title for each subplot

# set the common labels and title
fig.text(0.5, 0.04, 'Year', ha='center', va='center') # x-axis
fig.text(0.06, 0.5, 'Count (in 100 millions)', ha='center', va='center', rotation='vertical') # y-axis
fig.suptitle('Compare Votes in Two Elections', size = 15) # title

plt.savefig('fig_1c') # save the plot
plt.show()
plt.close()
