from fromily.models import DiscordUser, DiscordServer, UserServerData
from rest_framework import serializers

class DiscordUserBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscordUser
        fields = ('id', 'user_str')

class DiscordUserCustomSerializer(serializers.Serializer):
    """
    Do not validate user id for uniqueness
    """
    id = serializers.IntegerField()
    user_str = serializers.CharField(max_length=100)

class DiscordServerBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscordServer
        fields = ('id', 'server_str')

class UserServerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserServerData
        fields = ('user', 'server', 'dpoints')

class UserViewServerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserServerData
        fields = ('server', 'dpoints')

class ServerViewUserDataSerializer(serializers.ModelSerializer):
    user = DiscordUserCustomSerializer()
    class Meta:
        model = UserServerData
        fields = ('user', 'dpoints')

class DiscordServerSerializer(serializers.ModelSerializer):
    userdata = ServerViewUserDataSerializer(many=True, required=False)
    class Meta:
        model = DiscordServer
        fields = ('id', 'server_str', 'dictator', 'userdata')

class DiscordUserSerializer(serializers.ModelSerializer):
    serverdata  = UserViewServerDataSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = DiscordUser
        fields = ('id', 'user_str', 'serverdata')

