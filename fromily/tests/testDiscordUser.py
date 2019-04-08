from django.test import TestCase
from fromily.models import DiscordServer, DiscordUser, UserServerData

class DiscordUserTest(TestCase):
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
    Tests the update_serverdata method

    Expects the following data structure
    data['server'] = bigInt
    data['dpoints'] = dpoints
    """
    def test_update_serverdata_server_exists(self):
        data = {}
        data['server'] = 0
        data['dpoints'] = 100

        user = DiscordUser.objects.get(id=0)
        server = DiscordServer.objects.get(id=data['server'])
        userdata = UserServerData.objects.get(user=user,server=server)

        self.assertEquals(userdata.dpoints,0)

        self.assertTrue(user.update_serverdata(data))

        userdata.refresh_from_db()
        self.assertEquals(userdata.dpoints,data['dpoints'])

    def test_update_serverdata_no_server(self):
        data = {}
        data['server'] = 1
        data['dpoints'] = 100

        user = DiscordUser.objects.get(id=0)
        self.assertFalse(user.update_serverdata(data))

    def test_update_serverdata_create_userdata(self):
        data = {}
        data['server'] = 1
        data['dpoints'] = 100

        user = DiscordUser.objects.get(id=0)
        server = DiscordServer(id=1, server_str='server1')
        server.save()
        userdataCount = UserServerData.objects.count()

        self.assertEquals(UserServerData.objects.filter(server=server).count(),0)

        self.assertTrue(user.update_serverdata(data))
        self.assertEquals(UserServerData.objects.filter(server=server).count(),1)
        userdata = UserServerData.objects.get(user=user,server=server)
        self.assertEquals(userdata.dpoints,data['dpoints'])
