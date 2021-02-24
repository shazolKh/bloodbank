from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.core import serializers


from .forms import RegForm, UserProfileForm
from .models import UserProfile


# Create your views here.



def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = RegForm()
        if request.method == 'POST':
            form = RegForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                passs = form.cleaned_data.get('password1')
                new_user = authenticate(request, username=user, password=passs)
                login(request, new_user)
                # user = form.cleaned_data.get('username')
                messages.success(request, 'Please enter your details!!')
                return redirect('profile', user)
        context = {'form': form}
        return render(request, 'users/register.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Username or Password is incorrect!!')
        context = {}
        return render(request, 'users/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def userProfile(request, username):
    if request.method == 'POST':
        name = User.objects.get(username=username)
        age = request.POST.get('age')
        blood = request.POST.get('blood')
        gender = request.POST.get('gender')
        weight = request.POST.get('weight')
        mobile = request.POST.get('mobile')
        mobile2 = request.POST.get('mobile2')
        address = request.POST.get('address')
        dis = request.POST.get('dis')

        profile = UserProfile(user=name, age=age, blood_group=blood, gender=gender, mobile=mobile, mobile2=mobile2,
                              address=address, disease=dis, weight=weight)
        profile.save()
        messages.success(request, 'Your Profile Information is Updated!!!')
        return redirect('settings', request.user.id)

    return render(request, 'users/settings.html')


@login_required(login_url='login')
def userSettings(request, pk):
    profile_info = UserProfile.objects.get(user=pk)

    context = {
        'profile': profile_info
    }
    return render(request, 'users/profile.html', context)


@login_required(login_url='login')
def editProfile(request, pk):
    profile_info = UserProfile.objects.get(user=pk)

    if request.method == 'POST':
        age = request.POST.get('age')
        blood = request.POST.get('blood')
        gender = request.POST.get('gender')
        weight = request.POST.get('weight')
        mobile = request.POST.get('mobile')
        mobile2 = request.POST.get('mobile2')
        address = request.POST.get('address')
        disease = request.POST.get('dis')

        UserProfile.objects.filter(user_id=pk).update(age=age, blood_group=blood, gender=gender, mobile=mobile,
                                                      mobile2=mobile2, address=address, disease=disease, weight=weight)
        messages.success(request, 'Your Information are Updated')

        # print([age, blood, gender, weight, mobile, mobile2, address, disease, pk])
        return redirect('settings', request.user.id)

    context = {
        'profile': profile_info
    }
    return render(request, 'users/edit_profile.html', context)
