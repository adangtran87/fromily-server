from fromily.models import DiscordUser, DiscordServer, UserServerData
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from fromily.serializers import DiscordServerSerializer, DiscordUserSerializer
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

