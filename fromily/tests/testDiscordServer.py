from django.test import TestCase
from fromily.models import DiscordServer, DiscordUser, UserServerData

class DiscordServerTest(TestCase):
    def setUp(self):
        user = DiscordUser(id=0, name='user0')
        user.save()
        server = DiscordServer(id=0, name='server0')
        server.save()
        UserServerData.objects.create(user=user,server=server)
        return

    def tearDown(self):
        return

