from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView
from allauth.socialaccount.views import signup
# from authentication.views import GoogleLogin
# from authentication.views import FacebookLogin
from django.urls import path, include
from . import views
from authentication.views import GoogleLogin, FacebookLogin



urlpatterns = [
    # path("register/", RegisterView.as_view(), name="rest_register"),
    # path("login/", LoginView.as_view(), name="rest_login"),
    # path("logout/", LogoutView.as_view(), name="rest_logout"),
    # path("user/", UserDetailsView.as_view(), name="rest_user_details"),
    path('rest/', include('dj_rest_auth.urls')),
    path('rest/register/', include('dj_rest_auth.registration.urls')),
    path('rest/google/', GoogleLogin.as_view(), name='google_login'),
    path("signup/", signup, name="socialaccount_signup"),
    path("google/", GoogleLogin.as_view(), name="google_login"),
    path("facebook/", FacebookLogin.as_view(), name='fb_login'),
]