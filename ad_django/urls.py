"""ad_django URL Configuration

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
from django.conf.urls import url

import xadmin
from users.views.index import Index
from users.views.login import LoginView
from users.views.logout import LogoutView
from users.views.maintain import Maintain
from users.views.user import User

urlpatterns = [
    url(r'^$', Index.as_view(), name="index"),
    url('^xadmin/', xadmin.site.urls, name="xadmin"),

    url(r'^accounts/login/', LoginView.as_view(), name="login"),
    url(r'^accounts/logout/', LogoutView.as_view(), name="logout"),
    url(r'^maintain/$', Maintain.as_view(), name="maintain"),

    url(r'^user/', User.as_view(), name="user"),

]
