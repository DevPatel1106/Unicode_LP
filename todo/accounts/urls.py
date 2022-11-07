from django.contrib import admin
from django.urls import path,include
from .views import customregistration
from . import views
from django.conf import settings 
from django.conf.urls.static import static
urlpatterns = [
    # path('register/',customregistration.as_view(), name='registeration'),
    path('register/',views.customregistration, name='registeration'),
    path('login/', views.Customlogin, name='login'),
    path('logout/', views.Customlogout, name='logout'),
    path('register/admin/', views.adminsignin, name='admin_registeration'),
    path('register/agent/', views.agentsignin, name='agent_registeration'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)