import requests
from DotaApi.api import Api

BASE_API_URL = 'https://api.opendota.com/api/'

class Player(Api):
    '''
    Wrapper for Matches Api Endpoint in Dota2
    '''
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.player_info = self.get_player_info()

    def get_info(self):
        '''
        Get a match from OpenDota Api based on Match Id

        :params id: match id from dota 2
        '''
        url = f'{BASE_API_URL}/players/{self.id}' 
        response = requests.get(url=url, headers=self.add_headers())
        
        '''
        response.json()
        {
        "tracked_until": "string",
        "solo_competitive_rank": "string",
        "competitive_rank": "string",
        "rank_tier": 0,
        "leaderboard_rank": 0,
        "mmr_estimate": {
            "estimate": 0,
            "stdDev": 0,
            "n": 0
        },
        "profile": {
            "account_id": 0,
            "personaname": "string",
            "name": "string",
            "plus": true,
            "cheese": 0,
            "steamid": "string",
            "avatar": "string",
            "avatarmedium": "string",
            "avatarfull": "string",
            "profileurl": "string",
            "last_login": "string",
            "loccountrycode": "string",
            "is_contributor": false
            }
        }
        '''
        return response.json()

    def get_recent_matches(self):
        '''
        Get the recent matches from OpenDota Api based on Match Id for a given player
        '''
        url = f'{BASE_API_URL}/players/{self.id}/recentMatches' 
        response = requests.get(url=url, headers=self.add_headers())
        return response.json()

    def get_matches(self, **kwargs):
        '''
        Get all matches from OpenDota Api based on player id

        :params id: match id from dota 2
        '''
        url = f'{BASE_API_URL}/players/{self.id}/matches' 
        response = requests.get(url=url, headers=self.add_headers(), params=kwargs)
        return response.json()

    def get_matches_with_peers(self, **kwargs):
        '''
        Get all peers of all matches for a player id
        kwargs
        :included_account_id: the account id of a peer
        '''
        url = f'{BASE_API_URL}/players/{self.id}/peers'
        response = requests.get(url=url, headers=self.add_headers(), params=kwargs)
        '''
        response.json()
        Copy Expand all Collapse all
        [
            {
            "account_id": 0,
            "last_played": 0,
            "win": 0,
            "games": 0,
            "with_win": 0,
            "with_games": 0,
            "against_win": 0,
            "against_games": 0,
            "with_gpm_sum": 0,
            "with_xpm_sum": 0,
            "personaname": "string",
            "name": "string",
            "is_contributor": true,
            "last_login": "string",
            "avatar": "string",
            "avatarfull": "string"
            }
        ]
        '''
        return response.json()