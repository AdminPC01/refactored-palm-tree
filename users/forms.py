from django.forms import ModelForm, widgets
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Skill

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "email", "username", "password1", "password2"]
        label = {
            "first_name": "Name"
        }
    #     #  CheckboxSelectMultiple()
    #     widgets = { 'tags': forms.CheckboxSelectMultiple()}
    # def __init__(self,*args,**kwargs):
    #     super(CustomUserCreationForm,self).__init__(*args,**kwargs)
    #
    #     for name, field in self.fields.items():
    #         field.widget.attr.update({"class": "input "})

    def __init__(self,*args,**kwargs):
        super(CustomUserCreationForm,self).__init__(*args,**kwargs)
        for key,value in self.fields.items():
            value.widget.attrs.update({"class":"input"})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ["user"]

    def __init__(self,*args,**kwargs):
        super(ProfileForm, self).__init__(*args,**kwargs)
        for key, field in self.fields.items():
            field.widget.attrs.update({"class":"input"})


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"
        exclude = ["owner"]

    def __init__(self,*args,**kwargs):
        super(SkillForm, self).__init__(*args,**kwargs)
        for key, field in self.fields.items():
            field.widget.attrs.update({"class":"input"})