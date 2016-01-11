from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Designation(models.Model):
    desig = models.CharField(max_length=200)

    def __unicode__(self):
        return self.desig

class Team(models.Model):
    logo = models.FileField(upload_to='images')
    name = models.CharField(max_length=200)


    def __unicode__(self):
        return self.name

class Fixture(models.Model):
    team1 = models.ForeignKey(Team,related_name="first_team")
    team2 = models.ForeignKey(Team, related_name="second_team")
    goal1 = models.IntegerField(default=0)
    goal2 = models.IntegerField(default=0)
    date = models.DateTimeField()
    
    def __unicode__(self):
        return self.team1.name + " Vs " + self.team2.name


class Player(models.Model):
    name = models.CharField(max_length=200)
    goals = models.IntegerField(default=0)
    team = models.ForeignKey(Team)
    image = models.FileField(upload_to='images')
    designation = models.ForeignKey(Designation)
    is_captain = models.BooleanField(default=False)

    def __unicode__(self):
        if self.is_captain:
            return '[Captain] '+ self.name
        else:
            return self.name

class Goal(models.Model):
    player = models.ForeignKey(Player, related_name="goaling_player")
    time = models.TimeField()
    assist = models.ForeignKey(Player, related_name="goal_assist_player")
    fixture = models.ForeignKey(Fixture)
    team = models.ForeignKey(Team)

    def __unicode__(self):
        return self.player.name + " @ " + str(self.fixture)
