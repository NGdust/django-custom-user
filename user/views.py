from datetime import datetime

import jwt
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User
from user.serializer import UserReadSerialiser, UserSerialiser, RegistrationSerializer, LoginSerializer


class RegistrationAPIView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'access': serializer.data.get('access', None),
            'refresh': serializer.data.get('refresh', None)
        }
        return Response(response, status.HTTP_201_CREATED,)


class LoginAPIView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status.HTTP_200_OK)



class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class_reed = UserReadSerialiser
    serializer_class = UserSerialiser

    def get_serializer_class(self):
        if self.request.method in ('GET',):
            return self.serializer_class_reed
        return self.serializer_class