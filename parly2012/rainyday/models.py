from django.db import models

class Division(models.Model):
    div_no = models.IntegerField()
    date = models.DateField()
    title = models.CharField(max_length=128)

class Constituency(models.Model):
    name = models.CharField(max_length=128)

class Party(models.Model):
    name = models.CharField(max_length=128)
    
class Person(models.Model):
    name = models.CharField(max_length=128)
    party = models.ForeignKey(Party)
    constituency = models.ForeignKey(Constituency)
    area_name = models.CharField(max_length=128)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    age = models.FloatField()

class Vote(models.Model):
    text = models.CharField(max_length=128)
    
class VoteRecord(models.Model):
    person = models.ForeignKey(Person)
    vote = models.ForeignKey(Vote)
    division = models.ForeignKey(Division)
    date = models.DateField()
    rainfall = models.FloatField()
    deferred_vote = models.CharField(max_length=10)

class InstallStatus(models.Model):
    done = models.BooleanField()
    count = models.IntegerField()
    install_type = models.CharField(max_length=20)

