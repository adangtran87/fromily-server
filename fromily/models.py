from django.db import models

# Create your models here.
class DiscordUser(models.Model):
    # Should match discord ID
    id = models.BigIntegerField(primary_key=True)
    user_str = models.CharField(max_length=100)

    def __str__(self):
        return"{}:{}".format(self.user_str, self.id)

    # Expects UserServerData excluding the server
    # Return true if successful
    def update_userdata(self, data):
        try:
            server = DiscordServer.objects.get(id=data['server'])
        except DiscordServer.DoesNotExist:
            return False

        try:
            userdata = UserServerData.objects.get(user=self,server=server)
        except UserServerData.DoesNotExist:
            # Create userdata
            userdata = None
            # create if it doesn't exist
            userdata = UserServerData(user=self,server=server)
        userdata.dpoints = data['dpoints']
        userdata.save()
        return True

class DiscordServer (models.Model):
    # Matches discord server ID
    id = models.BigIntegerField(primary_key=True)
    server_str = models.CharField(max_length=100)

    # Dictator fields
    dictator = models.OneToOneField(DiscordUser, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "{}:{}".format(self.server_str, self.id)

class UserServerData(models.Model):
    user = models.ForeignKey(DiscordUser, on_delete=models.CASCADE, related_name='userdata')
    server = models.ForeignKey(DiscordServer, on_delete=models.CASCADE, related_name='serverdata')

    # Dictator fields
    dpoints = models.IntegerField(default=0)

    class Meta:
        unique_together = ("user", "server")
