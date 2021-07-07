from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

Transactions_types = {'DEPOT':'depot','RETRAIT':'retrait','VENTE':'vente','ACHAT':'achat','SWAP':'swap'}
States_types = {'EN_COURS':'en_cours', 'EXECUTER':'executer', 'ANNULER':'annuler'}

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    numero = models.CharField(max_length=15)

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Transaction(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    code = models.TextField()
    type = models.CharField(choices=Transactions_types.items(), max_length=100)
    state = models.CharField(choices=States_types.items(), default=States_types['EN_COURS'], max_length=100)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return str(self.created)
