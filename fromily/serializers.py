from fromily.models import DiscordUser, DiscordServer, UserServerData
from rest_framework import serializers

class DiscordServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscordServer
        fields = ('id', 'server_str', 'dictator')

class DiscordUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscordUser
        fields = ('id', 'user_str')

