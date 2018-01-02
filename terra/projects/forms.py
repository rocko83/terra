from django import forms

class NameForm(forms.Form):
    projectname = forms.CharField(label='projectname', max_length=50)
    resourcegroup = forms.CharField(label='resourcegroup', max_length=50)
    subnet = forms.CharField(label='subnet', max_length=500)
    vmimage = forms.CharField(label='vmimage', max_length=500)
    vmsize = forms.CharField(label='vmsize', max_length=50)
    disktype = forms.CharField(label='disktype', max_length=50)
    #vmtag = forms.CharField(label='VM Tag', max_length=50)
    ostype = forms.CharField(label='ostype', max_length=50)
    username = forms.CharField(label='username', max_length=25)
    password = forms.CharField(label='password', max_length=25)

