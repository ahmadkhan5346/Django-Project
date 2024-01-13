from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.utils.renderers import UserRender
from rest_framework.permissions import IsAuthenticated
from account.serializers.change_password import UserChangePasswordSerializer





class UserChangePassword(APIView):
    renderer_classes = [UserRender]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(data=request.data, context={'user':request.user})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Changed Successfully'}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        