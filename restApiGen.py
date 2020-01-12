import os
import json
from wikipediaapi import Wikipedia
from footballData import footballData 

class Post:
    def __init__(self, team_names='', team_colors='',
                 team1_players='', team2_players='',
                 options='', header='', question='',
                 twTags=''):
        if team_names == '' or team_colors == '' or team1_players == '' or team2_players == '':
            return

        if options == '' or header == '' or question == '':
            return

        self.listitems = list(options)
        self.header = str(header)
        self.question = str(question)
        self.wiki = Wikipedia('en')
        self.team_names = list(team_names)
        self.team_colors = list(team_colors)
        self.team1_players = list(team1_players)
        self.team2_players = list(team2_players)
        self.twTags = list(twTags)

    def getWikiUrl(self, player_name=''):
        if player_name == '':
            return None

        page_py = self.wiki.page(player_name)
        if page_py.exists() is False:
            return None

        return page_py.fullurl

    @staticmethod
    def tag(name, *content, style=None, href=None, **attrs):
        if style is not None:
            attrs['style'] = style

        if href is not None:
            attrs['href'] = href

        if attrs:
            attr_str = ''.join(' %s="%s"' % (attr, value)
                               for attr, value
                               in sorted(attrs.items()))
        else:
            attr_str = ""

        if content:
            return '\n'.join('<%s%s>%s</%s>' %
                             (name, attr_str, c, name) for c in content)
        else:
            return '<%s%s />' % (name, attr_str)

    def formatApi(self):
        http_part = "http --auth : --form POST http://www.tactification.com/api_rt/v1.0/new_post "
        question_tag = self.tag('div', self.question, style='color:black')
        br1 = self.tag('br')

        li_items = str()
        for item in self.listitems:
            li_items += ''.join(self.tag('li', item))

        ul = self.tag('ul', li_items)
        div1 = self.tag('div', ul, style='color:black')

        starring_tag = self.tag('div', "Starring:", style='color:black')

        team1_url = self.getWikiUrl(self.team_names[0])
        if team1_url is None:
            print('wiki url not found', self.team_names[0])
            return

        a_team1 = self.tag('a', self.team_names[0], href=team1_url) + ': '
        a_items = str()
        for item in self.team1_players:
            print(item)
            player_url = self.getWikiUrl(item[0])
            if player_url is None:
                print(item)
                continue 

            a_items += ''.join(self.tag('a', item[0], href=player_url) + '(' + str(item[1]) + '),')

        a_items.rstrip(',')

        i_team1 = self.tag('i', a_team1+a_items, style="color:" + str(self.team_colors[0]))
        team1_div = self.tag('div', i_team1, style='color:black')
       #team1_div = ""

        team2_url = self.getWikiUrl(self.team_names[1])
        if team2_url is None:
            print('wiki url not found', self.team_names[1])
            return

        a_team2 = self.tag('a', self.team_names[1], href=team2_url) + ': '
        a_items = str()
        for item in self.team2_players:
            print(item)
            player_url = self.getWikiUrl(item[0])
            if player_url is None:
                print(item)
                continue 

            a_items += ''.join(self.tag('a', item[0], href=player_url) + '(' + str(item[1]) + '),')

        a_items.rstrip(',')

        i_team2 = self.tag('i', a_team2+a_items, style="color:" + str(self.team_colors[1]))
        
        team2_div = self.tag('div', i_team2, style='color:black')
        #team2_div = ""
        header = " header={!r} ".format(self.header)
        twTag = (" twTag='{}, {}, {}' ".format(*self.twTags))
        end_part = "tactical_gif@home_img.jpg tactical_pic_1750@with_help_msg.jpg tactical_pic_1575@with_help_msg_75.jpg tactical_pic_875@with_help_msg_50.jpg"
        final_command = http_part + "body='" + question_tag + br1 + div1 + starring_tag + team1_div + br1 + team2_div + "'" + header + twTag + end_part
        final_command = http_part + "body='" + question_tag + br1 + div1 + "'" + header + twTag + end_part
        print(final_command)

if __name__ == "__main__":
    apiKey = os.getenv('FOOTBALL_DATA')
    with open('teamList.json', 'r') as f:
        team_dict = json.load(f)

    team1Name = team_dict[0]['teamName'] 
    team1Color = team_dict[0]['teamColor'] 
    team2Name = team_dict[1]['teamName'] 
    team2Color = team_dict[1]['teamColor'] 
    team1 = footballData(apiKey, team1Name, team1Color)
    team2 = footballData(apiKey, team2Name, team2Color)
    teamObjs = [team1, team2]

    competitions = team1.getJson('/v2/competitions/')
    print('======================================================')
    for comp in competitions['competitions']:
        if comp['plan'] == 'TIER_ONE':
            print('competition: {:s} id: {:d}'.format(comp['name'], comp['id']))

    competitionId = int(input('Enter competition Id:'))

    teamUrl = '/v2/competitions/{:d}/teams'.format(competitionId)
    teams = team1.getJson(teamUrl)
    print('======================================================')
    for team in teams['teams']:
        print('team name:{:s} team id:{:d}'.format(team['name'], team['id']))

    for i in range(2):
        jerseyNo = list()
        positionNo = list()
        teamId = int(input('team id for team: ' + str(i + 1)))

        teamUrl = '/v2/teams/{:d}'.format(teamId)
        squad = teamObjs[i].getJson(teamUrl)
        print('==========', squad['squad'])
        teamObjs[i].getPlayerTuple(squad['squad'], team_dict[i]['jerseyNo'], team_dict[i]['positionNo'])

    teams = [team1.teamName, team2.teamName]
    team_colors = [team1.teamColor, team2.teamColor]
    team1_players = team1.squadName
    print('team1:', team1.squadName)
    team2_players = team2.squadName
    print('team2:', team2.squadName)
    question = 'Here is a sequence of play from Germans game against Mexico. #6 and #8 of mexico dragged by Germans #8 and #7 when we see top and bottom pictures. How Mexican defense had to position themselves to prevent #6 receiving from #2?' 
    options = ['']
    header = "Ft: Germany vs Mexico"
    twTags = ['football', 'germany', 'mexico']
    obj = Post(team_names=teams, team_colors=team_colors, team1_players=team1_players, team2_players=team2_players, options=options, header=header, question=question, twTags=twTags)
    obj.formatApi()

