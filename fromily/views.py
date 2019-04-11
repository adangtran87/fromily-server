from fromily.models import DiscordUser, DiscordServer, UserServerData, DPointRecord
from rest_framework import exceptions, status, viewsets
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

    def get_queryset(self):
        queryset = UserServerData.objects.all()
        user = self.request.query_params.get('user', None)
        server = self.request.query_params.get('server', None)
        if user and server:
            queryset = queryset.filter(user=user,server=server)
        elif user:
            queryset = queryset.filter(user=user)
        elif server:
            queryset = queryset.filter(server=server)
        return queryset


class DPointRecordViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = DPointRecord.objects.all()
    serializer_class = DPointRecordSerializer

    def _get_userserverdata(self):
        user = self.request.query_params.get('user', None)
        server = self.request.query_params.get('server', None)
        if not user or not server:
            raise exceptions.NotFound(r'Provide user id and server id as query: ?user=id&server=id')

        try:
            userserverdata = UserServerData.objects.get(user=user, server=server)
        except UserServerData.DoesNotExist:
            raise exceptions.NotFound("UserServerData does not exist for user:{} and server:{}".format(user,server))

        return userserverdata

    def get_queryset(self):
        """
        When requesting this view a user and server id must be provided
        otherwise return 404 Not Found
        """
        userserverdata = self._get_userserverdata()
        queryset = DPointRecord.objects.filter(userserverdata=userserverdata)
        return queryset

    def perform_create(self, serializer):
        userserverdata = self._get_userserverdata()
        serializer.save(userserverdata=userserverdata)
