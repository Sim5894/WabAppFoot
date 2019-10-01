from django.db.models.signals import post_save
from .models import User, Profile, Joueur
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=User)
def create_joueur(sender, instance, created, **kwargs):
    isjoueur = User.objects.values_list("estjoueur", flat=True)
    for joueur in isjoueur:
        lastjoueur = joueur
    if created:
        if lastjoueur == 1:
            Joueur.objects.create(user=instance)



#@receiver(post_save, sender=User)
#def save_joueur(sender, instance, **kwargs):
#    instance.joueur.save()