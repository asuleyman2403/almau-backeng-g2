from my_auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = '__all__'


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(allow_blank=False, required=True, min_length=8, max_length=255)
    new_password = serializers.CharField(allow_blank=False, required=True, min_length=8, max_length=255)


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(allow_null=False)


class ResetPasswordSerializer(serializers.Serializer):
    repeat_password = serializers.CharField(allow_blank=False, required=True, min_length=8, max_length=255)
    new_password = serializers.CharField(allow_blank=False, required=True, min_length=8, max_length=255)
