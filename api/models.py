from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

Transactions_types = {'DEPOT':'depot','RETRAIT':'retrait','VENTE':'vente','ACHAT':'achat','SWAP':'swap'}
States_types = {'EN_COURS':'en_cours', 'EXECUTER':'executer', 'ANNULER':'annuler'}
Currencies = [{'code':'BTC'}, {'code':'ETH'}, {'code':'BNB'}, {'code':'USDT'}, {'code':'AVAX'}, {'code':'DOT'}, {'code':'USD'}]

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
            Profile.objects.create(user=instance, numero="+2430000000")

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Transaction(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    montant = models.FloatField(default=0)
    taux = models.FloatField(default=1)
    from_currency = models.CharField(max_length=15, default='BTC')
    to_currency = models.CharField(max_length=15, default='USDT')
    tx_id = models.CharField(max_length=100, default='')
    moyen = models.CharField(max_length=15, default='')
    account_number = models.CharField(max_length=30, default='')
    wallet = models.CharField(max_length=100, default='')
    code = models.TextField(default='')
    type = models.CharField(choices=Transactions_types.items(), max_length=100)
    state = models.CharField(choices=States_types.items(), default=States_types['EN_COURS'], max_length=100)
    owner = models.ForeignKey('auth.User', related_name='transactions', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return str(self.type)

class Currency(models.Model):
    name = models.CharField(max_length=50, default='USD')
    solde = models.FloatField(default=0)
    owner = models.ForeignKey('auth.User', related_name='currencies', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        unique_together = (('name', 'owner'))

    def __str__(self):
        return str(self.name)
