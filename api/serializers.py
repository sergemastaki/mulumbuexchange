from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Transaction, Profile

class TransactionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Transaction
        fields = ('id', 'created', 'code', 'type',
                  'state', 'owner', )


class UserSerializer(serializers.ModelSerializer):
    transactions = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Transaction.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'profile', 'transactions')
