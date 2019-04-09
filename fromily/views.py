from fromily.models import DiscordUser, DiscordServer, UserServerData
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from fromily.serializers import DiscordServerSerializer, DiscordUserSerializer, UserViewServerDataSerializer, ServerViewUserDataSerializer
# Create your views here.

class DiscordUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Discord Users to be viewed
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = DiscordUser.objects.all()
    serializer_class = DiscordUserSerializer

    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticatedOrReadOnly])
    def serverdata(self, request, pk=None):
        user = self.get_object()
        if request.method == 'GET':
            userdata = UserServerData.objects.filter(user=user)
            serializer = UserViewServerDataSerializer(userdata, many=True)
            return Response(serializer.data)

class DiscordServerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Discord Servers to be viewed
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = DiscordServer.objects.all()
    serializer_class = DiscordServerSerializer

    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticatedOrReadOnly])
    def userdata(self, request, pk=None):
        server = self.get_object()
        if request.method == 'GET':
            userdata = UserServerData.objects.filter(server=server)
            serializer = ServerViewUserDataSerializer(userdata, many=True)
            return Response(serializer.data)
