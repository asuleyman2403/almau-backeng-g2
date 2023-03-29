from rest_framework.views import APIView, Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from my_auth.serializers import UserSerializer, ChangePasswordSerializer, ForgotPasswordSerializer,\
    ResetPasswordSerializer
from my_auth.models import User, ResetPassword
from django.core.mail import send_mail
from django import template
import datetime
import uuid

RESET_PASSWORD_TIME_LIMIT = 1 * 60 * 60


class UserAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


class ChangePasswordAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request):
        data = request.data
        serializer = ChangePasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        try:
            user = User.objects.get(username=request.user.username)
            user.set_password(data['new_password'])
            user.save()
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=200)
        except User.DoesNotExist:
            return Response({'message': 'User does not exist'}, status=404)


class ForgotPasswordAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = request.data['email']
        try:
            user = User.objects.get(email=email)
            token = uuid.uuid4()
            reset_password = ResetPassword(email=email, token=token, created_at=datetime.datetime.now())
            reset_password.save()
            email_template = template.loader.get_template('my_auth/reset-password-email.html')
            email_content = email_template.render({'FRONTEND_RESET_PASSWORD_URL': 'http://localhost:5500/verify-email',
                                                   'TOKEN': token})
            send_mail(subject='Reset your password', message='', html_message=email_content,
                      from_email='settings.EMAIL_HOST_USER',
                      recipient_list=[user.email],
                      fail_silently=False)
            return Response({'message': "Success"}, status=200)
        except User.DoesNotExist:
            return Response({'message': 'We dont have such user'}, status=404)


class ResetPasswordAPIView(APIView):
    permission_classes = (AllowAny,)

    def put(self, request, token):
        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            reset_password = ResetPassword.objects.get(token=token)
            created_at = reset_password.created_at
            email = reset_password.email
            new_password = request.data['new_password']
            if (datetime.datetime.now(datetime.timezone.utc) - created_at).total_seconds() > RESET_PASSWORD_TIME_LIMIT:
                reset_password.delete()
                return Response({'message': 'Token is expired'}, status=400)
            else:
                user = User.objects.get(email=email)
                user.set_password(new_password)
                user.save()
                reset_password.delete()
                return Response({'message': 'Success'}, status=200)
        except ResetPassword.DoesNotExist:
            return Response({'message': 'Invalid request'}, status=400)
