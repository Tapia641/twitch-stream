import requests
import yaml

def read_credentials():
    # Open the YAML file
    with open('../keys.yml', 'r') as file:
        # Load the YAML content
        content = yaml.safe_load(file)
        return content['keys_twitch']

def generate_token(client_id:str, client_secret:str):
    url = 'https://id.twitch.tv/oauth2/token'
    params = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, params=params)
    content_utf8 = response.content.decode("utf-8")
    obj = yaml.safe_load(content_utf8)

    access_token = obj['access_token']
    return access_token

def test_live(access_token:str, streamers:list):
    
    # Streamer que queremos validar

    for streamer_login in streamers:
        # Endpoint para obtener información del streamer
        stream_endpoint = f'https://api.twitch.tv/helix/streams?user_login={streamer_login}'

        # Headers con el token de acceso
        headers = {
            'Client-ID': client_id,
            'Authorization': f'Bearer {access_token}'
        }

        # Realizamos la petición para obtener la información del streamer
        response = requests.get(stream_endpoint, headers=headers)
        data = response.json()

        # Si hay al menos un stream en la respuesta, entonces el streamer está en vivo
        if data['data']:
            print(f"El streamer {streamer_login} está en vivo.")
        else:
            print(f"El streamer {streamer_login} no está en vivo.")

if __name__ == "__main__":

    keys = read_credentials()
    token = generate_token(keys['client_id'], keys['client_secret'])
    streamers = ['juansguarnizo', 'asimog','quackity']
    value = test_live(token, streamers)

