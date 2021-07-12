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
        fields = ('id', 'created', 'code', 'type',
                  'state', 'owner', 'montant',
                  'from_currency', 'to_currency')

    def can_be_performed_by(self, user):
        return True

    def can_be_executed_by(self, user):
        return True

    def execute(self, user):
        pass

class UserSerializer(serializers.ModelSerializer):
    transactions = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Transaction.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'profile', 'transactions')

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
