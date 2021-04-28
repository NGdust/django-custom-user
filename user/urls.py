from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from user.views import *

urlpatterns = [
    path(r'<int:pk>/', UserView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user'),
    path(r'registration/', RegistrationAPIView.as_view(), name='user_registration'),
    path(r'login/', LoginAPIView.as_view(), name='user_login'),
    path(r'refresh/', TokenRefreshView.as_view(), name='user_refresh'),
]