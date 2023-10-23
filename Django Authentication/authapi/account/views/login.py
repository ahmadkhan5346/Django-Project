from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from account.serializers.login import UserLoginSerializer
from django.contrib.auth import authenticate
from account.utils.renderers import UserRender
from account.utils.jwt_token import get_tokens_for_user


class UserLoginView(APIView):
    renderer_classes = [UserRender]
    def post(self, request, format=None):
        
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')

            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token':token, 'msg':'Login Successfull'}, status=status.HTTP_200_OK)
                # response.set_cookie('auth_token', token, max_age=5000)
                # return response
            else:
                return Response({'errors':{'non_fields_errors':['Email or password is not valid']}})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)