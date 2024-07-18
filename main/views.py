from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#from django.contrib.auth import user
from main.services import editar_user_sin_password, cambiar_password
# Create your views here.
@login_required
def home(req):
    return render(req, 'home.html')

@login_required
def profile(req):
    return render(req, 'profile.html')

@login_required
def edit_user(req):
    #obtener usuario actual
    current_user = req.user
    if req.POST['telefono'].strip() != '':
        editar_user_sin_password(
            current_user.username,
            req.POST['first_name'],
            req.POST['last_name'],
            req.POST['email'],
            req.POST['direccion'],
            req.POST['telefono'])
    else:
        editar_user_sin_password(
            current_user.username,
            req.POST['first_name'],
            req.POST['last_name'],
            req.POST['email'],
            req.POST['direccion'])
    messages.success(req, "Se actualizaron tus datos!")
    return redirect('/')
    #return HttpResponse('Se actualizaron tus datos!')
    #modificar atributos del user
    # current_user.first_name = req.POST['first_name']
    # current_user.last_name = req.POST['last_name']
    # current_user.email = req.POST['email']
    # #obtener atributos de user_profile a traves del related_naem
    # current_user.usuario.direccion = req.POST['direccion']
    # if req.POST['telefono'] != '':
    #     current_user.usuario.telefono = req.POST['telefono']
    # current_user.usuario.save()

def change_password(req):
    password =  req.POST['password']
    pass_repeat =  req.POST['pass_repeat']
    cambiar_password(req, password, pass_repeat)
    return redirect('/accounts/profile')
#pendientes para trabajar con grupos
# def solo_arrendadores(req):
#     return HttpResponse('sólo arrendadores')

# def solo_arrendatarios(req):
#     return HttpResponse('sólo arrendatarios')