from django.shortcuts import render
from projects.models import Projects
from src import azure
#from config import Config as Config
#from src import Config as config
from src.terraform import Terraform as Terraform
from src.azure import Azclass as Azclass
from src.config import Config

# Create your views here.
def open_project(request,project_id):
    #this.project_id = project_id
    return render(request, 'projects.html',{'menu':'project','submenu':'open'})
    #return render(request, 'index.html',{'projects': Projects.objects.all(),'project_id': project_id })
def index(request):
    #this.project_id = project_id
    return render(request,'index.html',{'menu':'home'})
def create_project(request):
    #this.project_id = project_id
    return render(request,'projects.html',{'menu':'project','submenu':'create'})
def project(request):
    #this.project_id = project_id
    return render(request,'projects.html',{'menu':'project','submenu':'find'})
def edit_project(request):
    #this.project_id = project_id
    return render(request,'projects.html',{'menu':'project','submenu':'edit'})
def delete_project(request):
    #this.project_id = project_id
    return render(request,'projects.html',{'menu':'project','submenu':'delete'})
def create_project_id(request,cloud_id):
    if cloud_id == "2":
        credenciais = Config("/home/damato/projetos/dados.json")
        az = Azclass(credenciais)
        az.login()
        retorno = az.getRegion()
        return render(request,'projects.html',{'menu':'project','submenu':'create','cloud_id':cloud_id,'regions':retorno})
    else:
        return render(request, 'projects.html',
                      {'menu': 'project', 'submenu': 'create', 'cloud_id': cloud_id})
def create_project_region(request,cloud_id,cloud_region):
    credenciais = Config("/home/damato/projetos/dados.json")
    az = Azclass(credenciais)
    az.login()
    retorno = az.getRegion()
    return render(request,'projects.html',{'menu':'project','submenu':'create','cloud_id':cloud_id,'regions':retorno,'cloud_region':cloud_region})


'''def handler404(request):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)'''