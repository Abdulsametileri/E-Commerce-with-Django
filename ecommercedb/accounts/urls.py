from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^signout/$', SignOutView.as_view(), name='signout'),
]
