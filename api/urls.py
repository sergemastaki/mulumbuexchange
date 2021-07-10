from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('transactions/', views.TransactionList.as_view()),
    path('transactions/<int:pk>/', views.TransactionDetail.as_view()),
    path('transactions/<int:pk>/execute', views.TransactionExecution.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('users/register/', views.UserRegistration.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
