from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator
from api.models import Transaction, Profile, Currency, Transactions_types

class CantBeExecutedError(Exception):
    """Exception raised when transaction can't be performed."""
    pass

class NotValidError(Exception):
    """Exception raised when data not valid."""
    pass

class TransactionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Transaction
        fields = ('id', 'created', 'code', 'type', 'taux',
                  'state', 'owner', 'montant', 'wallet',
                  'tx_id', 'moyen', 'account_number',
                  'from_currency', 'to_currency')

    def get_currency(self, currency_name, currencies):
        for currency in currencies.data:
            if currency['name'] == currency_name:
                return currency
        return None

    def can_be_performed_by(self, currencies):
        if self.validated_data["type"].lower() == Transactions_types["DEPOT"]:
            return True
        if (self.validated_data["type"].lower() == Transactions_types["RETRAIT"] or
            self.validated_data["type"].lower() == Transactions_types["SWAP"]):
            currency = self.get_currency(self.validated_data["from_currency"], currencies)
            if self.validated_data["montant"] > currency["solde"]:
                return False
            return True
        if self.validated_data["type"].lower() == Transactions_types["ACHAT"]:
            currency = self.get_currency('USDT', currencies)
            if self.validated_data["montant"] * self.validated_data["taux"] > currency["solde"]:
                return False
            return True
        if self.validated_data["type"].lower() == Transactions_types["VENTE"]:
            currency = self.get_currency(self.validated_data["from_currency"], currencies)
            if self.validated_data["montant"] > currency["solde"]:
                return False
            return True
        return False

    def can_be_executed_by(self, user):
        return True

    def execute(self, user):
        pass

class MinimumProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('id', 'numero')

class UserSerializer(serializers.ModelSerializer):
    profile = MinimumProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'profile')

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('id', 'numero', 'user', 'currencies')
        read_only_fields = ('currencies', 'user')

class UserRegistrationInfoSerializer(serializers.ModelSerializer):
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    profile = ProfileSerializer()
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.profile.numero = validated_data['profile']['numero']
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'email',
                  'password',
                  'profile',
                  )

class CurrencyTypeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=20)

class CurrencySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner_profile.id')

    class Meta:
        model = Currency
        fields = ('id', 'name', 'solde', 'owner')
        extra_kwargs = {'owner': {'required': False}}
        validators = []
