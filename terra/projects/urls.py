from django.conf.urls import url
from projects import views
from projects.views import index
from projects.views import project
from projects.views import create_project_variables
from projects.views import create_project_id_variables
from projects.views import create_project_region_variables
from projects.views import open_project
from projects.views import edit_project
from projects.views import delete_project
from projects.views import get_form_create_variables
#from projects.views import projects_main
from projects.views import projects_find
import projects.views as project_view
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
    url(r'^projects/variables/$', create_project_variables, name='create_project_variables'),
    url(r'^projects/variables/(?P<cloud_id>\d+)$', create_project_id_variables, name='create_project_id_variables'),
    url(r'^projects/variables/(?P<cloud_id>\d+)/region/(?P<cloud_region>[\w\-]+)/$', create_project_region_variables,
        name='create_project_region_variables'),
    url(r'^projects/find/$', project, name='project'),
    url(r'^projects/create/form$', get_form_create_variables, name='get_form_create_variables'),
    #url(r'^perfis/(?P<perfil_id>\d+)/convidar$', views.convidar, name='convidar'),
    #url(r'^convite/(?P<convite_id>\d+)/aceitar$', views.aceitar, name='aceitar'),
    url(r'projectsmain/$',projects_find,name='projects_main'),
    url(r'projectsmain/find$',projects_find,name='projects_find'),
    url(r'^projectsmain/create/form',project_view.projects_create_form,name='projects_create_form')
]
'''handler404 = handler404
handler500 = handler500'''