import requests
import json

class Server:
    def __init__(self, locale, realmId):
        self.locale = locale
        self.realmId = "58" #temp #realmId
        self.accessToken
        self.apikey

    def GetRealmId(self, realm_name):
        url = "https://" + self.locale + \
              ".api.battle.net/data/wow/connected-realm/" + \
              "?namespace=dynamic-us&locale=en_US&access_token=" + self.accessToken

        #https://us.api.battle.net/data/wow/connected-realm/?namespace=dynamic-us&locale=en_US&access_token=access_token

        print (url + "\n")

        jsonStuff = requests.get(url).text

        print (jsonStuff)

        #some parsing function to find realm_name in get_realm_id

        #return requests.get(url).text


    def GetCurrentLeaderboards(self):
        """
        Get the list of all current leader boards for each dungeon

        :return: json file with link to each leaderboard for the server
        """
        #url = "https://" + self.locale + \
        #      ".api.battle.net/data/wow/connected-realm/" + self.connected_realm_id + \
        #      "/mythic-leaderboard/?namespace=dynamic-us&locale=en_US&access_token=" + apikey

        url = "https://" + self.locale + \
              ".api.battle.net/data/wow/connected-realm/" + self.realmId + \
              "/mythic-leaderboard/?namespace=dynamic-us&locale=en_US&access_token=" + "74r5yts3vqkedngqztntzecj" #self.access_token

        #url = "https://us.api.battle.net/data/wow/connected-realm/1171/mythic-leaderboard/?namespace=dynamic-us&locale=en_US&apikey=" + apikey

        print (url)
        return requests.get(url).text

def ImportKey(apiKeyFile):
    f = open(apiKeyFile, "r")
    apikey = f.read()
    #print(apikey)
    return apikey

if __name__ == '__main__':
    serverInstance = Server
    serverInstance.apikey = ImportKey("../ApiKeys/apikey.txt")
    serverInstance.accessToken = ImportKey("../ApiKeys/access_token.txt")
    serverInstance.locale = "us"
    rcvdRealmId = serverInstance.GetRealmId(serverInstance, "Mal'Ganis")
    print(rcvdRealmId)

    #serverInstance.realmId = rcvdRealmId
    #apiRequest = serverInstance.GetCurrentLeaderboards(serverInstance)

    #print(apiRequest)