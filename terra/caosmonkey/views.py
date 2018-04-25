from django.shortcuts import render
from caosmonkey.models import Caosmonkey
from django.contrib import admin
from .forms import CaosProject
from .models import Caosmonkey
admin.site.register(Caosmonkey)
projectName="Caos Monkey"

def caosmain(request):
    if request.method == 'POST':
        form = CaosProject(request.POST)
        if form.is_valid():
            search = form.cleaned_data['projectname']
            try:
                results = Caosmonkey.objects.get(name__contains=search)
                return render(request, 'caos_find.html',
                              {'menu': 'project', 'submenu': 'find', 'results': results,
                               'title': projectName, 'method': 'post'})
            except:
                print(search + " nao existe")
            return render(request, 'caos_find.html',
                          {'menu': 'project', 'submenu': 'find',
                           'title': projectName, 'method': 'post'})
    else:
        form = CaosProject()
        projects = []
        for dados in Caosmonkey.objects.all().order_by('-creation'):
            array2 = []
            array2.append(dados.name)
            array2.append(dados.filedata)
            array2.append(dados.creation)
            array2.append(dados.cloud_id)
            array2.append(dados.id)
            projects.append(array2)

        return render(request, 'caos_find.html',
                      {'menu': 'caos', 'submenu': 'find', 'method': 'web', 'title': projectName, 'form': form,'projects':projects})