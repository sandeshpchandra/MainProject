from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect
from django.utils.datastructures import MultiValueDictKeyError

from FrontEnd.models import contactdb, useremployeedb,usersignupdb
from MainApp.models import employeedb, propertydb, propertytypedb, propertyareadb, selltypedb


# Create your views here.
def home(request):
    data=employeedb.objects.all()
    data1=propertydb.objects.all()
    data2=propertytypedb.objects.all()
    data3=propertyareadb.objects.all()
    data4=usersignupdb.objects.all()
    return render(request,"home.html",{'data':data,'data1':data1,'data2':data2,'data3':data3,'data4':data4})


def properties(request):
    data1 = propertydb.objects.all()
    return render(request,"properties.html",{'data1':data1})


def products(request,pro_name):
    data=propertydb.objects.filter(parea=pro_name)
    data2 = propertytypedb.objects.all()
    return render(request,"products.html",{'data':data,'data2':data2})



def singleproperty(request,proid):
    data=propertydb.objects.get(id=proid)
    return render(request,"singleproperty.html",{'data':data})

def singleagent(request,proid):
    data=employeedb.objects.get(id=proid)
    return render(request,"singleagent.html",{'data':data})

def aboutus(request):
    data=employeedb.objects.all()
    return render(request,"aboutus.html",{'data':data})


def contactus(request):
    return render(request,"contactus.html")

def savecontact(request):
    if request.method=='POST':
        cn=request.POST.get('cname')
        ce=request.POST.get('cemail')
        cu=request.POST.get('cnumber')
        ct=request.POST.get('cnationality')
        cs=request.POST.get('csubject')
        cm=request.POST.get('cmessage')
        obj=contactdb(cname=cn,cemail=ce,cnumber=cu,cnationality=ct,csubject=cs,cmessage=cm)
        obj.save()
        return redirect(contactus)



def rateus(request):
    return render(request,"rateus.html")

def loginout(request):
    return render(request,"loginout.html")


def savesignup(request):
    if request.method == 'POST':
        un = request.POST.get('uname')
        ub = request.POST.get('unumber')
        ue = request.POST.get('uemail')
        us = request.POST.get('eusername')
        up = request.POST.get('epassword')
        uc = request.POST.get('econfirmpass')

        obj1 = useremployeedb(uname=un, unumber=ub, uemail=ue, eusername=us, epassword=up, econfirmpass=uc)
        obj1.save()
        return redirect(loginout)



def editprofile(request,dataid):
    data7=usersignupdb.objects.get(id=dataid)
    return render(request, 'editprofile.html',{'data7':data7})


def filtertype(request,pro1_name):
    dataa=propertydb.objects.filter(ptype=pro1_name)
    data3 = propertytypedb.objects.all()
    return render(request,"filtertype.html",{'dataa':dataa,'data3':data3})



def userloginout(request):
    return render(request,"userloginout.html")


def saveusersignup(request):
    if request.method == 'POST':
        un = request.POST.get('uname')
        ub = request.POST.get('unumber')
        ue = request.POST.get('uemail')
        us = request.POST.get('uusername')
        up = request.POST.get('upassword')
        uc = request.POST.get('confirmpass')


        obj1 = usersignupdb(uname=un, unumber=ub, uemail=ue, uusername=us, upassword=up, confirmpass=uc)
        obj1.save()
        return redirect(userloginout)







def userlogin(request):
    if request.method=='POST':
        na=request.POST.get('user_name')
        pwd=request.POST.get('pass_word')




        if usersignupdb.objects.filter(uusername=na,upassword=pwd).exists():
            request.session['uusername']=na
            request.session['upassword']=pwd

            return redirect(home)
        elif useremployeedb.objects.filter(eusername=na,epassword=pwd).exists():
            request.session['eusername']=na
            request.session['epassword']=pwd
            return redirect(employeehome)
        else:
            return redirect(userloginout)
    else:
        return redirect(userloginout)







def userlogout(request):
    del request.session['uusername']
    del request.session['upassword']
    return redirect(userloginout)


def employeehome(request):
    data=employeedb.objects.all()
    data1=propertydb.objects.all()
    data2=propertytypedb.objects.all()
    data3=propertyareadb.objects.all()
    data4=usersignupdb.objects.all()
    return render(request,"employeehome.html",{'data':data,'data1':data1,'data2':data2,'data3':data3,'data4':data4})



def intrestshown(request):
    return render(request,"intrestshown.html")



def employeeupload(request):
    data = employeedb.objects.all()
    data1 = propertytypedb.objects.all()
    data2 = propertyareadb.objects.all()
    data3 = selltypedb.objects.all()
    return render(request, "employeeupload.html", {'data': data, 'data1': data1, 'data2': data2, 'data3': data3})




def saveproperty(request):
    if request.method=='POST':
        en=request.POST.get('pname')
        ea=request.POST.get('price')
        eg=request.POST.get('eemployee')
        pt=request.POST.get('ptype')
        pa=request.POST.get('parea')
        st=request.POST.get('stype')
        ed=request.POST.get('pdiscription')
        edi=request.POST.get('paddress')
        ew=request.POST.get('proom')
        em=request.POST.get('ptoilet')
        eb=request.POST.get('squarfeet')
        img=request.FILES['pimage']
        img1=request.FILES['pimage1']
        img2=request.FILES['pimage2']
        obj1=propertydb(pname=en,price=ea,eemployee=eg,ptype=pt,parea=pa,stype=st,pdiscription=ed,paddress=edi,proom=ew,ptoilet=em,squarfeet=eb,pimage=img,pimage1=img1,pimage2=img2)
        obj1.save()
        return redirect(employeeupload)




def myproperties(request):
    data1 = propertydb.objects.all()
    return render(request,"myproperties.html",{'data1':data1})




def updateuser(request, dataid):
    if request.method == 'POST':
        un = request.POST.get('uname')
        ub = request.POST.get('unumber')
        ue = request.POST.get('uemail')
        us = request.POST.get('uusername')
        up = request.POST.get('upassword')
        uc = request.POST.get('confirmpass')
        try:
            img=request.FILES['uimage']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = usersignupdb.objects.get(id=dataid).uimage
        usersignupdb.objects.filter(id=dataid).update(uname=un, unumber=ub, uemail=ue, uusername=us, upassword=up, confirmpass=uc,uimage=file)
        return redirect(editprofile)













