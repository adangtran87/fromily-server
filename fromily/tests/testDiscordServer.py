from django.test import TestCase
from fromily.models import DiscordServer, DiscordUser, UserServerData

class DiscordServerTest(TestCase):
    def setUp(self):
        user = DiscordUser(id=0, user_str='user0')
        user.save()
        server = DiscordServer(id=0, server_str='server0')
        server.save()
        UserServerData.objects.create(user=user,server=server)
        return

    def tearDown(self):
        return

