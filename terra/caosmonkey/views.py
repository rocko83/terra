from django.shortcuts import render
from caosmonkey.models import Caosmonkey
from django.contrib import admin
admin.site.register(Caosmonkey)
def caosmain(request):
    return render(request, 'caos.html', {'menu': 'caos', 'submenu': 'find'})
