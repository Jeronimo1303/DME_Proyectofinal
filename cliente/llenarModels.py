from .models import *
def llenarEmpresa():
    cont = 0
    for i in range(89, 109):
        cont = cont + 1
        print(cont)
        empresa = getMagneto(i+1)
        if empresa[1]!=None and empresa[2]!=None and empresa[3]!=None:
            try:
                modificarEmpresa = Empresa.objects.get(name=empresa[0])
                modificarEmpresa.usernameInstagram = empresa[1]
                modificarEmpresa.usernameFacebook = empresa[2]
                modificarEmpresa.usernameComputrabajo = empresa[3]
                modificarEmpresa.save()
            except Empresa.DoesNotExist:
                miModelo = Empresa(
                    name = empresa[0],
                    usernameInstagram = empresa[1],
                    usernameFacebook = empresa[2],
                    usernameComputrabajo = empresa[3]
                )
                miModelo.save()
        elif empresa[1]==None and empresa[2]==None and empresa[3]==None:
            try:
                modificarEmpresa = Empresa.objects.get(name=empresa[0])
            except Empresa.DoesNotExist:
                miModelo = Empresa(
                    name = empresa[0]
                )
                miModelo.save()
        elif empresa[1]==None and empresa[2]==None:
            try:
                modificarEmpresa = Empresa.objects.get(name=empresa[0])
                modificarEmpresa.usernameComputrabajo = empresa[3]
                modificarEmpresa.save()
            except Empresa.DoesNotExist:
                miModelo = Empresa(
                    name = empresa[0],
                    usernameComputrabajo = empresa[3]
                )
                miModelo.save()
        elif empresa[1]==None and empresa[3]==None:
            try:
                modificarEmpresa = Empresa.objects.get(name=empresa[0])
                modificarEmpresa.usernameFacebook = empresa[2]
                modificarEmpresa.save()
            except Empresa.DoesNotExist:
                miModelo = Empresa(
                    name = empresa[0],
                    usernameFacebook = empresa[2]
                )
                miModelo.save()
        elif empresa[2]==None and empresa[3]==None:
            try:
                modificarEmpresa = Empresa.objects.get(name=empresa[0])
                modificarEmpresa.usernameInstagram = empresa[1]
                modificarEmpresa.save()
            except Empresa.DoesNotExist:
                miModelo = Empresa(
                    name = empresa[0],
                    usernameInstagram = empresa[1]
                )
                miModelo.save()
        elif empresa[1]!=None and empresa[2]!=None:
            try:
                modificarEmpresa = Empresa.objects.get(name=empresa[0])
                modificarEmpresa.usernameInstagram = empresa[1]
                modificarEmpresa.usernameFacebook = empresa[2]
                modificarEmpresa.save()
            except Empresa.DoesNotExist:
                miModelo = Empresa(
                    name = empresa[0],
                    usernameInstagram = empresa[1],
                    usernameFacebook = empresa[2]
                )
                miModelo.save()
        elif empresa[1]!=None and empresa[3]!=None:
            try:
                modificarEmpresa = Empresa.objects.get(name=empresa[0])
                modificarEmpresa.usernameInstagram = empresa[1]
                modificarEmpresa.usernameComputrabajo = empresa[3]
                modificarEmpresa.save()
            except Empresa.DoesNotExist:
                miModelo = Empresa(
                    name = empresa[0],
                    usernameInstagram = empresa[1],
                    usernameComputrabajo = empresa[3]
                )
                miModelo.save()
        else:
            try:
                modificarEmpresa = Empresa.objects.get(name=empresa[0])
                modificarEmpresa.usernameFacebook = empresa[2]
                modificarEmpresa.usernameComputrabajo = empresa[3]
                modificarEmpresa.save()
            except Empresa.DoesNotExist:
                miModelo = Empresa(
                    name = empresa[0],
                    usernameFacebook = empresa[2],
                    usernameComputrabajo = empresa[3]
                )
                miModelo.save()
