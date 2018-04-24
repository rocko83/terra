from django import forms
class CaosProject(forms.Form):
    projectname = forms.CharField(required=True,label='Project Name')