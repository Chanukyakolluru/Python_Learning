# To connect API , import requests module

import requests
base_url ="https://pokeapi.co/api/v2/"

def get_pokemon_data(name):
    url =f"{base_url}/pokemon/{pokemon_name}"
    response=requests.get(url)
    print(response)

    if response.status_code == 200:
        print(response.json())
        print("API response is successful and pokeman data retrieved!")
    else:
        print("Response failed")

pokemon_name ="pikachu"
pokeman_data= get_pokemon_data(pokemon_name)

if pokeman_data:
    print(f"{pokeman_data["name"]}")

####################################################
import requests
from bs4 import BeautifulSoup
url = "https://www.bbc.com/"

def bbc():
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        soup= BeautifulSoup(response.text,"html.parser")
        pretty_html= soup.prettify()
        print(pretty_html[:1000])

bbc()