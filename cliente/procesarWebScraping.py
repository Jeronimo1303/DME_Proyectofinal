from .models import WebScraping
import json

def promediarInstagram():
    registros = WebScraping.objects.all()
    sumarPublicaciones = 0
    sumarSeguidores = 0
    cont = 0
    for i in registros:
        if i.instagram is not None:
            diccionario = json.loads(i.instagram)
            publicaciones = diccionario.get('publicaciones', None)
            seguidores = diccionario.get('seguidores', None)
            sumarPublicaciones = publicaciones + sumarPublicaciones
            sumarSeguidores = seguidores + sumarSeguidores
            cont = cont + 1
    return sumarPublicaciones//cont, sumarSeguidores//cont
def promediarFacebook():
    registro = WebScraping.objects.all()
    sumarMeGusta = 0
    sumarSeguidores = 0
    cont = 0
    for i in registro:
        if i.facebook is not None:
            diccionario = json.loads(i.facebook)
            meGusta = diccionario.get('meGusta', None)
            seguidores = diccionario.get('seguidores', None)
            sumarMeGusta = meGusta + sumarMeGusta
            sumarSeguidores = seguidores + sumarSeguidores
            cont = cont + 1
    return sumarMeGusta//cont, sumarSeguidores//cont 
def promediarComputrabajo():
    registro = WebScraping.objects.all()
    sumarSeguidores = 0
    sumarPunGeneral = 0
    cont = 0
    for i in registro:
        if i.computrabajo is not None:
            diccionario = json.loads(i.computrabajo)
            seguidores = diccionario.get('seguidores', None)
            punGeneral = diccionario.get('punGeneral', None)
            sumarSeguidores = seguidores + sumarSeguidores
            sumarPunGeneral = punGeneral + sumarPunGeneral
            cont = cont + 1
    return sumarSeguidores//cont, sumarPunGeneral/cont
def calificarMarcaEmpleadora(nombreEmpresa):
    empresa = WebScraping.objects.get(name=nombreEmpresa)
    meGusta, seguidoresFacebook = promediarFacebook()
    publicaciones, seguidoresInstagram = promediarInstagram()
    seguidoresComputrabajo, punGeneral = promediarComputrabajo()
    puntos = 5.0
    if empresa.instagram is not None:
        diccInstagram = json.loads(empresa.instagram)
        publi = diccInstagram.get('publicaciones', None)
        seguiInstagram = diccInstagram.get('seguidores', None)
        if publi < publicaciones:
            puntos = puntos - 0.2
        if seguiInstagram < seguidoresInstagram:
            puntos = puntos - 0.2
    else:
        puntos = puntos - 0.5
    if empresa.facebook is not None:
        diccFacebook = json.loads(empresa.facebook)
        meGus = diccFacebook.get('meGusta', None)
        seguiFacebook = diccFacebook.get('seguidores', None)
        if meGus < meGusta:
            puntos = puntos - 0.2
        if seguiFacebook < seguidoresFacebook:
            puntos = puntos - 0.2
    else:
        puntos = puntos - 0.5
    if empresa.computrabajo is not None:
        diccComputrabajo = json.loads(empresa.computrabajo)
        seguiComputrabajo = diccComputrabajo.get('seguidores', None)
        punGene = diccComputrabajo.get('punGeneral', None)
        if seguiComputrabajo < seguidoresComputrabajo:
            puntos = puntos - 0.4
        if punGene < punGeneral:
            puntos = puntos - 0.4
    else:
        puntos = puntos - 1
    return round(puntos, 3)
















    
