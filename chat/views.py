from django.shortcuts import render , redirect
from django.contrib.auth.models import User 
from.utils import generate_otp,sendEmail
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def send_otp(request):
    otp = generate_otp()
    request.session['otp'] = otp
    email = request.session['email']
    sendEmail(otp,email)
    return redirect ("verify_mail")


def home_page(request):
    return render(request,"chat/home_page.html")



def login_page(request):

    if request.method == "POST":

        username = request.POST.get('email').strip().lower()
        password = request.POST.get('password')
        print(username,password)

        user = authenticate(username=username, password = password)
        print(user)

        if user is not None:
            login(request,user)
            return redirect('dashboard')


        else:
            return render(request,"chat/login_page.html",{'error':"username or password doesnot match "})



    return render(request,"chat/login_page.html")


def register_page(request):

    if request.method == "POST":
        email = request.POST.get("email").strip().lower()
        password = request.POST.get("password").strip()
        confirm_password = request.POST.get("confirm-password").strip()
        # print(confirm_password)
        if password != confirm_password:
            return render(request,"chat/register_page.html",{'error':'password and confirm_password doesnot match'})
        
        emails = User.objects.all().values_list('email',flat=True)

        if email in emails:
            return render(request,"chat/register_page.html",{'error':'This email already exist'})
        

        request.session['email']=email
        request.session['password']=password
        
        return redirect('send_otp')

    return render(request,"chat/register_page.html")


def get_info(request):

    if request.method == 'POST':
        request.session['first_name']= request.POST.get('Fname')
        request.session['last_name'] = request.POST.get('Lname')
        request.session['dob'] = request.POST.get('date_of_birt')
        request.session['gender'] = request.POST.get('gender')
                
        return redirect("verify_mail")

    return render(request,"chat/get_info.html")



def veryfy_mail(request):

    if request.method == 'POST':
        otp = request.POST.get('otp').strip()
        
        if otp == request.session['otp']:

            user = User.objects.create_user(username=request.session['email'])
            user.set_password(request.session['password'])

            user.save()

            return redirect("get_info")


        else:
            return render(request,'chat/verify_mail.html',{'error':'the otp is doennot match'})
            
    return render(request,'chat/verify_mail.html')



@login_required(login_url='login_page')
def dashboard(request):

    if request.method == "POST":
        sender = request.user
        message = request.POST.get("message")
        chatroom = request.POST.get("chatroom")


    