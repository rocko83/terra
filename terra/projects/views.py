from django.shortcuts import render
from projects.models import Projects
from src import azure
#from config import Config as Config
#from src import Config as config
from src.terraform import Terraform as Terraform
from src.azure import Azclass as Azclass
from src.config import Config
from .forms import NameForm
from django.shortcuts import HttpResponseRedirect
from .models import Projects

# Create your views here.
def open_project(request,project_id):
    return render(request, 'projects.html',{'menu':'project','submenu':'open'})

def index(request):
    return render(request,'index.html',{'menu':'home'})

def create_project_variables(request):
    return render(request,'projects.html',{'menu':'project','submenu':'variables'})

def project(request):
    return render(request,'projects.html',{'menu':'project','submenu':'find'})

def edit_project(request):
    return render(request,'projects.html',{'menu':'project','submenu':'edit'})

def delete_project(request):
    return render(request,'projects.html',{'menu':'project','submenu':'delete'})
#def projects_main(request):
#    return render(request,'projects_main.html',{'menu':'project','submenu':'find'})
def projects_find(request):
    projects = []
    for dados in Projects.objects.all():
        array2 = []
        array2.append(dados.name)
        array2.append(dados.filedata)
        array2.append(dados.creation)
        array2.append(dados.cloud_id)
        array2.append(dados.id)
        projects.append(array2)


    return render(request,'projects_find.html',{'menu':'project','submenu':'find','projects':projects})

def create_project_id_variables(request,cloud_id):
    if cloud_id == "2":
        credenciais = Config("/home/damato/projetos/dados.json")
        az = Azclass(credenciais)
        az.login()
        retorno = az.getRegion()
        return render(request,'projects.html',{'menu':'project','submenu':'variables','cloud_id':cloud_id,'regions':retorno})
    else:
        return render(request, 'projects.html',
                      {'menu': 'project', 'submenu': 'variables', 'cloud_id': cloud_id})

def create_project_region_variables(request,cloud_id,cloud_region):
    if cloud_id == "2":
        models = Config("/home/damato/projetos/git/rocko83/TerraStandard/terra/src/terraform_models.json")
        credenciais = Config("/home/damato/projetos/dados.json")
        az = Azclass(credenciais)
        az.login()
        retorno = az.getResourceGroup()
        if retorno == False:
            print("False")
        else:
            rgs = retorno
        retorno = az.getVnet(cloud_region)
        if retorno == False:
            print("False")
        else:
            vnets = retorno
        retorno = az.getImage(cloud_region)
        if retorno == False:
            print("False")
        else:
            images = retorno
        retorno = az.getVmSize(cloud_region)
        if retorno == False:
            print("False")
        else:
            vmsizes = retorno
        retorno = az.getDiskType(models)
        if retorno == False:
            print("False")
        else:
            disktypes = retorno
        retorno = az.getTags(models)
        if retorno == False:
            print("False")
        else:
            vmtags = retorno
        retorno = az.getOsType(models)
        if retorno == False:
            print("False")
        else:
            ostypes = retorno
        retorno = az.getAuth(models)
        if retorno == False:
            print("False")
        else:
            auths = retorno
        retorno = az.getDiskCache(models)
        if retorno == False:
            print("False")
        else:
            diskcaches = retorno

        return render(request, 'projects.html',
                      {'menu': 'project', 'submenu': 'variables', 'cloud_id': cloud_id, 'regions': retorno,
                       'cloud_region': cloud_region,'rgs':rgs,'vnets':vnets,'images':images,'vmsizes':vmsizes,
                       'disktypes':disktypes,'vmtags':vmtags,'ostypes':ostypes,'auths':auths,'diskcaches':diskcaches})
    else:
        return render(request, 'projects.html',
                      {'menu': 'project', 'submenu': 'variables', 'cloud_id': cloud_id})

def get_form_create_variables(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            models = Config("/home/damato/projetos/git/rocko83/TerraStandard/terra/src/terraform_models.json")
            credenciais = Config("/home/damato/projetos/dados.json")
            az = Azclass(credenciais)
            az.login()
            retorno = az.getTags(models)
            if retorno == False:
                print("False")
            else:
                vmtags = retorno
            formdata={}
            formdata["projectname"] = form.cleaned_data['projectname']
            formdata["resourcegroup"] = form.cleaned_data['resourcegroup']
            formdata["subnet"] = form.cleaned_data['subnet']
            formdata["vmimage"] = form.cleaned_data['vmimage']
            formdata["vmsize"] = form.cleaned_data['vmsize']
            formdata["disktype"] = form.cleaned_data['disktype']
            formdata["ostype"] = form.cleaned_data['ostype']
            formdata["username"] = form.cleaned_data['username']
            formdata["userpassword"] = form.cleaned_data['userpassword']
            tags={}
            for tag in vmtags:
                tags[tag] = form.data[tag]

        return render(request, 'teste.html', {'form': formdata,'tags':tags})

def get_form_create2(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/" + form.cleaned_data['your_name'] + "/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
'''def handler404(request):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)'''