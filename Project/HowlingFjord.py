# Project Howling Fjord
# Authors: Jake and Iliya
# A World of Warcraft Mythic Plus Analytics Tool

import requests
import json
import datetime
import io

class Grimoire(object):
    def __init__(self,data):
        self.__dict__ = json.loads(data)

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

    #input_file.close

if __name__ == '__main__':
    _serverInstance = Server
    _serverInstance.api_key = import_key("../ApiKeys/apikey.txt")
    _serverInstance.access_token = import_key("../ApiKeys/access_token.txt")
    _serverInstance.locale = "us"

    _realm_dict = {}

    #realm_index_outfile = open("realm_index.json", "w")
    out_file = open("realms.json","w")
    out_file2 = open("dungeons.json", "w")
    out_file3 = open("classes.json", "w")

    _realm_index_json = _serverInstance.get_realm_index(_serverInstance)

    write_json("realm_index.json", _realm_index_json)

    _parsed_realm_index_json = json.loads(_realm_index_json)

    for _realms_index in _parsed_realm_index_json['realms']:
        _realm_dict[_realms_index['name']] = _realms_index['slug']
        #print ("Realm Name: %s, Realm Slug: %s" % (_realms_index['name'], _realms_index['slug']))

    #print(_parsed_realm_index_json["realms"][50]["slug"])

    #parse realm index and get the realm_slug, you need to set _serverInstance.realm_slug

    print ("List of realms: \n")

    for _realm_key in _realm_dict:
        print (_realm_key)

    print()

    try:
        _user_input_realm = input("What realm do you want to access?")

        print ("User input realm %s" % _realm_dict[_user_input_realm])

        # Set this
        _serverInstance.realm_slug = _realm_dict[_user_input_realm]

        _realm_json = _serverInstance.get_realm(_serverInstance)

        _realm = json.loads(_realm_json)

        json.dump(_realm, out_file, sort_keys = True,indent=4)

        out_file.close

        # String slicer is awesome
        _local_connected_realm_id = (_realm['connected_realm']['href'])[51:-21]

        print (_local_connected_realm_id)

    except:

        print ("Cannot find input specified")

    # Iliya's commented code
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
    # # Set these
    # _serverInstance.dungeon_id = ''
    # _serverInstance.period = ''
    #
    # _mythic_leaderboard_dungeon_json = _serverInstance.get_mythic_leaderboard_dungeon(_serverInstance)
    #
    # print(_mythic_leaderboard_dungeon_json)

    #some additional code jake:
    # write_json("realm_json.joined", _realm_json)

    # # Set this
    # _serverInstance.realm_id = '3684'
    #
    # _mythic_leaderboard_index_json = _serverInstance.get_mythic_leaderboard_index(_serverInstance)
    #
    # write_json("mythic_leaderboard_index_json.joined", _mythic_leaderboard_index_json)
    #
    # # Set these
    # _serverInstance.dungeon_id = '199'
    # _serverInstance.period = '632'
    #
    # _mythic_leaderboard_dungeon_json = _serverInstance.get_mythic_leaderboard_dungeon(_serverInstance)
    #
    # write_json("mythic_leaderboard_dungeon_json.joined", _mythic_leaderboard_dungeon_json)
    #
    # _epoch = (1518533999000)
    #
    # _converted_timestamp = convert_epoch(_epoch)