from django.conf.urls import url
from caosmonkey import views as Views
urlpatterns = [
    url(r'caos/$', Views.caosmain, name='caosmain'),
    url(r'caos/find/form',Views.caosmain_find_form,name = 'caosmain_find_form')
]
