from fromily.models import DiscordUser, DiscordServer, UserServerData, DPointRecord
from rest_framework import serializers

class DPointRecordSerializer(serializers.ModelSerializer):
    date = serializers.DateField(read_only=True)
    class Meta:
        model = DPointRecord
        fields = ('points', 'reason', 'date')

class UserServerDataSerializer(serializers.ModelSerializer):
    # dpoints = serializers.IntegerField()
    class Meta:
        model = UserServerData
        # fields = ('user', 'server', 'dpoints')
        fields = ('user', 'server')

class UserViewServerDataSerializer(serializers.ModelSerializer):
    dpoints = serializers.IntegerField()
    class Meta:
        model = UserServerData
        fields = ('server', 'dpoints')

class ServerViewUserDataSerializer(serializers.ModelSerializer):
    dpoints = serializers.IntegerField()
    class Meta:
        model = UserServerData
        fields = ('user', 'dpoints')

class DiscordServerSerializer(serializers.ModelSerializer):
    # userdata = ServerViewUserDataSerializer(many=True, required=False)
    class Meta:
        model = DiscordServer
        # fields = ('id', 'name', 'dictator', 'userdata')
        fields = ('id', 'name', 'dictator')

class DiscordUserSerializer(serializers.ModelSerializer):
    # serverdata  = UserViewServerDataSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = DiscordUser
        # fields = ('id', 'name', 'serverdata')
        fields = ('id', 'name')

