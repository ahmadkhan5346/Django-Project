from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializers.register import UserRegistrationSerializer
from account.utils.renderers import UserRender



class UserRegistrationView(APIView):
    renderer_classes = [UserRender]
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({'msg':"Registration Successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    