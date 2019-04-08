from fromily.models import DiscordUser, DiscordServer, UserServerData
from rest_framework import serializers

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserServerData
        fields = ('server', 'dpoints')

class ServerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserServerData
        fields = ('user', 'dpoints')

class DiscordServerSerializer(serializers.ModelSerializer):
    serverdata = ServerDataSerializer(many=True, required=False)
    class Meta:
        model = DiscordServer
        fields = ('id', 'server_str', 'dictator', 'serverdata')

class DiscordUserSerializer(serializers.ModelSerializer):
    userdata = UserDataSerializer(many=True, required=False)
    class Meta:
        model = DiscordUser
        fields = ('id', 'user_str', 'userdata')

