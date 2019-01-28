from django.shortcuts import render
from rest_framework import viewsets
from apps.myapp.serializers import DtSerializer, TmpSerializer, HmdSerializer, RoomSerializer, DoorSerializer, ModeSerializer, StateSerializer
import requests
import json
from .models import *


# Create your views here.
class DtViewSet(viewsets.ModelViewSet):
    queryset = Dt.objects.all()
    serializer_class = DtSerializer


class TmpViewSet(viewsets.ModelViewSet):
    queryset = Tmp.objects.all()
    serializer_class = TmpSerializer


class HmdViewSet(viewsets.ModelViewSet):
    queryset = Hmd.objects.all()
    serializer_class = HmdSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class DoorViewSet(viewsets.ModelViewSet):
    queryset = Door.objects.all()
    serializer_class = DoorSerializer


class ModeViewSet(viewsets.ModelViewSet):
    queryset = Mode.objects.all()
    serializer_class = ModeSerializer


class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer


def rasp(request):
    locData = LocationData.objects.order_by('-id')[0]
    lat = locData.latitude
    lon = locData.longitude
    out = ''

    # currentstate = 'off'
    # currentmode = 'auto'
    dtstate = '2018-10-01T14:00:00-05:00'
    r = requests.get('http://127.0.0.1:8000/iot/rasp/dt/1/')
    result = r.text
    output = json.loads(result)
    dtstate = output['name']

    tmpstate = '20'
    r = requests.get('http://127.0.0.1:8000/iot/rasp/tmp/1/')
    result = r.text
    output = json.loads(result)
    tmpstate = output['name']

    hmdstate = '50'
    r = requests.get('http://127.0.0.1:8000/iot/rasp/hmd/1/')
    result = r.text
    output = json.loads(result)
    hmdstate = output['name']

    roomstate = 'no'
    r = requests.get('http://127.0.0.1:8000/iot/rasp/room/1/')
    result = r.text
    output = json.loads(result)
    roomstate = output['name']

    doorstate = 'closed'
    r = requests.get('http://127.0.0.1:8000/iot/rasp/door/1/')
    result = r.text
    output = json.loads(result)
    doorstate = output['name']

    r = requests.get('http://127.0.0.1:8000/iot/rasp/mode/1/')
    result = r.text
    output = json.loads(result)
    currentmode = output['name']

    r = requests.get('http://127.0.0.1:8000/iot/rasp/state/1/')
    result = r.text
    output = json.loads(result)
    currentstate = output['name']


    if 'on' in request.POST:
        values = {"name": "on"}
        r = requests.put('http://127.0.0.1:8000/iot/rasp/state/1/', data=values)
        result = r.text
        output = json.loads(result)
        out = output['name']
    if 'off' in request.POST:
        values = {"name": "off"}
        r = requests.put('http://127.0.0.1:8000/iot/rasp/state/1/', data=values)
        result = r.text
        output = json.loads(result)
        out = output['name']
    if 'auto' in request.POST:
        values = {"name": "auto"}
        r = requests.put('http://127.0.0.1:8000/iot/rasp/mode/1/', data=values)
        result = r.text
        output = json.loads(result)
        out = output['name']
    if 'manual' in request.POST:
        values = {"name": "manual"}
        r = requests.put('http://127.0.0.1:8000/iot/rasp/mode/1/', data=values)
        result = r.text
        output = json.loads(result)
        out = output['name']


    return render(request, 'rasp.html', {'lat': lat, 'lon': lon, 'dtstate': dtstate, 'tmpstate': tmpstate,
                                        'hmdstate': hmdstate, 'roomstate': roomstate, 'doorstate': doorstate, 'name': out,
                                        'currentmode': currentmode, 'currentstate': currentstate})
