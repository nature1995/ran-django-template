from apps.myapp.models import Dt, Tmp, Hmd, Room, Door, Mode, State
from rest_framework import serializers


class DtSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dt
        fields = ('url', 'name')


class TmpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tmp
        fields = ('url', 'name')


class HmdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hmd
        fields = ('url', 'name')


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('url', 'name')


class DoorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Door
        fields = ('url', 'name')


class ModeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mode
        fields = ('url', 'name')


class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields = ('url', 'name')
