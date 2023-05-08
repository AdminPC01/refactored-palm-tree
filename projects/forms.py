from django.forms import ModelForm, widgets
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        exclude = ["owner","vote_total","vote_ratio"]

    def __init__(self,*args,**kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)
        for key,value in self.fields.items():
            value.widget.attrs.update({"class":"input"})
            print(key)
