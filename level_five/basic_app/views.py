from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm

#imports for authentication 

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):

    return render(request,'basic_app/index.html')

@login_required
def special(request):
    return render(request,'basic_app/special.html')
    #return HttpResponse("Login successful SPECIAL")

@login_required
def user_logout(request):
    #In order to logout an user, the user has to be logged in first
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == "POST" :
        #data is a parameter for the form
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid() :
            #Check this area again
            user = user_form.save() # grabbing the user form and storing to database
            print("Before")
            print(user.password)
            user.set_password(user.password) # hashing the password using set_password method
            print("After")
            print(user.password)
            user.save() # saving the hashed password to the database.
            #Preventing to override with the above user hence commit=False
            profile = profile_form.save(commit=False)
            #OneToOne relation
            print("USER")
            print(user)
            profile.user = user
            print(profile.user)

            #request.FILES will be used to get all types of files from the user.
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'basic_app/register.html',{'user_form':user_form,
                                                    'profile_form':profile_form,
                                                    'registered':registered})

def user_login(request):

    if request.method == "POST":
        print(request)
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)

        #Authenticate the user using the username and password specifying the parameters

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                #Login the user if the account is active
                login(request,user)
                #post successful login redirect the user to home/index page
                return HttpResponseRedirect(reverse('index'))
            
            else:
                return HttpResponse("Account not active")
        
        else:
            print("Login failed")
            print("Username : {} and password {}".format(username,password))

            return HttpResponse("Invalid login details supplied!")

    else:
        return render(request,'basic_app/login.html',{})






