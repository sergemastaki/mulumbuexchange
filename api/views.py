from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions
from .models import Transaction, Profile
from .permissions import IsOwner, IsOwnerOrReadOnly, IsAdminUser
from .serializers import TransactionSerializer, UserSerializer # new


class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsAdminUser,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsAdminUser]


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

class UserTransationsList(APIView):
    """
    List user's transactions.
    """
    permission_classes = [permissions.IsAuthenticated,]

    def get(self, request, format=None):
        user = request.user
        transactions = user.transactions
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)
