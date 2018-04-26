from django.conf.urls import url
from caosmonkey import views as Views
urlpatterns = [
    url(r'caos/$', Views.caosmain, name='caosmain'),
    url(r'caos/create/$', Views.caos_create, name='caoscreate')
]
