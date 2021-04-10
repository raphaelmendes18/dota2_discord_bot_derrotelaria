import requests
import os 
class Api:

    def add_headers(self, headers = {}):

        headers.update({
            'Authorization': 'Bearer ' + os.environ['OPEN_DOTA_KEY']
        })

        return headers

