from django.shortcuts import render,redirect
from .models import negocio
from .forms import CustomUserForm, negocioForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate

from rest_framework import viewsets
from .serializers import negocioSerializer

from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, HttpResponseBadRequest

from django.core import serializers
import json
from fcm_django.models import FCMDevice


# Create your views here.
@csrf_exempt
@require_http_methods(['POST'])
def guardar_token(request):
    body = request.body.decode('utf-8')
    bodyDict = json.loads(body)

    token = bodyDict['token']

    existe = FCMDevice.objects.filter(registration_id = token, active=True)

    if len(existe) > 0:
        return HttpResponseBadRequest(json.dumps({'mensaje':'el token ya existe'}))

    dispositivo = FCMDevice()
    dispositivo.registration_id = token
    dispositivo.active = True

    if request.user.is_authenticated:
        dispositivo.user = request.user
    try:
        dispositivo.save()
        return HttpResponse(json.dumps({'mensaje':'token guardado'}))
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':'no se ha podido guardar'}))

def home(request):
    return render(request, 'cori/home.html')

def registro_usuario(request):
    data = {
        'form' : CustomUserForm()
    }

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to = 'home')

    return render(request, 'registration/registrar.html', data)

def mis_negocios (request):

    negocio1 = negocio.objects.all()
    data = {
        'negocio1':negocio1
    }

    return render(request, 'cori/mis_negocios.html', data)
@login_required
@permission_required('cori.add_negocio')
def nuevo_negocio (request):
    data = {
        'form':negocioForm()
    }

    if request.method == 'POST':
        formulario = negocioForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()

           
            

            data['mensaje'] = 'guardado correctamente'
    return render(request, 'cori/nuevo_negocio.html', data )
@login_required
@permission_required('cori.change_negocio')
def modificar_negocio(request, id):
    negocio1 = negocio.objects.get(id=id)
    data = {
        'form': negocioForm(instance=negocio1)
    }

    if request.method == 'POST':
        formulario = negocioForm(data=request.POST, instance=negocio1, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "modificado correctamente"
            data['form'] = negocioForm(instance=negocio.objects.get(id=id))

    return render(request, 'cori/modificar_negocio.html', data)

@login_required
@permission_required('cori.delete_negocio')
def eliminar_negocio(request, id):
    negocio1 = negocio.objects.get(id=id)
    negocio1.delete()

    return redirect(to="mis negocios")


class negocioViewSet(viewsets.ModelViewSet):
    queryset = negocio.objects.all()
    serializer_class = negocioSerializer
