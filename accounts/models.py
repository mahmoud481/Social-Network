from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# class Profile(models.Model):
#     GENDER = (
#         ("male", "male"),
#         ("female", "female"),
#     )
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     gender = models.CharField(max_length=10, choices=GENDER, default="male")
#     date_of_birth = models.DateField(null=True, blank=True)
#
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
