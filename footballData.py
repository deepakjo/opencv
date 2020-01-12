import http.client
import json

class footballData:
    def __init__(self, apiKey, teamName, teamColor):
        self.apiKey = apiKey
        self.teamName = teamName
        self.teamColor = teamColor
        self.connection = http.client.HTTPConnection('api.football-data.org')
        self.headers = { 'X-Auth-Token': self.apiKey }
        self.squadName = list()

    def getJson(self, url):
        self.connection.request('GET', url, None, self.headers)
        response = json.loads(self.connection.getresponse().read().decode())
        return response 

    def getPlayerTuple(self, squad, jerseyNo, positionNo):
        if isinstance(squad, list) == False:
            return ValueError

        if isinstance(jerseyNo, list) == False:
            return ValueError

        if isinstance(positionNo, list) == False:
            return ValueError

        if len(jerseyNo) != len(positionNo):
            return ValueError

        #team = [player if player['shirtNumber'] != None for player in squad]
        team = list()
        positionList = list()
        jerseyList = list()

        for player in squad:
            if player['shirtNumber'] != None and player['shirtNumber'] in jerseyNo:
                print(player)
                team.append(player)
                positionList.append(positionNo[jerseyNo.index(player['shirtNumber'])])
                jerseyList.append(player['shirtNumber'])

        if len(team) != len(positionList):
            return ValueError

        print('------------------')
        print(positionList, sep='\n')
        print(team, sep='\n')
        self.squadName = [(player['name'], position) for player, position in zip(team, positionList)]
        print(self.squadName, sep='\n')
        return 
