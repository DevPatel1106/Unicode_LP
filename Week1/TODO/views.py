from imp import create_dynamic
from django.shortcuts import render,redirect
# Create your views here.
from django.http import HttpResponse
from .forms import UserRegistrationForm,createlistform,listupdateform,deletelistform
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import ToDoList,ToDoItem

def test(request):
    return HttpResponse("test works.")

def registration(request):
    if request.method == "POST":
        fm = UserRegistrationForm(request.POST)
        if fm.is_valid():
            user = fm.save()
            login(request,user)
            messages.success(request, "Registration successful." )
            # return redirect("")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    
    fm = UserRegistrationForm()
    context={"register_form":fm}
    return render (request,"registerform.html",context )

def view_login(request):
    if request.method =="POST":
        form =AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("mylists")
            else:
                messages.error(request,"Invalid username or PAssword") 
        else:
            messages.error(request,"Invalid username or Password") 
    
    form = AuthenticationForm()
    context={"login_form":form}
    return render (request,"loginform.html",context )

def mylists(request): 
    context={}
    user_lists= ToDoList.objects.filter(added_by_user=request.user)
    list_user_lists = [entry for entry in user_lists]
    # for entry in list_user_lists:
    #     user_list_items= ToDoItem.objects.filter(ToDoList=user_lists)
    #     list_user_list_items = [entry for entry in user_list_items]
    #     context ["user_list_items"]=list_user_list_items
    context ["user_lists"]=list_user_lists
    return render(request,"userlistdisplay.html",context)

def listadd(request):
    if request.method == "POST":
        form = createlistform(request.POST, request.FILES)
        if form.is_valid():
            title=form.cleaned_data.get('title')
            list=ToDoList.objects.get_or_create(title=form.cleaned_data['title'], added_by_user=request.user)
            # obj = Data.objects.get_or_create(Company=form.cleaned_data['Company'], info_about=form.cleaned_data['info_about'],api_data =api_response,count=0)
            return redirect("mylists")
    
    form = createlistform()
    context={"form":form}
    return render(request,"createlistform.html",context)

def listupdate(request):
    context={}

    if request.method == "POST":
        form = createlistform(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            
            # listtoupdate = ToDoList.objects.get(title=title)
            listtoupdateitems = ToDoItem.objects.get(title=title)
            # context["listtoupdateitems"]=listtoupdateitems
            list_listtoupdateitems = [entry for entry in listtoupdateitems]
            context = {"listtoupdateitems":list_listtoupdateitems}
    form2 = listupdateform()
    context["form2"]=form2
    
    if request.method == "GET":
        form3 = listupdateform(request.GET)
        if form3.is_valid():
            item=ToDoItem.objects.get_or_create(ToDoList=form3.cleaned_data['ToDoList'],title=form3.cleaned_data['title'],description=form3.cleaned_data['description'],CompletionStatus=form3.cleaned_data['CompletionStatus'],daysgiven=form3.cleaned_data['daysgiven'])
            return redirect("mylists")

    return render(request,"listupdate.html",context)
    # form = createlistform()
    # context["form"]=form
    # return render(request,"listupdate.html",context)

def listdelete(request,title):
    # context={}
    # if request.method == "POST":
    #     form = deletelistform(request.POST)
    #     if form.is_valid():
    #         title = form.cleaned_data.get('title')
    #         instance= ToDoList.objects.get(title=title)
    #         instance.delete()
    #         return redirect("mylists")
    
    # form = deletelistform()
    # context["form"]=form
    # return render(request,"deletelistform.html",context)

    instance= ToDoList.objects.get(title=title)
    instance.delete()
    return redirect("mylists")

    
