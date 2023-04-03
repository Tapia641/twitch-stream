import requests
import json
import yaml

def read_credentials():
    # Open the YAML file
    with open('../keys.yml', 'r') as file:
        # Load the YAML content
        content = yaml.safe_load(file)
        return content['keys_facebook']

def generate_token(client_id:str, client_secret:str):
    url = 'https://graph.facebook.com/oauth/access_token'
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

def test_live(access_token:str, page_id:str):
    # Obtener un token de acceso de larga duración
    response = requests.get(f'https://graph.facebook.com/{page_id}?fields=access_token&access_token={access_token}')
    print(response._content.decode('utf-8'))
    # long_lived_token = response.json()['access_token']
    # Iniciar transmisión en vivo
    # response = requests.post(f'https://graph.facebook.com/{page_id}/live_videos',
    #                         params={'access_token': long_lived_token},
    #                         data={'status': 'LIVE_NOW', 'title': 'Testing'})


if __name__ == "__main__":
    keys = read_credentials()
    token = generate_token(keys['client_id'], keys['client_secret'])
    # print(token,keys['page_id'])
    value = test_live(token, keys['page_id'])
