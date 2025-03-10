from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from logreg.forms import UserForm,UserProfileInfoForm
# Create your views here.
def index(request):
    return render(request,'logreg/index.html')@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def log_request(request):
    logout(request)
    return HttpResponse('You are logOut')
def register_user(request):
    registered=False
    if request.method== 'POST':
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            if 'profile_pic' in request.FILES:
                print('profile pic found')
                profile.profile_pic = request.FILES['pro_pic']
            profile.save()
            registered=True
        else:
            print(user_form.errors)
            print("_____________")
            print(profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()
        user_details={'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered}
        return render(request,'logreg/index.html',context=user_details)

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active():
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'logreg/login.html', {})