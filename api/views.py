from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from .models import Transaction, Profile
from .permissions import IsOwner, IsOwnerOrReadOnly, IsAdminUser
from .serializers import TransactionSerializer, UserSerializer, UserRegistrationInfoSerializer


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
        if serializer.is_valid() and serializer.can_be_performed_by(request.user):
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

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