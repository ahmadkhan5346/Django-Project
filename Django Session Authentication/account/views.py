from django.contrib.auth import authenticate, login, logout
from account.models import User
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serialzers import UserSerializer
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from django.conf import settings
from account.utils import send_activation_email
from django.shortcuts import render
# from rest_framework.request import Request

@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFTokenView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        return Response({"Success":"CSRF Cookie Set"})

@method_decorator(csrf_protect, name='dispatch')
class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.create(serializer.validated_data)
            print('================================>',user)

            # Send Account Activation Email
            uid = urlsafe_base64_encode(force_bytes(user.pk)) # type: ignore
            token = default_token_generator.make_token(user)
            activation_link = reverse('activate', kwargs={'uid':uid, 'token':token})
            activation_url = f"{settings.SITE_DOMAIN}{activation_link}"

            send_activation_email(user, activation_url)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@method_decorator(csrf_protect, name='dispatch')
class ActivateView(APIView):
    permission_classes = [AllowAny]


@method_decorator(csrf_protect, name='dispatch')
class ActivationConfirm(APIView):
    permission_classes = [AllowAny]

    def post(self , request):
        uid = request.data.get('uid')
        token = request.data.get('token')
        if not uid or not token:
            return Response({"Details":"Missing uid or token"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            uid = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk = uid)

            if default_token_generator.check_token(user, token):
                if user.is_active:
                    return Response({"Details":"Account is already activated."}, status=status.HTTP_200_OK)
                
                user.is_active = True
                user.save()
                return Response({"Details":"Account activated successfully."}, status=status.HTTP_200_OK)
            
            else:
                return Response({"Details":"Invalid activation link."}, status=status.HTTP_400_BAD_REQUEST)
            
        except (User.DoesNotExist, ValueError):
            return Response({"Details":"Invalid activation link."}, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_protect, name='dispatch')
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print('============================>', request.__dict__)
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return Response({"Detail":"Logged in successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"Details":"Email or Password is incorrect."}, status=status.HTTP_400_BAD_REQUEST)
        
class UserDetailView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        data = serializer.data
        data["is_staff"] = request.user.is_staff # type: ignore
        return Response(data)
        
class LogoutView(APIView):
    def get(self, request):
        logout(request)
        return Response({"Details":"Logged out successfully."}, status=status.HTTP_200_OK)
