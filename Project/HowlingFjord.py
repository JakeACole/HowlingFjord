# Project Howling Fjord
# Authors: Jake and Iliya
# A World of Warcraft Mythic Plus Analytics Tool

import requests
import json
import datetime
import io

class Server:
    def __init__(self):
        self.locale = ''
        self.api_key = ''
        self.access_token = ''

        # urls for query
        self.realm_index_url = ''
        self.realm_url = ''
        self.mythic_leaderboard_index_url = ''
        self.mythic_leaderboard_dungeon_url = ''

        # parsed data
        self.realm_slug = ''
        self.realm_id = ''
        self.dungeon_id = ''
        self.period = ''

    def get_realm_index(self):
        #https://us.api.battle.net/data/wow/realm/?namespace=dynamic-us&locale=en_US&access_token= + self.accessToken
        self.realm_index_url = "https://" + self.locale + \
              ".api.battle.net/data/wow/realm/" + \
              "?namespace=dynamic-us&locale=en_US&access_token=" + self.access_token

        print (self.realm_index_url + "\n")

        _data = requests.get(self.realm_index_url).text

        #print (data)

        return _data

    def get_realm(self):
        #https://us.api.battle.net/data/wow/realm/magtheridon?namespace=dynamic-us&locale=en_US&access_token + self.access_token

        self.realm_url = "https://" + self.locale + \
              ".api.battle.net/data/wow/realm//" + self.realm_slug + \
              "?namespace=dynamic-us&locale=en_US&access_token=" + self.access_token

        print (self.realm_url + "\n")

        _data = requests.get(self.realm_url).text

        #print (data)

        return _data

    def get_mythic_leaderboard_index(self):
        #https://us.api.battle.net/data/wow/connected-realm/78/mythic-leaderboard/?namespace=dynamic-us&locale=en_US&access_token= + self.access_token

        self.mythic_leaderboard_index_url = "https://" + self.locale + \
              ".api.battle.net/data/wow/connected-realm/" + self.realm_id + \
              "/mythic-leaderboard/?namespace=dynamic-us&locale=en_US&access_token=" + self.access_token

        #https://us.api.battle.net/data/wow/connected-realm/?namespace=dynamic-us&locale=en_US&access_token=access_token

        print (self.mythic_leaderboard_index_url + "\n")

        _data = requests.get(self.mythic_leaderboard_index_url).text

        #print (data)

        return _data

    def get_mythic_leaderboard_dungeon(self):
        #https://us.api.battle.net/data/wow/connected-realm/78/mythic-leaderboard/197/period/630?namespace=dynamic-us&locale=en_US&access_token= + self.access_token

        self.mythic_leaderboard_dungeon_url = "https://" + self.locale + \
              ".api.battle.net/data/wow/connected-realm/" + self.realm_id + \
              "/mythic-leaderboard/" + self.dungeon_id + "/period/" + self.period + "?namespace=dynamic-us&locale=en_US&access_token=" + self.access_token

        #https://us.api.battle.net/data/wow/connected-realm/?namespace=dynamic-us&locale=en_US&access_token=access_token

        print (self.mythic_leaderboard_dungeon_url + "\n")

        _data = requests.get(self.mythic_leaderboard_dungeon_url).text

        #print (data)

        return _data

def import_key(api_key_file):
    f = open(api_key_file, "r")
    _api_key = f.read()
    #print(apikey)
    return _api_key

def convert_epoch(epoch):
    # divide by 1e3 for conversion to datetime
    _converted_epoch = datetime.datetime.fromtimestamp(epoch / 1e3)

    # format converted epoch to string format
    _converted_epoch = _converted_epoch.strftime('%Y-%m-%d %H:%M:%S')

    print (_converted_epoch)

    return _converted_epoch

def write_json(input_file, json_input):
    with io.open(input_file, 'w', encoding='utf-8') as f:
        #loads for json string, load for file or url
        _parsed_json = json.loads(json_input)

        f.write(json.dumps(_parsed_json, indent=4, sort_keys=True))

if __name__ == '__main__':
    _serverInstance = Server
    _serverInstance.api_key = import_key("../ApiKeys/apikey.txt")
    _serverInstance.access_token = import_key("../ApiKeys/access_token.txt")
    _serverInstance.locale = "us"

    _realm_index_json = _serverInstance.get_realm_index(_serverInstance)

    print (_realm_index_json)

    write_json("realm_index_json.txt", _realm_index_json)

    _parsed_realm_index_json = json.loads(_realm_index_json)

    print(_parsed_realm_index_json["realms"][50]["slug"])

    #parse realm index and get the realm_slug, you need to set _serverInstance.realm_slug

    # Set this
    _serverInstance.realm_slug = 'malganis'

    _realm_json = _serverInstance.get_realm(_serverInstance)

    write_json("realm_json.txt", _realm_json)

    # Set this
    _serverInstance.realm_id = '3684'

    _mythic_leaderboard_index_json = _serverInstance.get_mythic_leaderboard_index(_serverInstance)

    write_json("mythic_leaderboard_index_json.txt", _mythic_leaderboard_index_json)

    # Set these
    _serverInstance.dungeon_id = '199'
    _serverInstance.period = '632'

    _mythic_leaderboard_dungeon_json = _serverInstance.get_mythic_leaderboard_dungeon(_serverInstance)

    write_json("mythic_leaderboard_dungeon_json.txt", _mythic_leaderboard_dungeon_json)

    _epoch = (1518533999000)

    _converted_timestamp = convert_epoch(_epoch)
