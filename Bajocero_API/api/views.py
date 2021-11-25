from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Registro
import json

# Create your views here.
class RegistroView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request,  *args , **kwargs ):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request,id=0):
        if(id>0):
            registros=list(Registro.objects.filter(id=id).values())
            if len(registros)>0:
                registro=registros[0]
                datos={'message': "Exito", 'registros':registro}
            else:
                datos={'message': "usuario no existe"} 
            return JsonResponse(datos)      
        else:    
            registros=list(Registro.objects.values())
            if len(registros)>0:
                datos={'message': "Exito", 'registros':registros}
            else:    
                datos={'message': "usuario no existe"}
            return JsonResponse(datos)
        
    def post(self, request):
        # print(request.body)
        jd=json.loads(request.body)
        # print(jd)
        Registro.objects.create(nombre=jd['nombre'],correo=jd['correo'],contraseña=jd['contraseña'])
        datos={'message': "Exito" }
        return JsonResponse(datos)
     
    def put(self, request,id):
        jd=json.loads(request.body)
        registros=list(Registro.objects.filter(id=id).values())
        if len(registros)>0:
            registro=Registro.objects.get(id=id)
            registro.nombre=jd['nombre']
            registro.correo=jd['correo']
            registro.contraseña=jd['contraseña']
            registro.save()
            datos={'message': "Exito" }
        else:
            datos={'message': "usuario no existe"} 
        return JsonResponse(datos) 
                
    def delete(self, request,id):
        registros=list(Registro.objects.filter(id=id).values())
        if len(registros)>0:
            Registro.objects.filter(id=id).delete()
            datos={'message': "Exito" }
        else:
            datos={'message': "usuario no existe"}
        return JsonResponse(datos)           