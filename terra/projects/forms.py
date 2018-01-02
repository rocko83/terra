from django import forms

class NameForm(forms.Form):
    projectname = forms.CharField(required=True)
    resourcegroup = forms.CharField(required=True)
    subnet = forms.CharField(required=True)
    vmimage = forms.CharField(required=True)
    vmsize = forms.CharField(required=True)
    disktype = forms.CharField(required=True)
    #vmtag = forms.CharField(label='VM Tag', max_length=50)
    ostype = forms.CharField(required=True)
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)

