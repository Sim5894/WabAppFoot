"""TFE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from connexion import views as connexion_views
from connexion.views import LoginView, RegisterView
from classement import views as classement_views
from match import views as match_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view(), name='register'),
    path('finmatch/', match_views.finmatch, name='finmatch'),
    path('selection/', match_views.selection, name='selection'),
    path('profile/', connexion_views.profile, name='profile'),
    path('login/', LoginView.as_view(), name='login'),
    path('classement/', classement_views.classement, name='classement'),
    path('calendrier/', include('classement.urls')),
    path('covoit/', include('covoit.urls')),
    #path("getMatchsData/", classement_views.getMatchsData, name="get-matchs-data"),
    path('deconnexion/', auth_views.LogoutView.as_view(template_name='connexion/logout.html'), name='deconnexion'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='connexion/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='connexion/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='connexion/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    #path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='connexion/password_reset_complete.html'),         name='password_reset_complete'),

    path('', include('connexion.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
