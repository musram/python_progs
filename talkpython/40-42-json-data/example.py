import json
import requests






if __name__ == "__main__":

    r = requests.get('https://us.api.battle.net/wow/character/Cenarion%20Circle/Ardy?fields=mounts&locale=en_US&apikey=')

    data = json.loads(r.text)


    print(data)
