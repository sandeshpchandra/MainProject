from django.urls import path

from FrontEnd import views

urlpatterns=[
    path('home/',views.home,name="home"),
    path('properties/',views.properties,name="properties"),
    path('products/<pro_name>/', views.products, name="products"),
    path('singleproperty/<int:proid>/',views.singleproperty,name="singleproperty"),
    path('singleagent/<int:proid>/',views.singleagent,name="singleagent"),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('contactus/',views.contactus,name="contactus"),
    path('savecontact/',views.savecontact,name="savecontact"),
    path('rateus/',views.rateus,name="rateus"),
    path('loginout/',views.loginout,name="loginout"),
    path('savesignup/',views.savesignup,name="savesignup"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('filtertype/<pro1_name>/', views.filtertype, name="filtertype"),
    path('userloginout/', views.userloginout, name="userloginout"),
    path('saveusersignup/', views.saveusersignup, name="saveusersignup"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('employeehome/', views.employeehome, name="employeehome"),
    path('intrestshown/', views.intrestshown, name="intrestshown"),
    path('employeeupload/', views.employeeupload, name="employeeupload"),
    path('saveproperty/', views.saveproperty, name="saveproperty"),
    path('myproperties/', views.myproperties, name="myproperties"),


]