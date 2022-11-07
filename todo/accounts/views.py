from django.shortcuts import render,redirect
from accounts.forms import CustomUserCreationForm, LogInForm
# Create your views here.
from django.contrib.auth import login, authenticate, logout
# from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import CustomUser
from .managers import CustomUserManager
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# class customregistration(CreateView):
#     model = CustomUser
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy("mylists")
#     template_name = "CustomUserCreationForm.html"

#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'manager'
#         return super().get_context_data(**kwargs)
#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('mylists')

def customregistration(request):
    context={}
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            # form.save()
            # obj = CustomUser.objects.create_user(
            #     email = form.cleaned_data.get("email"),
            #     password = form.cleaned_data.get("password"))
            # obj.save()
            user = form.save(commit=False)
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user.save()
            login(request,user)
            messages.success(request, "Registration successful." )
            return redirect("/todoapp/mylists")
        #messages.error(request, "Unsuccessful registration. Invalid information.")
    form = CustomUserCreationForm()
    context["form"]=form
    return render (request,"CustomUserCreationForm.html",context )

def Customlogin(request):
    if request.method =="POST":
        form=LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user=authenticate(email=email,password=password)
            if user:
                login(request,user)
                # messages.info(request, f"You are now logged in as {email}.")
                return redirect("/todoapp/mylists")
            else:
                messages.error(request,"Invalid username or PAssword") 
        else:
            messages.error(request,"Invalid username or Password")
    form = LogInForm()
    context={"LogInForm":form}
    return render (request,"Customloginform.html",context )

@login_required
def Customlogout(request):
    useremail = request.user.email
    if useremail != None:
        logout(request)
        return redirect("/accounts/login")    

def adminsignin(request):
    context={}
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            # form.save()
            # obj = CustomUser.objects.create_user(
            #     email = form.cleaned_data.get("email"),
            #     password = form.cleaned_data.get("password"))
            # obj.save()
            # user = form.save(commit=False)            
            # user.save()
            # email = form.cleaned_data['email']
            # password = form.cleaned_data['password1']
            # user.save()
            user = form.save(commit=False)
            user.is_admin = True
            # user.useracc = request.user
            # user.is_admin=True
            print(user.username)
            user.save()
            login(request,user)
            messages.success(request, "Registration successful." )
            return redirect("/todoapp/mylists")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = CustomUserCreationForm()
    context["form"]=form
    return render (request,"CustomAdminCreationForm.html",context )

def agentsignin(request):
    context={}
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            # form.save()
            # obj = CustomUser.objects.create_user(
            #     email = form.cleaned_data.get("email"),
            #     password = form.cleaned_data.get("password"))
            # obj.save()
            # user = form.save()
            user = form.save(commit=False)
            # user.useracc = request.user
            user.is_agent=True
            user.save()
            login(request,user)
            # user = form.save(commit=False)
            # email = form.cleaned_data['email']
            # password = form.cleaned_data['password1']
            # user.is_agent = True
            # user.save()
            login(request,user)
            messages.success(request, "Registration successful." )
            return redirect("/todoapp/mylists")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = CustomUserCreationForm()
    context["form"]=form
    return render (request,"CustomAgentCreationForm.html",context )    


'''def adminsignin(request):
    context={}
    if request.method == "POST":
        form = AdminSignInForm(request.POST,request.FILES)
        if form.is_valid():
            # form.save()
            # obj = CustomUser.objects.create_user(
            #     email = form.cleaned_data.get("email"),
            #     password = form.cleaned_data.get("password"))
            # obj.save()
            # user = form.save(commit=False)            
            # user.save()
            # email = form.cleaned_data['email']
            # password = form.cleaned_data['password1']
            # user.is_admin = True
            # user.save()
            user = form.save(commit=False)
            # user.useracc = request.user
            # user.is_admin=True
            print(user.username)
            user.save()
            login(request,user)
            messages.success(request, "Registration successful." )
            return redirect("/todoapp/mylists")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = AdminSignInForm()
    context["form"]=form
    return render (request,"CustomAdminCreationForm.html",context )

def agentsignin(request):
    context={}
    if request.method == "POST":
        form = AgentSignInForm(request.POST,request.FILES)
        if form.is_valid():
            # form.save()
            # obj = CustomUser.objects.create_user(
            #     email = form.cleaned_data.get("email"),
            #     password = form.cleaned_data.get("password"))
            # obj.save()
            # user = form.save()
            user = form.save(commit=False)
            user.useracc = request.user
            # user.is_agent=True
            user.save()
            login(request,user)
            # user = form.save(commit=False)
            # email = form.cleaned_data['email']
            # password = form.cleaned_data['password1']
            # user.is_agent = True
            # user.save()
            login(request,user)
            messages.success(request, "Registration successful." )
            return redirect("/todoapp/mylists")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = AgentSignInForm()
    context["form"]=form
    return render (request,"CustomAgentCreationForm.html",context )    '''

