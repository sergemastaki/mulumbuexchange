from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from rest_framework.authtoken import views as authtoken_views

urlpatterns = [
    path('orders/', views.OrderList.as_view()),
    path('transactions/', views.TransactionList.as_view()),
    path('transactions/<int:pk>/', views.TransactionDetail.as_view()),
    path('transactions/<int:pk>/execute', views.TransactionExecution.as_view()),
    path('currencies-soldes/', views.CurrencyList.as_view()),
    path('accounts/profile/', views.UserDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('users/register/', views.UserRegistration.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', authtoken_views.obtain_auth_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)
