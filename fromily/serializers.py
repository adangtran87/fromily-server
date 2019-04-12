from fromily.models import DiscordUser, DiscordServer, UserServerData, DPointRecord
from rest_framework import serializers

class DPointRecordSerializer(serializers.ModelSerializer):
    date = serializers.DateField(read_only=True)
    class Meta:
        model = DPointRecord
        fields = ('points', 'reason', 'date')

class UserServerDataSummarySerializer(serializers.ModelSerializer):
    dpoints = serializers.SerializerMethodField()

    class Meta:
        model = UserServerData
        fields = ('user', 'server', 'dpoints')

    def get_dpoints(self, obj):
        return obj.get_dpoints()

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

class DiscordUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscordUser
        fields = ('id', 'name')

class ServerViewUserDataSerializer(serializers.ModelSerializer):
    user = DiscordUserSerializer()
    class Meta:
        model = UserServerData
        fields = ('user',)

class DiscordServerSerializer(serializers.ModelSerializer):
    userdata = ServerViewUserDataSerializer(many=True, required=False)
    class Meta:
        model = DiscordServer
        fields = ('id', 'name', 'dictator', 'userdata')

