from django.db import models
import json
from django.db.models.signals import post_save 
from .webScraping import *

class Empresa(models.Model):
    name = models.CharField(max_length=100)
    usernameComputrabajo = models.CharField(max_length=100, blank=True, null=True)
    usernameInstagram = models.CharField(max_length=100, blank=True, null=True)
    usernameFacebook = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name 
class WebScraping(models.Model):
    name = models.CharField(max_length=100)
    instagram = models.JSONField(blank=True, null=True)
    facebook = models.JSONField(blank=True, null=True)
    computrabajo = models.JSONField(blank=True, null=True)
    acercaDe = models.TextField(null=True)
def activarWebScraping(sender, instance, **kwargs):
    if instance.usernameComputrabajo != None:
        acercaDe = getAcercaDe(instance.usernameComputrabajo)
    else:
        acercaDe = None
    if instance.usernameComputrabajo != None:
        computrabajo = getComputrabajo(instance.usernameComputrabajo)
    else:
        computrabajo = None
    if instance.usernameInstagram != None:
        instagram = getInstagram(instance.usernameInstagram)
    else:
        instagram = None
    if instance.usernameFacebook != None:
        facebook = getFacebook(instance.usernameFacebook)
    else:
        facebook = None
    print(f'Acerca de: {acercaDe}')
    print(f'Computrabajo: {computrabajo}')
    print(f'Instagram: {instagram}')
    print(f'Facebook: {facebook}')  
    if acercaDe!=None and computrabajo!=None and instagram!=None and facebook!=None:
        try:
            modificarWebScraping = WebScraping.objects.get(name=instance.name)
            modificarWebScraping.instagram = json.dumps({
                "publicaciones": instagram[0],
                "seguidores": instagram[1],
                "seguidos": instagram[2]
            })
            modificarWebScraping.facebook = json.dumps({
                "meGusta": facebook[0],
                "seguidores": facebook[1]
            })
            modificarWebScraping.computrabajo = json.dumps({
                "seguidores": computrabajo[0],
                "punGeneral": computrabajo[1],
                "evaluaciones": computrabajo[2],
                "porCinco": computrabajo[3],
                "porCuatro": computrabajo[4],
                "porTres": computrabajo[5],
                "porDos": computrabajo[6],
                "porUna": computrabajo[7],
                "ambienteTrabajo": computrabajo[8],
                "salarioPrestaciones": computrabajo[9],
                "oportunidadesCarrera": computrabajo[10],
                "directorGeneral": computrabajo[11],
                "porRecomiendan": computrabajo[12]
            })
            modificarWebScraping.acercaDe = acercaDe
            modificarWebScraping.save()
        except WebScraping.DoesNotExist:
            instanciaWebScraping = WebScraping(
                name = instance.name,
                computrabajo = json.dumps({
                    "seguidores": computrabajo[0],
                    "punGeneral": computrabajo[1],
                    "evaluaciones": computrabajo[2],
                    "porCinco": computrabajo[3],
                    "porCuatro": computrabajo[4],
                    "porTres": computrabajo[5],
                    "porDos": computrabajo[6],
                    "porUna": computrabajo[7],
                    "ambienteTrabajo": computrabajo[8],
                    "salarioPrestaciones": computrabajo[9],
                    "oportunidadesCarrera": computrabajo[10],
                    "directorGeneral": computrabajo[11],
                    "porRecomiendan": computrabajo[12]
                }),
                instagram = json.dumps({
                    "publicaciones": instagram[0],
                    "seguidores": instagram[1],
                    "seguidos": instagram[2]
                }),
                facebook = json.dumps({
                    "meGusta": facebook[0],
                    "seguidores": facebook[1]
                }),
                acercaDe = acercaDe
            )
            instanciaWebScraping.save()
    elif acercaDe==None and computrabajo==None and instagram==None and facebook==None:
        try:
            modificarWebScraping = WebScraping.objects.get(name=instance.name)
        except WebScraping.DoesNotExist:
            instanciaWebScraping = WebScraping(
                name = instance.name
            )
            instanciaWebScraping.save()
    elif acercaDe!=None and computrabajo!=None and instagram!=None and facebook==None:
        try:
            modificarWebScraping = WebScraping.objects.get(name=instance.name)
            modificarWebScraping.instagram = json.dumps({
                "publicaciones": instagram[0],
                "seguidores": instagram[1],
                "seguidos": instagram[2]
            })
            modificarWebScraping.computrabajo = json.dumps({
                "seguidores": computrabajo[0],
                "punGeneral": computrabajo[1],
                "evaluaciones": computrabajo[2],
                "porCinco": computrabajo[3],
                "porCuatro": computrabajo[4],
                "porTres": computrabajo[5],
                "porDos": computrabajo[6],
                "porUna": computrabajo[7],
                "ambienteTrabajo": computrabajo[8],
                "salarioPrestaciones": computrabajo[9],
                "oportunidadesCarrera": computrabajo[10],
                "directorGeneral": computrabajo[11],
                "porRecomiendan": computrabajo[12]
            })
            modificarWebScraping.acercaDe = acercaDe
            modificarWebScraping.save()
        except WebScraping.DoesNotExist:
            instanciaWebScraping = WebScraping(
                name = instance.name,
                computrabajo = json.dumps({
                    "seguidores": computrabajo[0],
                    "punGeneral": computrabajo[1],
                    "evaluaciones": computrabajo[2],
                    "porCinco": computrabajo[3],
                    "porCuatro": computrabajo[4],
                    "porTres": computrabajo[5],
                    "porDos": computrabajo[6],
                    "porUna": computrabajo[7],
                    "ambienteTrabajo": computrabajo[8],
                    "salarioPrestaciones": computrabajo[9],
                    "oportunidadesCarrera": computrabajo[10],
                    "directorGeneral": computrabajo[11],
                    "porRecomiendan": computrabajo[12]
                }),
                instagram = json.dumps({
                    "publicaciones": instagram[0],
                    "seguidores": instagram[1],
                    "seguidos": instagram[2]
                }),
                acercaDe = acercaDe
            )
            instanciaWebScraping.save()
    elif acercaDe==None and computrabajo!=None and instagram!=None and facebook!=None:
        try:
            modificarWebScraping = WebScraping.objects.get(name=instance.name)
            modificarWebScraping.computrabajo = json.dumps({
                "seguidores": computrabajo[0],
                "punGeneral": computrabajo[1],
                "evaluaciones": computrabajo[2],
                "porCinco": computrabajo[3],
                "porCuatro": computrabajo[4],
                "porTres": computrabajo[5],
                "porDos": computrabajo[6],
                "porUna": computrabajo[7],
                "ambienteTrabajo": computrabajo[8],
                "salarioPrestaciones": computrabajo[9],
                "oportunidadesCarrera": computrabajo[10],
                "directorGeneral": computrabajo[11],
                "porRecomiendan": computrabajo[12]
            })
            modificarWebScraping.instagram = json.dumps({
                "publicaciones": instagram[0],
                "seguidores": instagram[1],
                "seguidos": instagram[2]
            })
            modificarWebScraping.facebook = json.dumps({
                "meGusta": facebook[0],
                "seguidores": facebook[1]
            })
            modificarWebScraping.save()
        except WebScraping.DoesNotExist:
            instanciaWebScraping = WebScraping(
                name = instance.name,
                computrabajo = json.dumps({
                    "seguidores": computrabajo[0],
                    "punGeneral": computrabajo[1],
                    "evaluaciones": computrabajo[2],
                    "porCinco": computrabajo[3],
                    "porCuatro": computrabajo[4],
                    "porTres": computrabajo[5],
                    "porDos": computrabajo[6],
                    "porUna": computrabajo[7],
                    "ambienteTrabajo": computrabajo[8],
                    "salarioPrestaciones": computrabajo[9],
                    "oportunidadesCarrera": computrabajo[10],
                    "directorGeneral": computrabajo[11],
                    "porRecomiendan": computrabajo[12]
                }),
                instagram = json.dumps({
                    "publicaciones": instagram[0],
                    "seguidores": instagram[1],
                    "seguidos": instagram[2]
                }),
                facebook = json.dumps({
                    "meGusta": facebook[0],
                    "seguidores": facebook[1]
                })
            )
            instanciaWebScraping.save()
    elif acercaDe!=None and computrabajo==None and instagram!=None and facebook!=None:
        try:
            modificarWebScraping = WebScraping.objects.get(name=instance.name)
            modificarWebScraping.acercaDe = acercaDe
            modificarWebScraping.instagram = json.dumps({
                "publicaciones": instagram[0],
                "seguidores": instagram[1],
                "seguidos": instagram[2]
            })
            modificarWebScraping.facebook = json.dumps({
                "meGusta": facebook[0],
                "seguidores": facebook[1]
            })
            modificarWebScraping.save()
        except WebScraping.DoesNotExist:
            instanciaWebScraping = WebScraping(
                name = instance.name,
                acercaDe = acercaDe,
                instagram = json.dumps({
                    "publicaciones": instagram[0],
                    "seguidores": instagram[1],
                    "seguidos": instagram[2]
                }),
                facebook = json.dumps({
                    "meGusta": facebook[0],
                    "seguidores": facebook[1]
                })
            )
            instanciaWebScraping.save()
    elif acercaDe!=None and computrabajo!=None and instagram==None and facebook!=None:
        try:
            modificarWebScraping = WebScraping.objects.get(name=instance.name)
            modificarWebScraping.acercaDe = acercaDe
            modificarWebScraping.computrabajo = json.dumps({
                "seguidores": computrabajo[0],
                "punGeneral": computrabajo[1],
                "evaluaciones": computrabajo[2],
                "porCinco": computrabajo[3],
                "porCuatro": computrabajo[4],
                "porTres": computrabajo[5],
                "porDos": computrabajo[6],
                "porUna": computrabajo[7],
                "ambienteTrabajo": computrabajo[8],
                "salarioPrestaciones": computrabajo[9],
                "oportunidadesCarrera": computrabajo[10],
                "directorGeneral": computrabajo[11],
                "porRecomiendan": computrabajo[12]
            })
            modificarWebScraping.facebook = json.dumps({
                "meGusta": facebook[0],
                "seguidores": facebook[1]
            })
            modificarWebScraping.save()
        except WebScraping.DoesNotExist:
            instanciaWebScraping = WebScraping(
                name = instance.name,
                acercaDe = acercaDe,
                computrabajo = json.dumps({
                    "seguidores": computrabajo[0],
                    "punGeneral": computrabajo[1],
                    "evaluaciones": computrabajo[2],
                    "porCinco": computrabajo[3],
                    "porCuatro": computrabajo[4],
                    "porTres": computrabajo[5],
                    "porDos": computrabajo[6],
                    "porUna": computrabajo[7],
                    "ambienteTrabajo": computrabajo[8],
                    "salarioPrestaciones": computrabajo[9],
                    "oportunidadesCarrera": computrabajo[10],
                    "directorGeneral": computrabajo[11],
                    "porRecomiendan": computrabajo[12]
                }),
                facebook = json.dumps({
                    "meGusta": facebook[0],
                    "seguidores": facebook[1]
                })
            )
            instanciaWebScraping.save()
    elif acercaDe!=None and computrabajo!=None and instagram==None and facebook==None:
        try:
            modificarWebScraping = WebScraping.objects.get(name=instance.name)
            modificarWebScraping.computrabajo = json.dumps({
                "seguidores": computrabajo[0],
                "punGeneral": computrabajo[1],
                "evaluaciones": computrabajo[2],
                "porCinco": computrabajo[3],
                "porCuatro": computrabajo[4],
                "porTres": computrabajo[5],
                "porDos": computrabajo[6],
                "porUna": computrabajo[7],
                "ambienteTrabajo": computrabajo[8],
                "salarioPrestaciones": computrabajo[9],
                "oportunidadesCarrera": computrabajo[10],
                "directorGeneral": computrabajo[11],
                "porRecomiendan": computrabajo[12]
            })
            modificarWebScraping.acercaDe = acercaDe
            modificarWebScraping.save()
        except WebScraping.DoesNotExist:
            instanciaWebScraping = WebScraping(
                name = instance.name,
                computrabajo = json.dumps({
                    "seguidores": computrabajo[0],
                    "punGeneral": computrabajo[1],
                    "evaluaciones": computrabajo[2],
                    "porCinco": computrabajo[3],
                    "porCuatro": computrabajo[4],
                    "porTres": computrabajo[5],
                    "porDos": computrabajo[6],
                    "porUna": computrabajo[7],
                    "ambienteTrabajo": computrabajo[8],
                    "salarioPrestaciones": computrabajo[9],
                    "oportunidadesCarrera": computrabajo[10],
                    "directorGeneral": computrabajo[11],
                    "porRecomiendan": computrabajo[12]
                }),
                acercaDe = acercaDe
            )
            instanciaWebScraping.save()
    elif acercaDe!=None and computrabajo==None and instagram!=None and facebook==None:
        try:
            modificarWebScraping = WebScraping.objects.get(name=instance.name)
            modificarWebScraping.instagram = json.dumps({
                "publicaciones": instagram[0],
                "seguidores": instagram[1],
                "seguidos": instagram[2]
            })
            modificarWebScraping.acercaDe = acercaDe
            modificarWebScraping.save()
        except WebScraping.DoesNotExist:
            instanciaWebScraping = WebScraping(
                name = instance.name,
                instagram = json.dumps({
                    "publicaciones": instagram[0],
                    "seguidores": instagram[1],
                    "seguidos": instagram[2]
                }),
                acercaDe = acercaDe
            )
            instanciaWebScraping.save()
    elif acercaDe!=None and computrabajo==None and instagram==None and facebook!=None:
        try:
            modificarWebScraping = WebScraping.objects.get(name=instance.name)
            modificarWebScraping.facebook = json.dumps({
                "meGusta": facebook[0],
                "seguidores": facebook[1]
            })
            modificarWebScraping.acercaDe = acercaDe
            modificarWebScraping.save()
        except WebScraping.DoesNotExist:
            instanciaWebScraping = WebScraping(
                name = instance.name,
                facebook = json.dumps({
                    "meGusta": facebook[0],
                    "seguidores": facebook[1]
                }),
                acercaDe = acercaDe
            )
            instanciaWebScraping.save()
    elif acercaDe==None and computrabajo!=None and instagram!=None and facebook==None:
        try:
            modificarWebScraping = WebScraping.objects.get(name=instance.name)
            modificarWebScraping.instagram = json.dumps({
                "publicaciones": instagram[0],
                "seguidores": instagram[1],
                "seguidos": instagram[2]
            })
            modificarWebScraping.computrabajo = json.dumps({
                "seguidores": computrabajo[0],
                "punGeneral": computrabajo[1],
                "evaluaciones": computrabajo[2],
                "porCinco": computrabajo[3],
                "porCuatro": computrabajo[4],
                "porTres": computrabajo[5],
                "porDos": computrabajo[6],
                "porUna": computrabajo[7],
                "ambienteTrabajo": computrabajo[8],
                "salarioPrestaciones": computrabajo[9],
                "oportunidadesCarrera": computrabajo[10],
                "directorGeneral": computrabajo[11],
                "porRecomiendan": computrabajo[12]
            })
            modificarWebScraping.save()
        except WebScraping.DoesNotExist:
            instanciaWebScraping = WebScraping(
                name = instance.name,
                computrabajo = json.dumps({
                    "seguidores": computrabajo[0],
                    "punGeneral": computrabajo[1],
                    "evaluaciones": computrabajo[2],
                    "porCinco": computrabajo[3],
                    "porCuatro": computrabajo[4],
                    "porTres": computrabajo[5],
                    "porDos": computrabajo[6],
                    "porUna": computrabajo[7],
                    "ambienteTrabajo": computrabajo[8],
                    "salarioPrestaciones": computrabajo[9],
                    "oportunidadesCarrera": computrabajo[10],
                    "directorGeneral": computrabajo[11],
                    "porRecomiendan": computrabajo[12]
                }),
                instagram = json.dumps({
                    "publicaciones": instagram[0],
                    "seguidores": instagram[1],
                    "seguidos": instagram[2]
                })
            )
            instanciaWebScraping.save()
    elif acercaDe==None and computrabajo!=None and instagram==None and facebook!=None:
        try:
            modificarWebScraping = WebScraping.objects.get(name=instance.name)
            modificarWebScraping.facebook = json.dumps({
                "meGusta": facebook[0],
                "seguidores": facebook[1]
            })
            modificarWebScraping.computrabajo = json.dumps({
                "seguidores": computrabajo[0],
                "punGeneral": computrabajo[1],
                "evaluaciones": computrabajo[2],
                "porCinco": computrabajo[3],
                "porCuatro": computrabajo[4],
                "porTres": computrabajo[5],
                "porDos": computrabajo[6],
                "porUna": computrabajo[7],
                "ambienteTrabajo": computrabajo[8],
                "salarioPrestaciones": computrabajo[9],
                "oportunidadesCarrera": computrabajo[10],
                "directorGeneral": computrabajo[11],
                "porRecomiendan": computrabajo[12]
            })
            modificarWebScraping.save()
        except WebScraping.DoesNotExist:
            instanciaWebScraping = WebScraping(
                name = instance.name,
                computrabajo = json.dumps({
                    "seguidores": computrabajo[0],
                    "punGeneral": computrabajo[1],
                    "evaluaciones": computrabajo[2],
                    "porCinco": computrabajo[3],
                    "porCuatro": computrabajo[4],
                    "porTres": computrabajo[5],
                    "porDos": computrabajo[6],
                    "porUna": computrabajo[7],
                    "ambienteTrabajo": computrabajo[8],
                    "salarioPrestaciones": computrabajo[9],
                    "oportunidadesCarrera": computrabajo[10],
                    "directorGeneral": computrabajo[11],
                    "porRecomiendan": computrabajo[12]
                }),
                facebook = json.dumps({
                    "meGusta": facebook[0],
                    "seguidores": facebook[1]
                })
            )
            instanciaWebScraping.save()
    elif acercaDe==None and computrabajo==None and instagram!=None and facebook!=None:
        try:
            modificarWebScraping = WebScraping.objects.get(name=instance.name)
            modificarWebScraping.instagram = json.dumps({
                "publicaciones": instagram[0],
                "seguidores": instagram[1],
                "seguidos": instagram[2]
            })
            modificarWebScraping.facebook = json.dumps({
                "meGusta": facebook[0],
                "seguidores": facebook[1]
            })
            modificarWebScraping.save()
        except WebScraping.DoesNotExist:
            instanciaWebScraping = WebScraping(
                name = instance.name,
                instagram = json.dumps({
                    "publicaciones": instagram[0],
                    "seguidores": instagram[1],
                    "seguidos": instagram[2]
                }),
                facebook = json.dumps({
                    "meGusta": facebook[0],
                    "seguidores": facebook[1]
                })
            )
            instanciaWebScraping.save()
    elif acercaDe!=None and computrabajo==None and instagram==None and facebook==None:
        try:
            modificarWebScraping = WebScraping.objects.get(name=instance.name)
            modificarWebScraping.acercaDe = acercaDe
            modificarWebScraping.save()
        except WebScraping.DoesNotExist:
            instanciaWebScraping = WebScraping(
                name = instance.name,
                acercaDe = acercaDe
            )
            instanciaWebScraping.save()
    elif acercaDe==None and computrabajo!=None and instagram==None and facebook==None:
        try:
            modificarWebScraping = WebScraping.objects.get(name=instance.name)
            modificarWebScraping.computrabajo = json.dumps({
                "seguidores": computrabajo[0],
                "punGeneral": computrabajo[1],
                "evaluaciones": computrabajo[2],
                "porCinco": computrabajo[3],
                "porCuatro": computrabajo[4],
                "porTres": computrabajo[5],
                "porDos": computrabajo[6],
                "porUna": computrabajo[7],
                "ambienteTrabajo": computrabajo[8],
                "salarioPrestaciones": computrabajo[9],
                "oportunidadesCarrera": computrabajo[10],
                "directorGeneral": computrabajo[11],
                "porRecomiendan": computrabajo[12]
            })
            modificarWebScraping.save()
        except WebScraping.DoesNotExist:
            instanciaWebScraping = WebScraping(
                name = instance.name,
                computrabajo = json.dumps({
                    "seguidores": computrabajo[0],
                    "punGeneral": computrabajo[1],
                    "evaluaciones": computrabajo[2],
                    "porCinco": computrabajo[3],
                    "porCuatro": computrabajo[4],
                    "porTres": computrabajo[5],
                    "porDos": computrabajo[6],
                    "porUna": computrabajo[7],
                    "ambienteTrabajo": computrabajo[8],
                    "salarioPrestaciones": computrabajo[9],
                    "oportunidadesCarrera": computrabajo[10],
                    "directorGeneral": computrabajo[11],
                    "porRecomiendan": computrabajo[12]
                })
            )
            instanciaWebScraping.save()
    elif acercaDe==None and computrabajo==None and instagram!=None and facebook==None:
        try:
            modificarWebScraping = WebScraping.objects.get(name=instance.name)
            modificarWebScraping.instagram = json.dumps({
                "publicaciones": instagram[0],
                "seguidores": instagram[1],
                "seguidos": instagram[2]
            })
            modificarWebScraping.save()
        except WebScraping.DoesNotExist:
            instanciaWebScraping = WebScraping(
                name = instance.name,
                instagram = json.dumps({
                    "publicaciones": instagram[0],
                    "seguidores": instagram[1],
                    "seguidos": instagram[2]
                })
            )
            instanciaWebScraping.save()
    else:
        try:
            modificarWebScraping = WebScraping.objects.get(name=instance.name)
            modificarWebScraping.facebook = json.dumps({
                "meGusta": facebook[0],
                "seguidores": facebook[1]
            })
            modificarWebScraping.save()
        except WebScraping.DoesNotExist:
            instanciaWebScraping = WebScraping(
                name = instance.name,
                facebook = json.dumps({
                    "meGusta": facebook[0],
                    "seguidores": facebook[1]
                })
            )
            instanciaWebScraping.save() 
post_save.connect(activarWebScraping, sender=Empresa)

        




    








