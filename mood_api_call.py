#Modified from codingforentrepreneurs' Reusable Spotify API Client
#Link for Reusable Client: https://github.com/codingforentrepreneurs/30-Days-of-Python/blob/master/tutorial-reference/Day%2019/client/spotify_client.py

import base64
import datetime
import time
from urllib.parse import urlencode

import requests

class SpotifyAPI(object):
    access_token = None
    access_token_expires = datetime.datetime.now()
    access_token_did_expire = True
    client_id = None
    client_secret = None
    token_url = "https://accounts.spotify.com/api/token"
    
    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secret = client_secret

    def get_client_credentials(self):
        """
        Returns a base64 encoded string
        """
        client_id = self.client_id
        client_secret = self.client_secret
        if client_secret == None or client_id == None:
            raise Exception("You must set client_id and client_secret")
        client_creds = f"{client_id}:{client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode())
        return client_creds_b64.decode()
    
    def get_token_headers(self):
        client_creds_b64 = self.get_client_credentials()
        return {
            "Authorization": f"Basic {client_creds_b64}"
        }
    
    def get_token_data(self):
        return {
            "grant_type": "client_credentials"
        } 
    
    def perform_auth(self):
        token_url = self.token_url
        token_data = self.get_token_data()
        token_headers = self.get_token_headers()
        r = requests.post(token_url, data=token_data, headers=token_headers)
        if r.status_code not in range(200, 299):
            raise Exception("Could not authenticate client.")
            # return False
        data = r.json()
        now = datetime.datetime.now()
        access_token = data['access_token']
        expires_in = data['expires_in'] # seconds
        expires = now + datetime.timedelta(seconds=expires_in)
        self.access_token = access_token
        self.access_token_expires = expires
        self.access_token_did_expire = expires < now
        return True
    
    def get_access_token(self):
        token = self.access_token
        expires = self.access_token_expires
        now = datetime.datetime.now()
        if expires < now:
            self.perform_auth()
            return self.get_access_token()
        elif token == None:
            self.perform_auth()
            return self.get_access_token() 
        return token
    
    def get_resource_header(self):
        access_token = self.get_access_token()
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        return headers
        
        
    def get_resource(self, batch_id, resource_type='audio-features', version='v1'):
        endpoint = f"https://api.spotify.com/{version}/{resource_type}/?ids={batch_id}"
        headers = self.get_resource_header()
        r = requests.get(endpoint, headers=headers)
        if r.status_code not in range(200, 299):
            return {}
        return r.json()
    
#Fill in client_id and client_secret
client_id= ""
client_secret= ""

start2= time.time()
print("Clock started")

client= SpotifyAPI(client_id, client_secret)
client.get_client_credentials()
client.get_token_headers()
client.get_token_data()
client.perform_auth()
client.get_access_token()
client.get_resource_header()

audioresponses=list()
concatls_len= len(concatls)
for index in range(concatls_len):
    audiojson= client.get_resource(batch_id=concatls[index])
    audioresponses.append(audiojson)
    
valencels=list()
energyls=list()
idcheckls=list()
for index2 in range(len(audioresponses)):
    #for index3 in range(len(audioresponses[index2])):
    for index3 in range(len(audioresponses[index2]["audio_features"])):
        valencels.append(audioresponses[index2]["audio_features"][index3]["valence"])
        energyls.append(audioresponses[index2]["audio_features"][index3]["energy"])
        idcheckls.append(audioresponses[index2]["audio_features"][index3]["id"])
                         
valencedf= pd.DataFrame(valencels)
energydf= pd.DataFrame(energyls)
idcheckdf= pd.DataFrame(idcheckls)
combineddf= pd.concat([valencedf, energydf, idcheckdf], axis=1, sort=False)
combineddf.columns = ["Valence", "Energy", "ID Check"]
combineddf.to_csv("all_mood_features2.csv", index= False)

end2= time.time()
print("Seconds: %.2f"
      % (end2-start2))
