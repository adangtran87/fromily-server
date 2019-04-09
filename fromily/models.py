from django.db import models

# Create your models here.
class DiscordUser(models.Model):
    # Should match discord ID
    id = models.BigIntegerField(primary_key=True)
    user_str = models.CharField(max_length=100)

    def __str__(self):
        return"{}:{}".format(self.user_str, self.id)

class DiscordServer (models.Model):
    # Matches discord server ID
    id = models.BigIntegerField(primary_key=True)
    server_str = models.CharField(max_length=100)

    # Dictator fields
    dictator = models.OneToOneField(DiscordUser, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "{}:{}".format(self.server_str, self.id)

    def update_userdata(self, data):
        """
        For a given server, update a user's data
        """
        try:
            user = DiscordUser.objects.get(id=data['user']['id'])
        except DiscordUser.DoesNotExist:
            # Create user
            user = DiscordUser(**data['user'])
            user.save()

        try:
            userdata = UserServerData.objects.get(user=user,server=self)
        except UserServerData.DoesNotExist:
            userdata = UserServerData(user=user, server=self)
        userdata.dpoints = data['dpoints']
        userdata.save()
        return userdata

class UserServerData(models.Model):
    user = models.ForeignKey(DiscordUser, on_delete=models.CASCADE, related_name='serverdata')
    server = models.ForeignKey(DiscordServer, on_delete=models.CASCADE, related_name='userdata')

    # Dictator fields
    dpoints = models.IntegerField(default=0)

    class Meta:
        unique_together = ("user", "server")
