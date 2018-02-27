# Project Howling Fjord
# Project Description :
# Authors: Jake and Iliya
# Cool Stuff

import requests
import json

class Server:
    def __init__(self):
        self.locale = ''
        self.access_token = ''
        self.api_key = ''

        self.realm_index_url = ''
        self.realm_url = ''
        self.mythic_leaderboard_index_url = ''
        self.mythic_leaderboard_dungeon_url = ''

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

if __name__ == '__main__':
    _serverInstance = Server
    _serverInstance.apikey = import_key("../ApiKeys/apikey.txt")
    _serverInstance.accessToken = import_key("../ApiKeys/access_token.txt")
    _serverInstance.locale = "us"

    _realm_index_json = _serverInstance.get_realm_index(_serverInstance)

    #parse realm index and get the realm_slug, you need to set _serverInstance.realm_slug

    # Set these
    # _serverInstance.realm_slug
    # _serverInstance.realm_id
    # _serverInstance.dungeon_id
    # _serverInstance.period

    _realm__json = _serverInstance.get_realm(_serverInstance)
    _mythic_leaderboard_index_json = _serverInstance.get_mythic_leaderboard_index(_serverInstance)
    _mythic_leaderboard_dungeon_json = _serverInstance.get_mythic_leaderboard_dungeon(_serverInstance)