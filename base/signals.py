from django.contrib.auth.models import User
from django.db.models.signals import pre_save


def update_user(sender, instance, **kwargs):
    print('-------------------------------signal triggered')


pre_save.connect(update_user, sender=User)
