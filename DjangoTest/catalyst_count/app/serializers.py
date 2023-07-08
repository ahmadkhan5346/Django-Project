from rest_framework import serializers
from app.models import Catalyst


class FileDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalyst
        fields = "__all__"