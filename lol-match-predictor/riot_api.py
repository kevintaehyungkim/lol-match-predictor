
import csv
import json
import requests


API_KEY = [ 'RGAPI-f9cf7be1-8f48-4cf4-b95c-b0c078cbf978', 
			'RGAPI-54a7cca5-befe-458e-bb4a-b20b7f65ba55',
			'RGAPI-8df5a619-b910-4d61-bdca-bf8ce84270b6']
REGION = 'na1'

PATCH_START_EPOCH_MILLI = 1601470800000
PATCH_END_EPOCH_MILLI = 1602669600000

RANKED_QUEUE_ID = 420

# match_ids = set()

# selected players to obtain match histories
player_ids = [
"LAFLAMME 01",
"hate it here",
"jojopyun 16",
"PantsAreFacebook",
"qpalzmwoiaj",
"John5un",
"KEITH EXOTIC",
"CtrI C",
"Spawwwwn",
"OSHMKUFA",
"100 Breezyyy",
"Doublelift",
"10 iQ PLAYER",
"Pants are Dragon",
"itzy dog",
"SuckQueen",
"Ba cua Sofm",
"Irk Luigi",
"Apple Pie 78",
"qpalzmwoiaj",
"Photograph",
"Diamond Emperor",
"potatoporcupine1",
"ThePyroGod",
"Ominui",
"Wave Control",
"AD Nannies Pref",
"10 iQ PLAYER",
"EG Junsik",
"snowing in april",
"MrJimmyOG supp",
"Young Tactician",
"RENGAR EATS BUTT",
"June 3rd Uzi",
"WA LAZA",
"Sweaty Intern",
"FF250KG",
"RapidfireX",
"Pentius",
"Super Vegeta",
"Wave Control",
"AD Nannies Pref",
"veerchand101",
"Masuta ni ikitai",
"BL00D rush"]


# riot account ids of players selected above
account_ids = [
'UztHeUupdA1OT1LgQ2CeXiTprO1u7LxNoH5FOXWaIIe5UQs', 
'R577mCO5KvDgOUyaof8U2fkXIYWbNpUPro4MDEMpW5W5fNDhbAoX5oHQ', 
'gegoxllKgvnvCuSU-RQKcrdtuhSfaZ6MZ2kiladCbxvEOQ', 
'ykfFA_FWaEcwSp1ufzCV1k7R5Cwv6a5pN42pfZ_NLONgiuk', 
'8I5jIH1hfe_vbErLhABrtmiZkER6QswC-ipZNTJYnEEGH7M', 
'WqMge7rw4zNWI5REZaoMvZkP9GlBrIyA6krxvSy-hUnNvA', 
'-7WeE6tbwJ39psFFjm7fqXJhU05cwXls3HkfQbdIK-P5f6b3tKdkkdI4', 
'HFGC-AuOJY5AhffBChVocPSDYKp_ukfdIl0YY3Inuo3L-A', 
'_zY6xJcRt8Gan0J5fALO1IziPZbbBiIzSYLypZeeNboLyA', 
'xsFPCxWRS7oc3f-q9k4fGOy29rZ71DIpnxcUYZo_FlBdLDQ', 
'mFAh5I9gwTI0ym4QvjAVIH2nn5tFJqZLoVF8IgiJhdDbYeu08mOReBIF', 
'fwx-IHTzYAkaayGQd1hE78huQ4Y6IZItKT-3-GRNtCkUSw',
'jThYf1jIMnqZMLtFY4e9dgYBP74j7b24eGN6oH6CuscpvDYSRRjy46G9', 
'qTW0akImPgTsaxqmS12uGjGRzkZbdn3TrSuOlg5q4L6-bg', 
'2LjLUBB6Ip3HY8Rk-ucqniXDLZGcr8rADk7HLnsJRoibsznBj3WGjsox']

