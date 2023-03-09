from rest_framework.viewsets import ModelViewSet

from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action

from authentication.serializers import SignUpSerializer


class AuthToken(ObtainAuthToken, ModelViewSet):

    serializer_class = SignUpSerializer
    permission_classes = []

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def signup(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            user = serializer.save()
            response = {"message": "User Created Successfully"}

            return JsonResponse(data=response, status=201)

        return JsonResponse(serializer.errors, status=400)

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def login(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            response = {"message":"Login successfully", "token": str(token)}

            return JsonResponse(data=response, status=200)

        else:
            return JsonResponse(data={"message": "Invalid email or password"}, status=400)

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def logout(self, request, *args, **kwargs):

        user = request.user
        Token.objects.get(user=user).delete()

        return JsonResponse()
