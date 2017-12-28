from django.conf.urls import url
from projects import views
from projects.views import index
from projects.views import project
from projects.views import create_project
from projects.views import create_project_id
from projects.views import create_project_region
from projects.views import open_project
from projects.views import edit_project
from projects.views import delete_project
'''from projects.views import handler404
from projects.views import handler500'''
#import project.views

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^projects/(?P<project_id>\d+)$', open_project, name='open_project'),
    url(r'^projects/$', project, name='project'),
    url(r'^projects/open/$', project, name='project'),
    url(r'^projects/edit/$', edit_project, name='edit_project'),
    url(r'^projects/delete/$', delete_project, name='delete_project'),
    url(r'^projects/create/$', create_project, name='create_project'),
    url(r'^projects/create/(?P<cloud_id>\d+)$', create_project_id, name='create_project_id'),
    url(r'^projects/create/(?P<cloud_id>\d+)/region/(?P<cloud_region>[\w\-]+)/$', create_project_region, name='create_project_region'),
    url(r'^projects/find/$', project, name='project'),
    #url(r'^perfis/(?P<perfil_id>\d+)/convidar$', views.convidar, name='convidar'),
    #url(r'^convite/(?P<convite_id>\d+)/aceitar$', views.aceitar, name='aceitar')
]
'''handler404 = handler404
handler500 = handler500'''