import requests
import json
def get_nextMatch_info():
    uri = 'https://api.football-data.org/v4/teams/81/matches?status=SCHEDULED&limit=1'
    headers = { 'X-Auth-Token': '' }#api key for apifotball needed

    response = requests.get(uri, headers=headers)
    for match in response.json()['matches']:
        gameType = match['competition']['type']
        matchNum = match['season']['currentMatchday']
        homeTeam =match['homeTeam']['name']
        awayTeam = match['awayTeam']['name']
        gameDate = match['utcDate']
        compType = match['stage']
        homeBadge =match['homeTeam']['crest']
        awayBadge = match['awayTeam']['crest']

    return gameType, matchNum, homeTeam, awayTeam, gameDate, compType, homeBadge ,awayBadge