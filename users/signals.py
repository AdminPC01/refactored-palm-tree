from .models import User,Profile
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
     if created:
         user=instance
         profile=Profile.objects.create(
             user=user,
             username=user.username,
             name=user.first_name,
             email=user.email
         )
@receiver(post_save,sender=Profile)
def updateAccount(sender,instance,created,**kwargs):
    profile = instance
    user = profile.user

    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


@receiver(post_delete, sender=Profile)
def deleteProfile(sender, instance, **kwargs):
    user = instance.user
    user.delete()


@receiver(post_save, sender=Profile)
def profileUpdated(sender, instance, created, **kwargs):
    print("Updated")
    print(instance)
    print(created)


@receiver(post_delete, sender=Profile)
def deleteUser(sender,instance, **kwargs):
    print("Deleting...")
    print(instance)

# post_save.connect(profileUpdated, sender=Profile)
# post_delete.connect(deleteUser,sender=Profile)

