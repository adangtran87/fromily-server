from fromily.models import DiscordUser, DiscordServer, UserServerData
from rest_framework import serializers

class UserServerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserServerData
        fields = ('user', 'server', 'dpoints')

class UserViewServerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserServerData
        fields = ('server', 'dpoints')

class ServerViewUserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserServerData
        fields = ('user', 'dpoints')

class DiscordServerSerializer(serializers.ModelSerializer):
    userdata = ServerViewUserDataSerializer(many=True, required=False)
    class Meta:
        model = DiscordServer
        fields = ('id', 'server_str', 'dictator', 'serverdata')

class DiscordUserSerializer(serializers.ModelSerializer):
    serverdata  = UserViewServerDataSerializer(many=True, required=False)
    class Meta:
        model = DiscordUser
        fields = ('id', 'user_str', 'userdata')

