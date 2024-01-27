from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True},
        }

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ('id', 'title')

class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = ('id', 'title')
        


class SubEventsSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True)
    game = GamesSerializer()

    class Meta:
        model = SubEvents
        fields = ['id', 'title', 'game', 'description', 'rules', 'participants']

class MainEventsSerializer(serializers.ModelSerializer):
    sub_events = SubEventsSerializer(many=True)

    class Meta:
        model = MainEvent
        fields = ['id', 'title', 'sub_events']