account_ids2 = ['49o1_tOK7PYoHhlx9-zb42E9uQY3GTHGbcydUd7WajCzmwQ', 'zWrhGRh1GuH_gB--j5t-gYhJ6He2_GXWWd6tMokfB73hWQ', 'rdsHYQeEYopWBqOS8QV7vN9hP3cnZe2TYM90NMiy-RrCjLg', 'UmsU15TsrPx01sRICv7V3Bi9Sr2vMxI04FBk-4WpRvX-Wg', '8I5jIH1hfe_vbErLhABrtmiZkER6QswC-ipZNTJYnEEGH7M', 'xfFZpZaQbTv8kYC0IMvX59JuAGXEOXcIHU0Zxmtga_kU2w', '5F_cTIDXGGDRZLNwstFaxt9YCx0sO-Vu9aWXyB9GJIKp7HQ', 'fOSs1n9Pst0nHMmXUOBwqdcoDEBqWmxxQ_JQ6X1OEV4kQjY', 'rjXM7aZAZyBqt3T4PXGdU9zSwsMR33uvPkhPYdHLiro1zXM', 'zzyay8NG8xq0zCJU1I2pETxmzQs2ech0eL3PeSBlSkBDVtIORMM_53e9', 'ELN86To9Mi-3IyoALgHGzqpjRG93dFpLYrs1wlDGT_pxKVQ', 'jThYf1jIMnqZMLtFY4e9dgYBP74j7b24eGN6oH6CuscpvDYSRRjy46G9', 'q2zkyPjd2FhjNiKGCgwwjcuHLD5wBbXCWUtNdKI4VqcJu06q893V9cxk', '9wLrqqu8YstNTFcldU4r7eRKbTpmZIY6pSnui2A8Vocd0lp0I19j6wJz']
account_ids3 = ['fHfvsG_B5mHlfoI0y4fvBgN-Ie7t2gn9g5xTcYR0llKDOg', 'OP2a0MlA2MXCrhfSeZ9XGGZsOwkEDFqmh02UVJddXfhjNg', 'NCqYJtwvtr2ivn5Sq68wTMDPZOGjdnc4z1aMzlQAVbVliOq5FYph5YSS', '7bvZcGNLicD9LiYUcSfl3AAagkap-stBvISh-LBGggO53A', 'sI4M97wJ-ScSRnPgHF_hYuBuYuadRYTd5fI5GHMes-aTxeo', 'F6eHtCrf3Eq92ElqpbTD99UWMxl-Skep0VyAkNka9ijukw', 'on7DuUgEQvzRAZIiYpiqLanfm2phctrlj5-1jkLYoFBBLqXSCHLDrHdR', 'pHdLjpDDPYLERXdlK42p3VtAhJocCRhJOuJIQbZYZXosIQ', '7cYx4Qur1fi7mDopK6uAkHf99Jy3eucvoAO4-HfHC1xj9ag', '0sb4c3TT0xDpbGpW1WDEoC835m8pRR2_PcZNX67Yf1XtjA', 'zzyay8NG8xq0zCJU1I2pETxmzQs2ech0eL3PeSBlSkBDVtIORMM_53e9', 'ELN86To9Mi-3IyoALgHGzqpjRG93dFpLYrs1wlDGT_pxKVQ', 'Gb5nOyYe4zLz7N74iS5-ogkch7i32aCH8o8OWkWl5ZXBFqk', 'ASVmyNNx9NMmsR5RQ9cMTTHI-GpWE76l8U67aAxJ3bph5OY', '3aJKDlioIpbGdIAfZAeYSBvaQWv3wIcQrrDzxEMbK7BcAA']

unique_match_ids = []


# Riot API Endpoints #

