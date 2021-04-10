import requests
from DotaApi.api import Api

BASE_API_URL = 'https://api.opendota.com/api/'

class Players(Api):
    '''
    Wrapper for Matches Api Endpoint in Dota2
    '''
    def get_player_by_id(self, id):
        '''
        Get a match from OpenDota Api based on Match Id

        :params id: match id from dota 2
        '''
        url = f'{BASE_API_URL}/players/{id}' 
        response = requests.get(url=url, headers=self.add_headers())
        return response.json()

    def get_player_recent_matches(self, id):
        '''
        Get a match from OpenDota Api based on Match Id

        :params id: match id from dota 2
        '''
        url = f'{BASE_API_URL}/players/{id}/recentMatches' 
        response = requests.get(url=url, headers=self.add_headers())
        return response.json()

    def get_player_matches(self, id, **kwargs):
        '''
        Get a match from OpenDota Api based on Match Id

        :params id: match id from dota 2
        '''
        url = f'{BASE_API_URL}/players/{id}/matches' 
        response = requests.get(url=url, headers=self.add_headers(), params=kwargs)
        return response.json()