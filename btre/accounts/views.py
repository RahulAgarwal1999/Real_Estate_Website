from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import Contact
# Create your views here.
def register(request):
    if request.method=='POST':
        # Get form value
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        #Check if password match
        if password==password2:
            #Check username for that we have to import User model
            if User.objects.filter(username=username).exists():  #objects check from the database that the username in the database is equal to the value store in variable username
                messages.error(request,'That username is taken')
                return redirect('register')

            else:
                if User.objects.filter(email=email).exists(): #objects check from the database that the username in the database is equal to the value store in variable username
                    messages.error(request,'That Email is being used')
                    return redirect('register')
                else:
                    #Looks Good
                    user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                    #direct Login after register
                    # auth.login(request,user)    first import auth
                    # messages.success(request,'You are now logged in')
                    # return redirect('index')

                    #  OR

                    #Fill login page after register
                    user.save()
                    messages.success(request,'You are now registered and can now Log In')
                    return redirect('login')

        else:
            messages.error(request,'Password do not match')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now Logged In')
            return redirect('dashboard')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('login')
    else:
        return render(request,'accounts/login.html')


def logout(request):
    if request.method=='POST':
        auth.logout(request)
        messages.success(request,'You are now Logged Out')
        return redirect('index')

def dashboard(request):
    user_contacts=Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context={
        'contacts':user_contacts
    }
    return render(request,'accounts/dashboard.html',context)
