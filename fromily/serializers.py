from fromily.models import DiscordUser, DiscordServer, UserServerData, DPointRecord
from rest_framework import serializers

class DPointRecordSerializer(serializers.ModelSerializer):
    date = serializers.DateField(read_only=True)
    class Meta:
        model = DPointRecord
        fields = ('points', 'reason', 'date')

class UserServerDataSerializer(serializers.ModelSerializer):
    dpoints = serializers.SerializerMethodField()
    dpoint_log = serializers.SerializerMethodField()
    class Meta:
        model = UserServerData
        fields = ('user', 'server', 'dpoints', 'dpoint_log')

    def get_dpoints(self, obj):
        return obj.get_dpoints()

    def get_dpoint_log(self, obj):
        return DPointRecordSerializer(obj.get_dpoint_log(), many=True).data

class UserViewServerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserServerData
        fields = ('server', 'dpoints')

class ServerViewUserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserServerData
        fields = ('user', 'dpoints')

class DiscordServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscordServer
        fields = ('id', 'name', 'dictator')

class DiscordUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscordUser
        fields = ('id', 'name')

