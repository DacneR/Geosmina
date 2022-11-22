from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.

def Index(request):
    
    if request.method == 'GET':
        return render(request, 'index.html',{
        'form': UserCreationForm
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                #register user
                Usuario = User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'])
                #Save user
                Usuario.save()
                return HttpResponse('Usuario creado')
            except:
                return HttpResponse('Usuario ya existe')
        return HttpResponse('Contraseñas no coinciden') 

    

def iniciar(request):

    


    return render(request, 'home.html')