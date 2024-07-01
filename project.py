# spotify project i think
import requests
import pandas as pd
import sqlalchemy as db

CLIENT_ID = ""
CLIENT_SECRET = ""

AUTH_URL = 'https://accounts.spotify.com/api/token'
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})
auth_response_data = auth_response.json()
access_token = auth_response_data['access_token']
headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}

BASE_URL = 'https://api.spotify.com/v1/'
track_id = input('Enter track id: ')
r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)

data = r.json()
print(data)

# Day 3

tbl = pd.DataFrame.from_dict(details, orient='columns')
engine = db.create_engine('sqlite:///tbl.db')
tbl.to_sql('spotify_stats', con=engine, if_exists='replace', index=False)

with engine.connect() as connection:
   query_result = connection.execute(db.text("SELECT * FROM table_name;")).fetchall()
   print(pd.DataFrame(query_result))
