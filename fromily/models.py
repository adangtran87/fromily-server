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

class UserServerData(models.Model):
    user = models.ForeignKey(DiscordUser, on_delete=models.CASCADE)
    server = models.ForeignKey(DiscordServer, on_delete=models.CASCADE)

    # Dictator fields
    dpoints = models.IntegerField(default=0)

    class Meta:
        unique_together = ("user", "server")
