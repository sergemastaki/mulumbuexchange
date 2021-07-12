from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

Transactions_types = {'DEPOT':'depot','RETRAIT':'retrait','VENTE':'vente','ACHAT':'achat','SWAP':'swap'}
States_types = {'EN_COURS':'en_cours', 'EXECUTER':'executer', 'ANNULER':'annuler'}

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    numero = models.CharField(unique=True, max_length=15)
    airtel_money = models.CharField(max_length=15, default=0)
    orange_money = models.CharField(max_length=15, default=0)
    africell_money = models.CharField(max_length=15, default=0)
    mpesa = models.CharField(max_length=15, default=0)
    equity_bcdc = models.CharField(max_length=20, default=0)
    uba = models.CharField(max_length=20, default=0)
    ecobank = models.CharField(max_length=20, default=0)

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
    montant = models.FloatField(default=0)
    from_currency = models.CharField(max_length=15, default='BTC')
    to_currency = models.CharField(max_length=15, default='USDT')
    code = models.TextField()
    type = models.CharField(choices=Transactions_types.items(), max_length=100)
    state = models.CharField(choices=States_types.items(), default=States_types['EN_COURS'], max_length=100)
    owner = models.ForeignKey('auth.User', related_name='transactions', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return str(self.type)

class Currency(models.Model):
    name = models.CharField(max_length=50)
    solde = models.FloatField()
    owner_profile = models.ForeignKey(Profile, related_name='currencies', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('name', 'owner_profile'))

    def __str__(self):
        return str(self.name)
