from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from .models import Transaction, Profile, Currency, Currencies
from .permissions import IsOwner, IsOwnerOrReadOnly, IsAdminUser
from .serializers import (
    TransactionSerializer,
    UserSerializer,
    UserRegistrationInfoSerializer,
    CurrencySerializer
)


class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def list(self, request):
        user = request.user
        transactions = None
        if user.is_staff:
            transactions = self.queryset.all()
        else:
            transactions = user.transactions
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = TransactionSerializer(data=request.data)
        currencies_serializer = CurrencySerializer(request.user.currencies, many=True)
        if serializer.is_valid() and serializer.can_be_performed_by(currencies_serializer):
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"solde": "Insuffisant"}, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CurrencyList(generics.ListCreateAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [permissions.IsAuthenticated,]

    def list(self, request):
        currencies = request.user.currencies
        serializer = CurrencySerializer(currencies, many=True)
        self.add_currencies_not_on_user_list(serializer)
        return Response(serializer.data)

    def add_currencies_not_on_user_list(self, serializer):
        user_currencies_codes = [currency['name'] for currency in serializer.data]
        for currency in Currencies:
            if currency['code'] not in user_currencies_codes:
                self.perform_create(currency)

    def perform_create(self, data):
        serializer = CurrencySerializer(data={'name': data['code']})
        if serializer.is_valid(raise_exception=True):
            serializer.save(owner=self.request.user)

class OrderList(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def list(self, request):
        transactions = self.queryset.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class TransactionExecution(APIView):
    permission_classes = [permissions.IsAuthenticated,]

    def get_object(self, pk):
        try:
            return Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        user = request.user
        transaction = self.get_object(pk)
        serializer = TransactionSerializer(transaction)
        if serializer.can_be_executed_by(request.user):
            serializer.execute(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsAdminUser]

class UserRegistration(generics.CreateAPIView):
    serializer_class = UserRegistrationInfoSerializer
    slug_field = 'slug'

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
