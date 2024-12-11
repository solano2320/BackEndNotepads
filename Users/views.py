from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import  status
from rest_framework_simplejwt.tokens import RefreshToken
from Users.serializer import SignUpInputSerializer, SignUpOutputSerializer
from Users.serializer import LogInInputSerializer, LogInOutputSerializer
from Users.serializer import ProfileOutputSerializer

from Users.models import CustomUser



# La vista del SignUp de los usuarios
class SignUp(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        """ """

        # Validacion para ususarios de Notepads
        serializer = SignUpInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Crear el usuario
        if CustomUser.objects.filter(email=serializer.validated_data['email']).exists():
            return Response("Email ya esta registrado", status=status.HTTP_400_BAD_REQUEST)

        if CustomUser.objects.filter(username=serializer.validated_data['username']).exists():
            return Response("username ya esta registrado", status=status.HTTP_400_BAD_REQUEST)

        user = CustomUser.objects.create_user(**serializer.validated_data)

        # token de refresh
        refresh = RefreshToken.for_user(user)

        # Lo que se retorna
        serializer = SignUpOutputSerializer({
            "username": user.username,
            "email": user.email,
            "birth_date": user.birth_date,
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        })
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)



# La vista del Login de los usuarios 
class Login(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        # validacion 
        serializer = LogInInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            user = CustomUser.objects.get(username=serializer.validated_data['username'])
        except CustomUser.DoesNotExist:
            return Response("username o password incorrecta", status=status.HTTP_400_BAD_REQUEST)

        is_password_correct = user.check_password(serializer.validated_data['password'])
        if is_password_correct is False:
            return Response("username o password incorrecta", status=status.HTTP_400_BAD_REQUEST)

        # token del login
        refresh = RefreshToken.for_user(user)

        # Lo que se retorna
        serializer = LogInOutputSerializer({
            "username": user.username,
            "email": user.email,
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        })
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    

class myProfile(APIView):

    def get(self, request):
        serializer = ProfileOutputSerializer({
            "username": request.user.username,
            "email": request.user.email,
            "birth_date": request.user.birth_date
        })
    
        return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)

