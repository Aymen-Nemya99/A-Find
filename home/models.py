from pyexpat import model
from django.db import models
from django.db.models.fields import AutoField
from datetime import  datetime,date

# Create your models here.

class Task(models.Model):
    TaskTitle = models.CharField(max_length=20)
    TaskDesc = models.TextField()
    time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.TaskTitle
class Patien(models.Model):
    PatId = models.BigAutoField(primary_key=True, null=False , blank=True)
    PatNom = models.TextField()
    PatPrenom = models.TextField()
    PatNais = models.DateField( auto_now=False, auto_now_add=False)

    objects = models.Manager()

    def __str__(self):
        return     " {}".format(self.PatId) + "  " + self.PatNom + " {} ".format(self.PatNais) 


class User(models.Model):
    UserId = models.BigAutoField(primary_key=True, null=False , blank=True)
    UserNom = models.TextField()
    UserPass = models.CharField(max_length=20,default='')
    is_active = models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.UserNom

    con_objet = models.Manager()


class Cluster(models.Model):
    ID = models.BigAutoField(primary_key=True, null=False , blank=True)
    Username = models.TextField()
    Tweet = models.TextField()
    Retweet = models.BigIntegerField()
    Cluster = models.BigIntegerField()

    objects = models.Manager()

    def __str__(self):
        return     " {}".format(self.ID) + "  " + self.Username 
