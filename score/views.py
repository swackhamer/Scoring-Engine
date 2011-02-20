# Create your views here.
from django.http import HttpResponse
from ccdc.score.models import *
from django.http import Http404
from django.shortcuts import get_object_or_404, render_to_response
import dns_resolver

def index(request):
    html = ''
    services = Service.objects.all()
    sList = []
    for serv in services:
        s = dict()
        s['name'] = serv.name
        s['ip'] = serv.address
        s['ip'] = dns_resolver.get_A_record('192.168.1.2','google.com')
        s['status'] = serv.status
        s['team'] = serv.team_name.name
        sList.append(s)
    

    
    tList = []
    teams = Team.objects.all()
    
    for team in teams:
        t = dict()
        t['name'] = team.name
        tList.append(t)
    return render_to_response('index.html', {'services' : sList, 'teams' : tList})
    