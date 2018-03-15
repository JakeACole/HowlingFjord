# Project Howling Fjord
# Authors: Jake and Iliya
# A World of Warcraft Mythic Plus Analytics Tool

import requests
import json

class Test(object):
    def __init__(self,data):
        self.__dict__ = json.loads(data)

class Server:
    def __init__(self):
        self.locale = ''
        self.access_token = ''
        self.api_key = ''

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

        #print (self.realm_index_url + "\n")

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

        #print (self.mythic_leaderboard_index_url + "\n")

        _data = requests.get(self.mythic_leaderboard_index_url).text

        #print (data)

        return _data

    def get_mythic_leaderboard_dungeon(self):
        #https://us.api.battle.net/data/wow/connected-realm/78/mythic-leaderboard/197/period/630?namespace=dynamic-us&locale=en_US&access_token= + self.access_token

        self.mythic_leaderboard_dungeon_url = "https://" + self.locale + \
              ".api.battle.net/data/wow/connected-realm/" + self.realm_id + \
              "/mythic-leaderboard/" + self.dungeon_id + "/period/" + self.period + "?namespace=dynamic-us&locale=en_US&access_token=" + self.access_token

        #https://us.api.battle.net/data/wow/connected-realm/?namespace=dynamic-us&locale=en_US&access_token=access_token

        #print (self.mythic_leaderboard_dungeon_url + "\n")

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
    _serverInstance.api_key = import_key("../ApiKeys/apikey.txt")
    _serverInstance.access_token = import_key("../ApiKeys/access_token.txt")
    _serverInstance.locale = "us"

    #_realm_index_json = _serverInstance.get_realm_index(_serverInstance)

    out_file = open("realms.json","w")
    out_file2 = open("dungeons.json", "w")
    out_file3 = open("classes.json", "w")

    #parse realm index and get the realm_slug, you need to set _serverInstance.realm_slug

    # Set this
    _serverInstance.realm_slug = 'malganis'

    _realm__json = _serverInstance.get_realm(_serverInstance)

    realm = json.loads(_realm__json)

    json.dump(realm, out_file,sort_keys = True,indent=4)

    out_file.close

    print(realm['id'])

    # test1 = Test(_realm__json)
    #
    # x = test1.connected_realm['href']
    #
    # print(x)
    #
    # # Set this
    # #_serverInstance.realm_id = x
    #
    # _mythic_leaderboard_index_json = _serverInstance.get_mythic_leaderboard_index(x)
    #
    # dungeons = json.loads(_mythic_leaderboard_index_json)
    #
    # json.dump(dungeons,out_file2, sort_keys = True,indent =4)
    #
    #
    #
    #
    # # Set these
    # _serverInstance.dungeon_id = ''
    # _serverInstance.period = ''
    #
    # _mythic_leaderboard_dungeon_json = _serverInstance.get_mythic_leaderboard_dungeon(_serverInstance)
    #
    # print(_mythic_leaderboard_dungeon_json)
