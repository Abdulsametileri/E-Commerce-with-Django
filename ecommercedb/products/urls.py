from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from products.views import OrderView
from . import views
from django.conf import settings
from django.conf.urls.static import static

#controller

urlpatterns = [
    url(r'^desktop/$', views.categoryDispatcher, name='desktop'),
    url(r'^laptop/$', views.categoryDispatcher, name='laptop'),
    url(r'^tablet/$', views.categoryDispatcher, name='tablet'),
    url(r'^microphone/$', views.categoryDispatcher, name='microphone'),
    url(r'^gaming-headphones/$', views.categoryDispatcher, name='gaming-headphones'),
    url(r'^phone-headsets/$', views.categoryDispatcher, name='phone-headsets'),
    url(r'^bluetooth/$', views.categoryDispatcher, name='bluetooth'),
    url(r'^broom/$', views.categoryDispatcher, name='broom'),
    url(r'^iron/$', views.categoryDispatcher, name='iron'),
    url(r'^television/$', views.categoryDispatcher, name='television'),
    url(r'^detail/(?P<id>\w+)/$', views.productDetail, name='product-detail'),
    url(r'^order/(?P<id>\w+)/$', OrderView.as_view(), name='product-order')
]


