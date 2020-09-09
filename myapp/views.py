from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import User,Content
from datetime import datetime

def index(request):

    # Authenticated users view their diary
    if request.user.is_authenticated:
        complete=request.POST.getlist('complete')
        print(complete)

        conts=Content.objects.order_by("-created").all().filter(user=request.user)
        context={
            "conts":conts
        }
        return render(request, "index.html",context)

    # Everyone else is sent to sign in
    else:
        
        return HttpResponseRedirect(reverse("login"))




# for login
def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request,"login.html")




# for registering new user
def register(request):
    if request.method == "POST":
        email = request.POST["email"]
        name  = request.POST["name"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })
        if name in password:
            return render(request, "register.html", {
                "message": "Username should not appear in password"
            })
        if not any(x.isupper() for x in password):
            return render(request, "register.html", {
                "message": "Password should contain an Uppercase letter"
            })
        if not any(x.isdigit() for x in password):
            return render(request, "register.html", {
                "message": "Password should contain atleast one digit"
            })
        if set('[!@#$%^&*()_+{}\]+$').intersection(password):
            pass
        else:
            return render(request, "register.html", {
                "message": "Password should contain atleast one symbol"
            })


        # Attempt to create new user
        try:
            user = User.objects.create_user(email, email, password)
            user.first_name=name.upper()
            user.save()
        # if email already exist
        except IntegrityError as e:
            print(e)
            return render(request, "register.html", {
                "message": "Email address already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "register.html")



# for logout
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

# for new diary
@csrf_exempt
@login_required
def new_list(request):
    if request.method == "POST":
        body=request.POST.get('Body',False)
        due_date=request.POST["duedate"]
        if len(list(due_date))!=0:
            pass
        else:
            due_date=datetime.now()
        user=request.user
        name=request.POST.get('name',False)
        content=Content(name=name,body=body,user=user,due_date=due_date)
        content.save()
        #conts=Content.objects.order_by("-created").all()
        conts=Content.objects.order_by("-created").all().filter(user=user)
        context={
            "conts":conts,
        }
        return render(request, "index.html",context)

#for viewing single list
@csrf_exempt
@login_required
def single_view(request,name):
        user=request.user
        conts=Content.objects.order_by("-created").all().filter(name=name,user=user)
        context={
            "conts":conts
        }
        return render(request,"single.html",context)

#for deleting tasks
@csrf_exempt
@login_required
def delete(request,name):
    user=request.user   
    Content.objects.all().filter(name=name,user=user).delete()
    return HttpResponseRedirect(reverse("index"))

#for task completion
@csrf_exempt
@login_required
def tasky(request,name):
    c=Content.objects.get(name=name)
    c.complete=True
    c.save()
    user=request.user
    conts=Content.objects.order_by("-created").all().filter(name=name,user=user)
    context={
            "conts":conts
        }
    return render(request,"single.html",context)


#for task not completion
@csrf_exempt
@login_required
def taskn(request,name):
    c=Content.objects.get(name=name)
    c.complete=False
    c.save()
    user=request.user
    conts=Content.objects.order_by("-created").all().filter(name=name,user=user)
    context={
            "conts":conts
        }
    return render(request,"single.html",context)

