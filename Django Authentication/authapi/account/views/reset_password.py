from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from account.utils.renderers import UserRender
from account.serializers.reset_password import UserPasswordResetSerializer



class UserPasswordResetView(APIView):
    renderer_classes = [UserRender]
    def post(self, request, uid, token, format=None):
        serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
        serializer.is_valid(raise_exception=True)
        return Response({'msg':'Password Reset Successfully'}, status=status.HTTP_200_OK)