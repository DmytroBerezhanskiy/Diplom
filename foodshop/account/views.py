from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm, UserEditForm, ProfileEditForm
from .models import UserProfile


def register(request):
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            new_user = register_form.save(commit=False)
            new_user.set_password(register_form.cleaned_data['password'])
            new_user.save()
            UserProfile.objects.create(user=new_user)
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        register_form = RegistrationForm()
    return render(request, 'registration/register.html', {'register_form': register_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.userprofile, data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully')
        else:
            messages.error(request, 'Something\'s going wrong')
    else:
        user_form = UserEditForm()
        profile_form = ProfileEditForm()
    return render(request, 'registration/edit.html', {'user_form': user_form, 'profile_form': profile_form})