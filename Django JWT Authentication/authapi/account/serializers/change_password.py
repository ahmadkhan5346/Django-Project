from rest_framework import serializers




class UserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=50, style={'input_type':'password'}, write_only=True)
    password2 = serializers.CharField(max_length=50, style={'input_type':'password'}, write_only=True)
    class Meta:
        fields = ['password', 'password2']

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesnot match")
        user = self.context.get('user')
        user.set_password(password)
        user.save()
        return attrs
        
        