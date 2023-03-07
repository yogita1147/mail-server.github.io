from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from mail.models import mail

def index(request):
    return render(request,'index.html')
def logincheck(request):
    var1 = request.POST['txtUsername']
    var2 = request.POST['Password']
    request.session['un'] = var1

    s = auth.authenticate(username=var1,password=var2)
    if s is not None:
        return render(request,'home.html',{'N':var1})

    else:
        return render(request, 'loginfail.html')

def compose(request):
 un=request.session['un']

 return render(request,'compose.html',{'N':un})
def compose1(request):
    un = request.session['un']
    var1 = request.session['un']
    var2 = request.POST['recipient']
    var3 = request.POST['subject']
    var4 = request.POST['content']
    p = mail()
    p.mailfrom=var1
    p.mailto=var2
    p.subject=var3
    p.contents=var4
    p.save()
    return render(request,'compose.html',{'N':un})
def inbox(request):
    un = request.session['un']
    var1 = request.session['un']
    p = mail.objects.filter(mailto=var1)
    return render(request,'inbox.html',{'P':p,'N': un})
def sent(request):
    un = request.session['un']
    var1 = request.session['un']
    p = mail.objects.filter(mailfrom=var1)
    return render(request,'sent.html',{'P':p,'N': un})
def logout(request):
    return redirect(index)

def newuser(request):
    return render(request,'newuser.html')
def newuser1(request):
    fname=request.POST['t1']
    lname=request.POST['t2']
    uname=request.POST['t3']
    password=request.POST['t4']
    email=request.POST['t5']
    user=User.objects.create_user(username=uname,password=password,first_name=fname,last_name=lname,email=email)
    user.save()
    return render(request,'index.html')
