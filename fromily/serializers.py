from fromily.models import DiscordUser, DiscordServer, UserServerData
from rest_framework import serializers

class DiscordServerSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = DiscordServer
        fields = ('id', 'server_str', 'dictator')

class DiscordUserSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = DiscordUser
        fields = ('id', 'user_str')

