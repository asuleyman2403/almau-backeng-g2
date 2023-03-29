from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from my_auth.views.cbv import UserAPIView, ChangePasswordAPIView, ForgotPasswordAPIView, ResetPasswordAPIView

urlpatterns = [
    path('login', TokenObtainPairView.as_view()),
    path('refresh-token', TokenRefreshView.as_view()),
    path('register', UserAPIView.as_view()),
    path('change-password', ChangePasswordAPIView.as_view()),
    path('forgot-password', ForgotPasswordAPIView.as_view()),
    path('reset-password/<slug:token>', ResetPasswordAPIView.as_view())
    # path('change-password'),
    # path('forgot-password'),
    # path('reset-password'),
]