from django.db import models
from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     friends = models.ManyToManyField("self", through='Friendship', related_name='friends')
#     pass


# class Friendship(models.Model):
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
     # = models.ForeignKey(Group, on_delete=models.CASCADE)
    # date_joined = models.DateField(auto_now_add=True)
    # approved = models.BooleanField(default=False)
