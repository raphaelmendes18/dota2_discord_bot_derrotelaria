import requests
from DotaApi.api import Api

BASE_API_URL = 'https://api.opendota.com/api/'

class Matches(Api):
    '''
    Wrapper for Matches Api Endpoint in Dota2
    '''

    def __init__(self, id):
        self.id = id
        self.match_info = self.get_match_info()

    def get_match_info(self):
        '''
        Get a match from OpenDota Api based on Match Id

        :params id: match id from dota 2
        '''
        url = f'{BASE_API_URL}/matches/{self.id}' 
        response = requests.get(url=url, headers=self.add_headers())
        return response.json()

