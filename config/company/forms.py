from dataclasses import fields
from django import forms
from django import forms
from .models import *

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('title', 'logo', 'info')

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('title', 'info')

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'info', 'image', 'tz')