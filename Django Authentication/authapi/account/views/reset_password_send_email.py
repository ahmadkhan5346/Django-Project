from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from account.utils.renderers import UserRender
from account.serializers.reset_password_send_email import SendPasswordResetEmailSerializer




class SendResetPasswordEmailView(APIView):
    renderer_classes = [UserRender]
    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'msg':'Password reset link send. please check your email'}, status=status.HTTP_200_OK)