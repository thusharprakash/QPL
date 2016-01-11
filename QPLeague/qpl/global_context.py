from models import Team

def get_teams(request):
    teams = Team.objects.all()
    return {'teams_all':teams}
