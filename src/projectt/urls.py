"""projectt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from auditapp import views
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('create', views.createView, name='create'),
    path('store', views.store, name='store'),
    path('data/', views.index,name='data'),
    path('view/<int:pk>', views.viewEmp, name='viewEmp'),
    path('delete/<int:pk>', views.deleteEmp, name='deleteEmp'),
    path('update/<int:pk>', views.updateView, name='updateEmp'),
    path('edit/<int:pk>', views.update, name='edit'),
    path('home/', views.landing, name='home'),
    path('choose/', views.choose, name='choose'),
    path('isago/', views.isago, name='isago'),
    path('iso/', views.iso, name='iso'),
    path('multistep/', views.multistep, name='multistep'),
    path('report/<str:pk>', views.report, name='report'),
    path('createaudit/', views.createAuditStandard, name='createaudit'),
    path('updateaudit/<str:pk>/', views.updateAuditStandard, name='updateaudit'),
    path('createaudit2/', views.createAuditRequirements, name='createaudit2'),
    path('dataa/', views.indexx,name='dataa'),
    # path('vieww/<str:pk>', views.viewaudit,name='vieww'),
    path('vieww/<str:pk>', views.viewaudit,name='vieww'),
    path('viewww/<str:pk>', views.gotochecklist,name='viewww'),
    path('email/', views.email, name='email'),
    path('emaill/', views.emaill, name='emaill'),
    path('pdf/<str:pk>', views.pdf, name='pdf'),
    path('cra/', views.CRA, name='cra'),
]