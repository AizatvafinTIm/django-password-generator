from django.shortcuts import render
import random
# Create your views here.


def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

def password(request):
    alpha = list('qwertyuiopasdfghjklzxcvbnm')
    length = int(request.GET.get('length'))
    if (request.GET.get('uppercase')):
        alpha.extend('QWERTYUIOPASDFGHJKLZXCVBNM')
    if (request.GET.get('special')):
        alpha.extend('`!@#$%^&*()')
    if (request.GET.get('numbers')):
        alpha.extend('1234567890')
    thepassword = ''
    for i in range(length):
        thepassword += random.choice(alpha)


    return render(request, 'password.html', {'password': thepassword})