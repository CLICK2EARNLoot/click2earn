from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
from myapp.models import signup_table,usernametable,logintable



# Create your views here.

def home(request):
    return render(request,"html/index.html")

def about(request):
    return render(request,"html/about.html")

def contact(request):
    return render(request,"html/contact.html")
def signup(request):
    return render(request,"html/signup.html")
def login(request):
    return render(request,"html/login.html")
def payout(request):
    return render(request,"html/payout.html")
def sign_up(request):
    uname1 = request.POST.get("u_name")
    email1 = request.POST.get("e_mail")
    phone1 = request.POST.get("p_hone")
    pwd1 = request.POST.get("p_ass")
    pwd2 = request.POST.get("c_password")
    obj1 = signup_table.objects.filter(uname = uname1)
    obj2 = signup_table.objects.filter(email = email1)
    obj3 = signup_table.objects.filter(phone = phone1)
    if obj1.count()==0 :
        if obj2.count()==0:
            if obj3.count()==0:
                obj = signup_table(uname = uname1,email = email1,phone=phone1,pwd=pwd1)
                obj.save()
                dict_success = {'success':'Sign Up Success Login Now'}
                return HttpResponseRedirect(settings.BASEURL +'login',dict_success,)
            else:
                dict_data1={'error1':'Phone No. alrady exist please retry',"uname": uname1,"email":email1,"phone":phone1,"pass":pwd1,"rpass":pwd2}
                return render(request,"html/signup.html",dict_data1)
        else:
            dict_data2={'error2':'Email alrady exist please retry',"uname": uname1,"email":email1,"phone":phone1,"pass":pwd1,"rpass":pwd2}
            return render(request,"html/signup.html",dict_data2)
    else:
        dict_data3={'error3':'Username alrady exist please retry',"uname": uname1,"email":email1,"phone":phone1,"pass":pwd1,"rpass":pwd2}
        return render(request,"html/signup.html",dict_data3)

def log_in(request):
    uname = request.POST.get("uname")
    pwd = request.POST.get("pwd")
    obj = signup_table.objects.filter(uname = uname, pwd=pwd)
    if obj.count()>0 :
        request.session['user_id'] = 1
        return HttpResponseRedirect(settings.BASEURL +'about')
    else:
        dict_data={'error':'Username and Password does not exist'}
        return render(request,"html/login.html",dict_data)
   

     

