from django.shortcuts import render, redirect
from django.utils.text import slugify
from .models import *
from .forms import *
from uuid import uuid4
from django.contrib import messages

# Create your views here.

def company_update(request):
    if request.method == 'POST':
        form = CompanyForm(instance=request.user.selfcomp, data=request.POST, files=request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            company = form.save(commit=False)
            company.slug = slugify(f"{uuid4()}{cd['title']}")
            company.save()
            return redirect('company:profile')
        else:
            messages.error(request, "Forma xato to'ldirilgan!")
            return redirect('company:update')
    else:
        form = CompanyForm()
    return render(request, 'update.html', {'form':form})

def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            department = form.save(commit=False)
            department.slug = slugify(f"{uuid4()}{cd['title']}")
            department.company = request.user.selfcom
            department.save()
            return redirect('company:profile')
        else:
            messages.error(request, "Forma xaro to'ldirilgan")
            return redirect('company:depart_update')
    else:
        form = DepartmentForm()
    return render(request, 'company/department_create.html', {'form':form})

def department_update(request):
    if request.method == 'POST':
        form = DepartmentForm(instance=request.user.selfcomp, data=request.POST, files=request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            department = form.save(commit=False)
            department.slug = slugify(f"{uuid4()}{cd['title']}")
            department.save()
            return redirect('company:profile')
        else:
            messages.error(request, "Forma xato to'ldirilgan!")
            return redirect('company:update')
    else:
        form = Department()
    return render(request, 'update.html', {'form':form})

def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            project = form.save(commit=False)
            project.slug = slugify(f"{uuid4()}{cd['title']}")
            project.company = request.user.selfcom
            project.save()
            return redirect('company:profile')
        else:
            messages.error(request, "Forma xaro to'ldirilgan")
            return redirect('company:depart_update')
    else:
        form = ProjectForm()
    return render(request, 'company/project_create.html', {'form':form})

def project_update(request):
    if request.method == 'POST':
        form = ProjectForm(instance=request.user.selfcomp, data=request.POST, files=request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            project = form.save(commit=False)
            project.slug = slugify(f"{uuid4()}{cd['title']}")
            project.save()
            return redirect('company:profile')
        else:
            messages.error(request, "Forma xato to'ldirilgan!")
            return redirect('company:update')
    else:
        form = Department()
    return render(request, 'project_update.html', {'form':form})