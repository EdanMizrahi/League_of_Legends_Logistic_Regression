import requests
import json
import os

# Functions to make API calls to the Riot Games API. 


def get_summoner(summoner_name,api_key,create_file = True):
	# Function to retreive information on summoner and create a readable file JSON. 
	
	dirName = f'riot_games/summoner/{summoner_name}/'
	if not os.path.exists(dirName):
		# Creat the file path and get the summoner info from Riot API.
		os.mkdir(dirName)
		print("Directory " , dirName ,  " Created ") 


	url = f'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}'
	headers = {
	    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
	    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
	    "Origin": "https://developer.riotgames.com",
	    "X-Riot-Token": api_key
	}
	r=requests.get(url, headers=headers)
	print(f"Summoner request for {summoner_name}\tStatus code: {r.status_code}")
	summoner_dict = r.json()
	# If we want to create a file, then it creates a file. 
	if create_file == True:
		readable_file = f"riot_games/summoner/{summoner_name}/{summoner_dict['name']}.json"
		with open(readable_file, 'w') as f:
			json.dump(summoner_dict, f, indent=4)


	return summoner_dict




	return summoner_dict

def get_matchlist(summoner_name,account_id,api_key,create_file = True):
	# Function to retreive information on summoner and create a readable file JSON. 
	
	url = f'https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/{account_id}'
	headers = {
	    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
	    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
	    "Origin": "https://developer.riotgames.com",
	    "X-Riot-Token": api_key
	}
	r=requests.get(url, headers=headers)
	print(f"Matchlist request for {account_id}\tStatus code: {r.status_code}")
	summoner_matchlist = r.json()

	# If we want to create a file, then it creates a file. 
	if create_file == True:
		readable_file_matchlist = f"riot_games/summoner/{summoner_name}/{summoner_name}_matchlist.json"
		with open(readable_file_matchlist, 'w') as f:
			json.dump(summoner_matchlist, f, indent=4)

	return summoner_matchlist


def get_match(match_id, api_key):
	# Function to get match information from a match Id.
	url= f"https://euw1.api.riotgames.com/lol/match/v4/matches/{match_id}"
	headers = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": api_key
	}
	r=requests.get(url, headers=headers)
	print(f"Match request for {match_id}\tStatus code: {r.status_code}")

	match_data = r.json()



	return match_data