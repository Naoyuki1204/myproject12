from django.db import models

class game(models.Model):
    gamename = models.CharField(max_length=100)
    score = models.CharField(max_length=100)
    keioS = models.CharField(max_length=100)
    keioV = models.CharField(max_length=100)
    eS = models.CharField(max_length=100)
    eV = models.CharField(max_length=100)
    eteam = models.CharField(max_length=100)
    date = models.DateField()
     
    def __str__(self):
        return '<game:id=' + str(self.id) + ', ' + \
            self.gamename + '(' + str(self.score) + ')>'

class result(models.Model):
    gameid = models.IntegerField()
    pname = models.CharField(max_length=100)
    placeS = models.IntegerField()
    placeF = models.IntegerField()
    skill = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    count = models.CharField(max_length=100)
    def __str__(self):
          return str(self.pname) + str(self.result)
    

class before(models.Model):
    gameid = models.IntegerField()
    pname = models.CharField(max_length=100)
    placeS = models.IntegerField()
    placeF = models.IntegerField()
    skill = models.CharField(max_length=100)


class player(models.Model):
    pname = models.CharField(max_length=100)
    pname2 = models.CharField(max_length=100)
    hand = models.CharField(max_length=100)
    pos = models.CharField(max_length=100)
    def __str__(self):
          return str(self.pname) + str(self.pname2)