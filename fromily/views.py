from fromily.models import DiscordUser, DiscordServer, UserServerData, DPointRecord
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from fromily.serializers import DiscordServerSerializer, DiscordUserSerializer, UserServerDataSerializer, DPointRecordSerializer
# Create your views here.

class DiscordUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Discord Users to be viewed
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = DiscordUser.objects.all()
    serializer_class = DiscordUserSerializer

class DiscordServerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Discord Servers to be viewed
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = DiscordServer.objects.all()
    serializer_class = DiscordServerSerializer

class UserServerDataViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = UserServerData.objects.all()
    serializer_class = UserServerDataSerializer

class DPointRecordViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = DPointRecord.objects.all()
    serializer_class = DPointRecordSerializer
