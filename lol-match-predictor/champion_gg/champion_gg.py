
import json
from pprint import *


'''
A simple script to organize raw champion data 'raw_stats.txt'
provided by Champion.GG into 'champion_stats.json'.


The columns in 'raw_stats.txt' represent (in order):
Rank	
Champion	
Role	
Win Percent	
Play Percent	
Ban Rate	
Playerbase Avg. Games	
Kills	
Deaths	
Assists	
Largest Killing Spree	
Damage Dealt	
Damage Taken	
Total Healing	
Minions Killed	
Enemy Jungle CS	
Team Jungle CS	
Gold Earned	
Role Position	
Position Change
'''

file = open('raw_stats.txt', 'r')

champion_stats = {}

i = 0
curr_champion = ""
for line in file:
	
	if i == 1: 
		curr_champion = str(line[1:-1])
		if curr_champion not in champion_stats:
			champion_stats[curr_champion] = {}

	elif i == 2: 
		stats = line.split()

		# champion specific features
		winrate = float(stats[1][:-1])*0.01
		kda = (float(stats[5])+float(stats[7]))/float(stats[6])
		damage_dealt = int(stats[9])
		damage_taken = int(stats[10])
		gold = float(stats[15])

		champion_stats[curr_champion][str(stats[0])] = [winrate, kda, damage_dealt, damage_taken, gold]

	i = (i + 1) % 3


with open("champion_stats.json", "w") as outfile:  
    json.dump(champion_stats, outfile, indent = 2) 


# pprint(champion_stats)

