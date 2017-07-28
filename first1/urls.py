from django.conf.urls import url

from first1 import views

urlpatterns = [

    url(r'^x/(?P<name>.+)/$', views.test, name='test_view'),
    url(r'^e/(?P<name>.+)/$', views.get_email, name='get_email'),
]
