from django.shortcuts import render, redirect
from .forms import (
    StudentAccountForm,
    RegisterForm
)
from .models import StudentAccount, Address, FamilyInformation, EducationalBackground, Subject

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# =====================================================
# AUTHENTICATION VIEWS
# =====================================================

def register_user(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Account created successfully! You can now log in.')
        return redirect('login_user')
    return render(request, 'auth/register.html', {'form': form})


def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('dashboard')
        messages.error(request, 'Invalid username or password.')
    return render(request, 'auth/login.html', {'form': form})


def logout_user(request):
    auth_logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login_user')


# =====================================================
# DASHBOARD + DATA VIEWS
# =====================================================

@login_required(login_url='login_user')
def dashboard(request):
    students = StudentAccount.objects.all()
    return render(request, 'auth/dashboard.html', {'students': students})


@login_required(login_url='login_user')
def student_account_view(request):
    students = StudentAccount.objects.all()
    return render(request, 'student.html', {'students': students})


@login_required(login_url='login_user')
def address_view(request):
    addresses = Address.objects.all()
    return render(request, 'address.html', {'addresses': addresses})


@login_required(login_url='login_user')
def family_view(request):
    families = FamilyInformation.objects.all()
    return render(request, 'family.html', {'families': families})


@login_required(login_url='login_user')
def education_view(request):
    educations = EducationalBackground.objects.all()
    return render(request, 'education.html', {'educations': educations})


@login_required(login_url='login_user')
def subject_view(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects.html', {'subjects': subjects})


@login_required(login_url='login_user')
def add_student_view(request):
    form = StudentAccountForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Student added successfully!')
        return redirect('add_student')

    students = StudentAccount.objects.all()
    return render(request, 'auth/add_student.html', {
        'form': form,
        'students': students
    })

@login_required(login_url='login_user')
def edit_student_view(request, student_id):
    student = StudentAccount.objects.get(id=student_id)
    form = StudentAccountForm(request.POST or None, instance=student)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Student information updated successfully!')
        return redirect('add_student')

    return render(request, 'auth/edit_student.html', {'form': form, 'student': student})


@login_required(login_url='login_user')
def success(request):
    return render(request, 'auth/success.html')
