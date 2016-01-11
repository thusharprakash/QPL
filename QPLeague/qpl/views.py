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
    highscorer = Player.objects.filter().order_by('-goals')[0]
    last_game = Fixture.objects.filter(date__lt = datetime.now())[::-1][0]
    context = {
                "top": highscorer,
                "last_game":last_game,
                "difference":abs(last_game.goal1 - last_game.goal2)
            }
    return render(request, 'qpl/index.html', context)

def details(request,name):
    try:
        player = Player.objects.get(name=name)
        context = {
                "player":player,
                }
        return render(request,'qpl/details.html',context)
    except Exception:
        raise Http404("Player Does not exist ")
def teams(request,name):
    try:
        team = Team.objects.get(name=name)
        players = Player.objects.filter(team=team)
        context = { 'team':team, 'players':players}
        return render(request, 'qpl/teams.html', context)
    except Exception:
        raise Http404("Team Not Found")

