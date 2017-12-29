from django.conf.urls import url
from .views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^$', home, name='admin-home'),
    url(r'^addproduct$', add_product, name="admin-add-product")
]
