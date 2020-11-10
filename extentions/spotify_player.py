import requests, json

from extentions.funcs import speak


def spotify_player(req, option):

    # Using refresh token to gen new api access token
    Auth1 = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Basic TOKEN"
    }

    params1 = {
        "grant_type": "refresh_token",
        "refresh_token": "refresh token"
    }

    request = requests.post('https://accounts.spotify.com/api/token', headers=Auth1, params=params1)
    x = request.json()

    token = x['access_token']


    # Using acess token to get access to spotify's api
    Auth = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    if req == 'put':
        r = requests.put(f'https://api.spotify.com/v1/me/player/{option}', headers=Auth)

    elif req == 'post':
        r = requests.post(f'https://api.spotify.com/v1/me/player/{option}', headers=Auth)

    elif req == 'get':
        r = requests.get(f'https://api.spotify.com/v1/me/player/{option}', headers=Auth)

    if option == 'currently-playing':
        try:
            x = r.json()
            item = x['item']
            uri = item['uri']
            requests.post(f"https://api.spotify.com/v1/me/player/queue?{uri}", headers=Auth)
        except:
            speak('I cant add this song to queue. checkout my code')