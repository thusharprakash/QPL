from django.shortcuts import render
from django.http import Http404
from models import Fixture, Player, Team
from datetime import datetime, timedelta
# Create your views here.
def fixtures(request):
    fixes = Fixture.objects.all()
    template ='qpl/fixture.html'
    context = {
                "fix":fixes,
                }
    return render(request,template,context)

def index(request):
    # highscorer = Player.objects.filter().order_by('-goals')[0]
    # last_game = Fixture.objects.filter(date__lt = datetime.now())[::-1][0]
    # context = {
    #             "top": highscorer,
    #             "last_game":last_game,
    #             "difference":abs(last_game.goal1 - last_game.goal2)
    #         }
    return render(request, 'qpl/index.html', {})

def indx(request):
    highscorer = Player.objects.filter().order_by('-goals')[0]
    last_game = Fixture.objects.filter(date__lt = datetime.now())[::-1][0]
    context = {
                "top": highscorer,
                "last_game":last_game,
                "difference":abs(last_game.goal1 - last_game.goal2)
            }
    return render(request, 'qpl/indx.html', context)

def details(request,name):
    try:
        player = Player.objects.get(id=name)
        context = {
                "player":player,
                }
        return render(request,'qpl/details.html',context)
    except Exception:
        raise Http404("Player Does not exist ")
def teams(request,name):
    try:
        team = Team.objects.get(id=name)
        players = Player.objects.filter(team=team)
        context = { 'team':team, 'players':players}
        return render(request, 'qpl/teams.html', context)
    except Exception:
        raise Http404("Team Not Found")
#class Standing:
#    
#    def calculate_points(self):
#        self.points = games_won * 1
#
#    def __init__(self,**kwargs):
#        for key in kwargs:
#            self.
#        self.team = team
#        self.games_played = GP
#        self.games_won = GW
#        self.games_defeated = GD
#        self.goals_attained = GA
#        self.goals_lost = GL
#        calculate_points()
#

def standings(request):
    try:
        stands = []
        fixtures = Fixture.objects.all()
        teams = Team.objects.all()
        for team in teams:
            local = {'team':team,'GP':0,'GW':0,'GD':0,'GA':0,'GL':0,}
            for fixture in fixtures:
                if team == fixture.team1:
                    local['GP'] +=1
                    if fixture.goal1 > fixture.goal2:
                        local['GW'] += 1
                        local['GA'] += fixture.goal1
                        local['GL'] += fixture.goal2
                    elif fixture.goal1 < fixture.goal2:
                        local['GD'] += 1
                        local['GA'] += fixture.goal1
                        local['GL'] += fixture.goal2
                    else:
                        print 'Game is a draw'
                elif team == fixture.team2:
                    local['GP'] +=1
                    if fixture.goal2 > fixture.goal1:
                        local['GW'] += 1
                        local['GA'] += fixture.goal2
                        local['GL'] += fixture.goal1
                    elif fixture.goal2 < fixture.goal1:
                        local['GD'] += 1
                        local['GA'] += fixture.goal2
                        local['GL'] += fixture.goal1
                    else:
                        print 'Game is a draw'
                else:
                    pass
            local['P'] = local['GW'] * 1
            local['diff'] = local['GA'] - local['GL']
            stands.append(local)
        
        sorted_stands = sorted(stands, key=lambda k: (k['P'],k['diff']),reverse=True) 
        context = {
                        'standings_list' : sorted_stands,
                        }
        return render(request, 'qpl/standings.html', context)         
    except Exception as e:
        raise Http404("Standings error" + str(e))
