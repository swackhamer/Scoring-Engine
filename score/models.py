from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=20)
    dns_server = models.IPAddressField()
    def __unicode__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=20)
    address = models.IPAddressField()
    status = models.CharField(max_length=20)
    team_name = models.ForeignKey(Team)
    
    def __unicode__(self):
        return self.name
# Create your models here.