def get_account_ids(player_ids):
	acc_ids = []
	for pid in player_ids:
		try:
			account_data = requests.get('https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + pid + '?api_key=' + API_KEY).json()
			account_id = account_data['accountId']
			acc_ids.append(str(account_id))
		except:
			print "wtf"
	print acc_ids


def get_account_matches(account_ids):
	for account_id in account_ids:
		matches_response = requests.get('https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/' + account_id +  '?beginTime=1601470800000&api_key=' + API_KEY).json()
		matches = matches_response['matches']

		for match in matches: 
			if match['queue'] == RANKED_QUEUE_ID and match['timestamp'] > PATCH_START_EPOCH_MILLI and match['timestamp'] < PATCH_END_EPOCH_MILLI:
				print match['gameId']


def get_all_match_data():
	match_ids = open('match_ids.txt', 'r')

	all_match_data = []
	i = 0
	
	for match_id in match_ids:
		raw_match_data = requests.get('https://na1.api.riotgames.com/lol/match/v4/matches/' + str(long(match_id)) + '?api_key=' + API_KEY[i]).json()

		blue = { "side": [0], "firstTower": [], "firstBlood": [], "firstRiftHerald": [], "firstInhibitor": [], "TOP": [], "JUNGLE": [], "MID": [], "ADC": [], "SUP": [], "win": [] }
		red = { "side": [1], "firstTower": [], "firstBlood": [], "firstRiftHerald": [], "firstInhibitor": [], "TOP": [], "JUNGLE": [], "MID": [], "ADC": [], "SUP": [], "win": [] }

		# print raw_match_data

		team1 = raw_match_data["teams"][0]
		team2 = raw_match_data["teams"][1]

		# team 1 is blue side
		if team1["teamId"] == 100:
			if team1["win"] == "Win":
				blue["win"] = [1] 
				red["win"] = [0] 
			else:
				blue["win"] = [0]
				red["win"] = [1] 

			blue["firstTower"] = [int(team1["firstTower"])]
			blue["firstBlood"] = [int(team1["firstBlood"])]
			blue["firstRiftHerald"] = [int(team1["firstRiftHerald"])]
			blue["firstInhibitor"] = [int(team1["firstInhibitor"])]

			red["firstTower"] = [int(team2["firstTower"])]
			red["firstBlood"] = [int(team2["firstBlood"])]
			red["firstRiftHerald"] = [int(team2["firstRiftHerald"])]
			red["firstInhibitor"] = [int(team2["firstInhibitor"])]

		# team 1 is red side
		else: 
			if team1["win"] == "Win":
				blue["win"] = [0] 
				red["win"] = [1] 
			else:
				blue["win"] = [1]
				red["win"] = [0] 

			red["firstTower"] = [int(team1["firstTower"])]
			red["firstBlood"] = [int(team1["firstBlood"])]
			red["firstRiftHerald"] = [int(team1["firstRiftHerald"])]
			red["firstInhibitor"] = [int(team1["firstInhibitor"])]

			blue["firstTower"] = [int(team2["firstTower"])]
			blue["firstBlood"] = [int(team2["firstBlood"])]
			blue["firstRiftHerald"] = [int(team2["firstRiftHerald"])]
			blue["firstInhibitor"] = [int(team2["firstInhibitor"])]

		for player in raw_match_data["participants"]:
			team = player["teamId"]
			role = player["timeline"]["role"]
			lane = player["timeline"]["lane"]
			position = find_position(role, lane)
			print position

			stats = [
				player["stats"]["totalDamageDealtToChampions"], 
				player["stats"]["damageDealtToObjectives"],
				player["stats"]["visionScore"],
				player["stats"]["kills"],
				player["stats"]["deaths"],
				player["stats"]["assists"],
				player["stats"]["goldEarned"],
				player["stats"]["totalMinionsKilled"],
				player["stats"]["champLevel"]]

		

			if team == 100:
				if position == "N/A": 
					blue["SUP"] += stats
				else:
					blue[position] += stats
			else:
				if position == "N/A":
					red["SUP"] += stats
				else:
					red[position] += stats

	
		blue_combined = blue["side"] + blue["firstBlood"] + blue["firstTower"] + blue["firstRiftHerald"] + blue["firstInhibitor"] + blue["TOP"] + blue["JUNGLE"] + blue["MID"] + blue["ADC"] + blue["SUP"] + blue["win"]
		red_combined = red["side"] + red["firstBlood"] + red["firstTower"] + red["firstRiftHerald"] + red["firstInhibitor"] + red["TOP"] + red["JUNGLE"] + red["MID"] + red["ADC"] + red["SUP"] + red["win"]

		print blue_combined
		print red_combined

		if len(blue_combined) == 51:
			all_match_data.append(blue_combined)

		if len(red_combined) == 51:
			all_match_data.append(red_combined)

		print len(all_match_data)
		i = (i + 1) % 3

	with open("data.csv", "w") as f:
	    writer = csv.writer(f)
	    writer.writerows(all_match_data)
	
	return all_match_data



# Helper Methods #

def filter_unique_match_ids():
	match_ids = open('match_ids.txt', 'r')
	unique_mids = set()

	for match_id in match_ids:
		unique_mids.add(long(match_id))

	for unique_mid in list(unique_mids):
		print unique_mid

	return 


def find_champion_id_mapping():
	champion_id_map = {}
	with open('champions_raw.json') as json_file:
	
		raw_champion_data = json.load(json_file)
		
		for champion in raw_champion_data['data']:
			cid = int(raw_champion_data['data'][champion]['key'])
			cname = str(raw_champion_data['data'][champion]['name'])
			champion_id_map[cid] = cname
		
	print champion_id_map
	return


def find_position(role, lane): 
	if not role and not lane:
		return "N/A"

	if role == "SOLO":
		if lane == "TOP":
			return "TOP"
		else:
			return "MID"
	elif role == "NONE" and lane == "JUNGLE":
		return "JUNGLE"
	elif lane == "BOT" or lane == "BOTTOM":
		if "role" == "DUO_SUPPORT":
			return "SUP"
		else: 
			return "ADC"

	return "N/A"

# get_account_ids(player_ids2)
# get_account_ids(player_ids3)


# get_account_matches(account_ids2)
# get_account_matches(account_ids3)



# find_champion_id_mapping()

print(get_all_match_data())





