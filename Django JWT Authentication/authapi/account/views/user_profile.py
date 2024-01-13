from rest_framework.views import APIView
from account.utils.renderers import UserRender
from account.serializers.user_profile import UserProfileSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated



class UserProfileView(APIView):
    print('inside class:')
    renderer_classes = [UserRender]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        print(type(request))
        print('inside get')
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)