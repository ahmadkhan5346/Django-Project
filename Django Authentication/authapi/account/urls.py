from django.urls import path
from account.views.register import UserRegistrationView
from account.views.login import UserLoginView
from account.views.user_profile import UserProfileView
from account.views.change_password import UserChangePassword
from account.views.reset_password_send_email import SendResetPasswordEmailView
from account.views.reset_password import UserPasswordResetView


urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name='regster' ),
    path("login/", UserLoginView.as_view(), name='login' ),
    path("profile/", UserProfileView.as_view(), name='profile'),
    path("changepassword/", UserChangePassword.as_view(), name='changepassword'),
    path("send-reset-password-email/", SendResetPasswordEmailView.as_view(), name='resetpassword'),
    path("reset-password/<uid>/<token>/", UserPasswordResetView.as_view(), name='resetpassword'),
]
