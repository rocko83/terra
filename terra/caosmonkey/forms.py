from django import forms
class CaosProject(forms.Form):
    projectname = forms.CharField(required=True,label='Project Name')
    name = forms.CharField(required=True)
    cloud_id = forms.IntegerField(required=True)