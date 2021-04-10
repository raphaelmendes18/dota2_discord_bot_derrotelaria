import requests
from DotaApi.api import Api

BASE_API_URL = 'https://api.opendota.com/api/'

class Heroes(Api):
    '''
    Wrapper for Matches Api Endpoint in Dota2
    '''
    def get_hero_by_id(self, id):
        '''
        Get a match from OpenDota Api based on Match Id

        :params id: match id from dota 2
        '''
        url = f'{BASE_API_URL}/heroes' 
        response = requests.get(url=url, headers=self.add_headers())
        
        heroes = next(filter(lambda hero: hero['id'] == id, response.json()))
        return heroes


