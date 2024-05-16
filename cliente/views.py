from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import WebScraping,Empresa
from .procesarWebScraping import *
import json 

def index(request):
    return HttpResponse('<h2>Página de inicio<h2>')
def viewEmpresa(request, nameEmpresa):
    meGusta, seguidoresFacebook = promediarFacebook()
    publicaciones, seguidoresInstagram = promediarInstagram()
    seguidoresComputrabajo, punGeneral = promediarComputrabajo()
    puntos = calificarMarcaEmpleadora(nameEmpresa)
    empresa = get_object_or_404(WebScraping, name=nameEmpresa)
    
    if empresa.instagram != None or empresa.facebook != None or empresa.computrabajo != None:
        if empresa.instagram != None and empresa.facebook != None:
            instagram = json.loads(empresa.instagram)
            facebook = json.loads(empresa.facebook)
            if empresa.computrabajo != None:
                computrabajo = json.loads(empresa.computrabajo)
                acercaDe = empresa.acercaDe
                return render(request, 'empresaC.html', {'name': nameEmpresa,
                                                         'facebook': facebook, 
                                                         'instagram': instagram,
                                                         'computrabajo': computrabajo,
                                                         'acercaDe': acercaDe,
                                                         'meGusta': meGusta,
                                                         'seguidoresFacebook': seguidoresFacebook,
                                                         'publicaciones': publicaciones,
                                                         'seguidoresInstagram': seguidoresInstagram,
                                                         'seguidoresComputrabajo': seguidoresComputrabajo,
                                                         'punGeneral': punGeneral,
                                                         'puntos': puntos})
            else:
                return render(request, 'empresaP1.html', {'name': nameEmpresa,
                                                          'facebook': facebook, 
                                                          'instagram': instagram,
                                                          'meGusta': meGusta,
                                                          'seguidoresFacebook': seguidoresFacebook,
                                                          'publicaciones': publicaciones,
                                                          'seguidoresInstagram': seguidoresInstagram,
                                                          'puntos': puntos})
        elif empresa.computrabajo != None:
            computrabajo = json.loads(empresa.computrabajo)
            acercaDe = empresa.acercaDe
            return render(request, 'empresaP2.html', {'name': nameEmpresa,
                                                      'computrabajo': computrabajo,
                                                      'acercaDe': acercaDe,
                                                      'seguidoresComputrabajo': seguidoresComputrabajo,
                                                      'punGeneral': punGeneral,
                                                      'puntos': puntos})
        else:
            return render(request, 'empresa.html', {'name': nameEmpresa, 'puntos': puntos})
    else:
        return render(request, 'empresa.html', {'name': nameEmpresa, 'puntos': puntos})


def cliente(request):
    products_queryset = Empresa.objects.all()
    context = {
        'Empresas': products_queryset,
        'name' : "DME"
    }

    if request.method == 'POST':
        viewEmpresa(request,"ARUS")



    return render(request,'cliente.html',context)

        


