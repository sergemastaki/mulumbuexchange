from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from api.models import Transaction, Profile, Currency

class TransactionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Transaction
        fields = ('id', 'created', 'code', 'type',
                  'state', 'owner', 'montant',
                  'from_currency', 'to_currency')

class UserSerializer(serializers.ModelSerializer):
    transactions = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Transaction.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'profile', 'transactions')

class CurrencySerializer(serializers.ModelSerializer):
    owner_profile = serializers.ReadOnlyField(source='owner_profile.id')

    class Meta:
        model = Currency
        fields = ('id', 'name', 'solde', 'owner_profile')
        validators = [
            UniqueTogetherValidator(
                queryset=Currency.objects.all(),
                fields=['name', 'owner_profile']
            )
        ]
