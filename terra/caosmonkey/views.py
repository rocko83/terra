from django.shortcuts import render
from caosmonkey.models import Caosmonkey
from django.contrib import admin
from .forms import CaosProject
admin.site.register(Caosmonkey)
projectName="Caos Monkey"
def caosmain(request):
    form = CaosProject()
    return render(request, 'caos_find.html', {'menu': 'caos', 'submenu': 'find','title':projectName,'form':form})
def caosmain_find_form(request):
    if request.method == 'POST':
        form = CaosProject(request.POST)
        if form.is_valid():
            print(form.cleaned_data['projectname'])
    #return redirect('http://' + form.cleaned_data['projectname'])
    return render(request, 'caos_find_result.html',
                  {'menu': 'project', 'submenu': 'find', 'result':form.cleaned_data['projectname'],'title':projectName})
