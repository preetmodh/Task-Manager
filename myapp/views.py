from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import User,Content
from datetime import datetime
import json

def index(request):

    # Authenticated users view their lists
    if request.user.is_authenticated:
        conts=Content.objects.order_by("-created").all().filter(user=request.user)
        context={
            "conts":conts
        }
        return render(request, "index.html",context)

    # Everyone else is sent to sign in
    else:

        return HttpResponseRedirect(reverse("login"))




# for login
@csrf_exempt
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
@csrf_exempt
def register(request):
    if request.method == "POST":
        email = request.POST["email"]
        name  = request.POST["name"]
        password = request.POST["password"]


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
        response_data = {'success':1}
        return HttpResponse(json.dumps(response_data), content_type="application/json")
        
    else:
        return render(request, "register.html")




# for logout
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

# for new list
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
        if (len(list(name))==0 or len(list(body))==0):
            return HttpResponseRedirect(reverse("index"))
        else:
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
        cont=Content.objects.order_by("-created").all().filter(name=name,user=user)
        conts=Content.objects.order_by("-created").all().filter(user=request.user)
        context={
            "cont":cont,
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
    cont=Content.objects.order_by("-created").all().filter(name=name,user=user)
    conts=Content.objects.order_by("-created").all().filter(user=request.user)
    context={
            "cont":cont,
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
    cont=Content.objects.order_by("-created").all().filter(name=name,user=user)
    conts=Content.objects.order_by("-created").all().filter(user=request.user)
    context={
            "cont":cont,
            "conts":conts
        }
    return render(request,"single.html",context)

