from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import GestionMobiliaria

# Login function.
def signin(request):
    if request.method == 'GET':
        return render(request, 'home.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'home.html', {
                'form': AuthenticationForm,
                'error': 'El usuario o la contraseña son incorrectos'
            })
        else:
            login(request, user)
            return redirect('menu')


#Register function
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        #validates that the password is the same in both fields
        if request.POST['password1'] == request.POST['password2']:
            try:
                #register user
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('menu')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Las contraseñas no coinciden'
                })


# logout the session
def signout(request):
    logout(request)
    return redirect('signin')


def menu(request):
    return render(request, 'menu.html')


def mobiliario(request):
    mobiliario = GestionMobiliaria.objects.all()

    return render(request, 'Mobiliario/mobiliario.html', {
        'mobiliario' : mobiliario,
    })


def mobiliario_p(request):
    context = {}
    #table gestion mobiliaria inside a list
    mobiliario = GestionMobiliaria.objects.all()
    #getting inputs inside a list
    mobiliario_calcular = request.POST.getlist('calcular[]')
    
    subtotal = ['105', '90', '20', '12', '6', '4', '15', '0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
    """ for i in range(len(mobiliario_elegido)):
        if mobiliario_elegido[i] == "":
            mobiliario_elegido[i] = 0
        for j in mobiliario:
            subtotal.append(int(j.precio_renta) * int(mobiliario_elegido[i])) """

    my_list = zip(mobiliario, mobiliario_calcular, subtotal)
    context = {
        'my_list' : my_list
    }

    return render(request, 'Mobiliario/mobiliario_p.html', context)


def presupuesto(request):
    mobiliario_elegido = request.POST.getlist('mobiliario_elegido[]')
    subtotal_mobiliario = request.POST.getlist('subtotal_mobiliario[]')
    print(mobiliario_elegido)
    print(subtotal_mobiliario)

    return render(request, 'Presupuesto/presupuesto.html')
