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

    """
    update_server tests
    """
    def test_update_serverdata_user_exists(self):
        data = {}
        data['user'] = {}
        data['user']['id'] = 0
        data['user']['user_str'] = "user0"
        data['dpoints'] = 100

        user = DiscordUser.objects.get(id=data['user']['id'])
        server = DiscordServer.objects.get(id=0)
        userdata = UserServerData.objects.get(user=user,server=server)

        self.assertEquals(userdata.dpoints,0)

        server.update_userdata(data)

        userdata.refresh_from_db()
        self.assertEquals(userdata.dpoints,data['dpoints'])

    def test_update_serverdata_no_user(self):
        data = {}
        data['user'] = {}
        data['user']['id'] = 1
        data['user']['user_str'] = "user0"
        data['dpoints'] = 100

        server = DiscordServer.objects.get(id=0)

        # Check to see that user doesn't exist
        self.assertEquals(DiscordUser.objects.filter(id=data['user']['id']).count(),0)

        self.assertEquals(UserServerData.objects.filter(server=server).count(),1)

        server.update_userdata(data)

        # See that user is created
        self.assertEquals(DiscordUser.objects.filter(id=data['user']['id']).count(),1)
        # See that userdata is created
        self.assertEquals(UserServerData.objects.filter(server=server).count(),2)

        user = DiscordUser.objects.get(id=data['user']['id'])
        userdata = UserServerData.objects.get(user=user,server=server)

        self.assertEquals(userdata.dpoints, data['dpoints'])
