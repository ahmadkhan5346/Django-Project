from account.models import ProfileImage
from account.models import User
from django.db.models.signals import post_save


def create_profile(sender, **kwargs):
    if kwargs['created']:
        ProfileImage.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=User)