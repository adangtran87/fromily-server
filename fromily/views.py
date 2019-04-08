from fromily.models import DiscordUser, DiscordServer, UserServerData
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from fromily.serializers import DiscordServerSerializer, DiscordUserSerializer, UserDataSerializer
# Create your views here.

class DiscordUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Discord Users to be viewed
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = DiscordUser.objects.all()
    serializer_class = DiscordUserSerializer

    @action(detail=True, methods=['get','post'], permission_classes=[IsAuthenticatedOrReadOnly])
    def userdata(self, request, pk=None):
        user = self.get_object()
        if request.method == 'GET':
            userdata = UserServerData.objects.filter(user=user)
            serializer = UserDataSerializer(userdata, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            print(request.data)
            serializer = UserDataSerializer(data=request.data)
            if serializer.is_valid():
                if user.update_userdata(serializer.data):
                    return Response(serializer.data)
                else:
                    return Reponse({'status': 'server does not exist'})
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)

class DiscordServerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Discord Servers to be viewed
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = DiscordServer.objects.all()
    serializer_class = DiscordServerSerializer

