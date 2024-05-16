from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from googlesearch import search

class Webdriver:
    def __init__(self):
        edgeOptions = Options()
        edgeOptions.add_argument('--incognito')
        self.driver = webdriver.Edge(options=edgeOptions)
    def get(self, url):
        self.driver.get(url)
        self.driver.minimize_window()
    def find_element(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)
    def find_elements(self, xpath):
        return self.driver.find_elements(By.XPATH, xpath)
    def click(self, xpath):
        c = self.find_element(xpath)
        c.click()
    def implicitly_wait(self):
        self.driver.implicitly_wait(10)

def getAcercaDe(user):
    listaAcercaDe = []
    driver = Webdriver()
    url = f'https://co.computrabajo.com/{user}'
    #url = 'https://co.computrabajo.com/postobon'
    driver.get(url)
    try:
        xpath = driver.find_elements('//div[2]/div[1]/div[3]/div[1]/div/div[1]/p')
        if xpath == []:
            xpath = driver.find_elements('//div[1]/div[2]/article/div/div/p')
    except NoSuchElementException:
        return None
    paragraph = ''
    for i in xpath:
        paragraph += f'{i.text}\n'
    paragraph = paragraph[:-1]
    if len(paragraph) > 10:
        return paragraph
    return None
def getComputrabajo(user):
    listaComputrabajo = []
    driver = Webdriver()
    url = f'https://co.computrabajo.com/{user}'
    #url = 'https://co.computrabajo.com/postobon'
    try:
        driver.get(url)
        seguidores = driver.find_element('/html/body/main/div[1]/div/div[2]/div[2]/span')
        strSeguidores = seguidores.text
        strSeguidores = strSeguidores[:strSeguidores.find('seguidores')-1]
        strSeguidores = int(strSeguidores.replace('.', ''))
        listaComputrabajo.append(strSeguidores)
        punEvaluaciones = driver.find_elements('//div[1]/div/div[1]/div/div[@class="pr10 mbB_m"]/p')
        for i in punEvaluaciones:
            listaComputrabajo.append(i.text)
        if len(listaComputrabajo)>1:
            listaComputrabajo[1] = float(listaComputrabajo[1].replace(',', '.'))
        porcentajes = driver.find_elements('//div[1]/div/div[1]/div/ul/li/div[2]/div/p')
        for i in porcentajes:
            listaComputrabajo.append(int(i.text[:-1]))
        puntuaciones = driver.find_elements('//div[1]/div/div[2]/ul/li/div/p')
        for i in range(0, len(puntuaciones), 2):
            concatenar = f"{puntuaciones[i].text} {puntuaciones[i+1].text}"
            listaComputrabajo.append(concatenar)
        porRecomiendan = driver.find_element('//div[1]/span/strong')
        listaComputrabajo.append(porRecomiendan.text)
        subtitle = driver.find_elements('//div[1]/div[3]/div[1]/div[2]/article/div/span')
        for i in subtitle:
            listaComputrabajo.append(i.text)
        p = driver.find_elements('//div[1]/div[3]/div[1]/div[2]/article/div/div/p')
        for i in p:
            listaComputrabajo.append(i.text)
        if listaComputrabajo!=[]:
            return listaComputrabajo
        return None
    except NoSuchElementException:
        return None
def getFacebook(user):
    listaFacebook = []
    driver = Webdriver()
    url = f'https://www.facebook.com/{user}'
    #url = 'https://www.facebook.com/Postobon'
    try:
        driver.get(url)
        driver.implicitly_wait()
        driver.click('//div/div[1]/div[@aria-label="Cerrar"]/i')
        facebook = driver.find_elements('//div[3]/div/div/div[2]/span/a')
        if facebook != []:
            for i in facebook:
                listaFacebook.append(i.text)
            if listaFacebook[0].find('Me')==-1:
                return None
            if listaFacebook[0].find('mil')!=-1:
                listaFacebook[0] = listaFacebook[0][:listaFacebook[0].find('mil')-1]
                if listaFacebook[0].find(',')!=-1:
                    listaFacebook[0] = listaFacebook[0].replace(',', '.')
                listaFacebook[0] = int(float(listaFacebook[0])*1000)
            else:
                listaFacebook[0] = listaFacebook[0][:listaFacebook[0].find('Me')-1]
                listaFacebook[0] = int(float(listaFacebook[0]))
            if listaFacebook[1].find('mil')!=-1:
                listaFacebook[1] = listaFacebook[1][:listaFacebook[1].find('mil')-1]
                if listaFacebook[1].find(',')!=-1:
                    listaFacebook[1] = listaFacebook[1].replace(',', '.')
                listaFacebook[1] = int(float(listaFacebook[1])*1000)
            else:
                listaFacebook[1] = listaFacebook[1][:listaFacebook[1].find('seguidores')-1]
                listaFacebook[1] = int(float(listaFacebook[1]))
            return listaFacebook
        else:
            return None
    except NoSuchElementException:
        return None
def getTwitter(user):
    if user:
        aux = []
        driver = Webdriver()
        url = f'https://twitter.com/{user}'
        #url = 'https://twitter.com/postobonoficial'
        driver.get(url)
        twitter = driver.find_elements('//div/div[5]/div/a/span[1]/span')
        for i in twitter:
            aux.append(i.text)
        return aux
    return None
def getInstagram(user):
    listaInstagram = []
    driver = Webdriver()
    url = f'https://www.instagram.com/{user}'
    #url = 'https://www.instagram.com/postobonempresa'
    try: 
        driver.get(url)
        driver.implicitly_wait()
        instagram = driver.find_elements('//ul/li/button/span/span')
        if instagram != []:
            for i in instagram:
                listaInstagram.append(i.text)
            listaInstagram[0] = int(float(listaInstagram[0]))
            if listaInstagram[1].find('mil')!=-1:
                listaInstagram[1] = listaInstagram[1][:listaInstagram[1].find('mil')-1]
                if listaInstagram[1].find(',')!=-1:
                    listaInstagram[1] = listaInstagram[1].replace(',', '.')
                listaInstagram[1] = int(float(listaInstagram[1])*1000)
            elif listaInstagram[1].find('M')!=-1:
                listaInstagram[1] = listaInstagram[1][:listaInstagram[1].find('M')-1]
                if listaInstagram[1].find(',')!=-1:
                    listaInstagram[1] = listaInstagram[1].replace(',', '.')
                listaInstagram[1] = int(float(listaInstagram[1])*1000000)
            else:
                listaInstagram[1] = int(float(listaInstagram[1]))
            return listaInstagram
        else:
            return None
    except NoSuchElementException:
        return None
def getMagneto(num):
    driver = Webdriver()
    url = 'https://www.magneto365.com/co/empresas'
    driver.get(url)
    registro = []
    nombreEmpresa = driver.find_element(f'//section/main/div/a[{num}]/div/h3')
    nombreEmpresa = nombreEmpresa.text[12:]
    registro.append(nombreEmpresa)
    print(nombreEmpresa)
    #Instagram
    buscarInstagram = f'Instagram de {nombreEmpresa}'
    inst = next(search(buscarInstagram, start=0, pause=2))
    if inst.find('/?hl=')!=-1:
        inst = inst[:inst.find('/?hl=')]
    if inst[-1]=='/':
        inst = inst[:-1]
    #Facebook
    buscarFacebook = f'Facebook de {nombreEmpresa}'
    face = next(search(buscarFacebook, start=0, pause=2))
    if face.find('/?locale=es_LA')!=-1:
        face = face.replace('/?locale=es_LA', '')
    if face[-1]=='/':
        face = face[:-1]
    #Computrabajo
    buscarComputrabajo = f'Computrabajo de {nombreEmpresa}'
    comp = next(search(buscarComputrabajo, start=0, pause=2))
    if comp.find('/empleos')!=-1:
        comp = comp.replace('/empleos', '')
    if comp.find('ofertas-de-trabajo')!=-1:
        comp = comp.replace('ofertas-de-trabajo', 'acerca')
    #Instagram
    if inst.find('instagram')!=-1 and inst.find('tv/')==-1 and inst.count('/')<5:
        pi = inst.find('instagram.com/')
        inst = inst[pi+len('instagram.com/'):]
        registro.append(inst)
        print(inst)
    else:
        registro.append(None)
        print(None)
    #Facebook
    if face.find('facebook')!=-1 and face.find('php?')==-1 and face.find('/help')==-1 and face.count('/')<5:
        pf = face.find('facebook.com/')
        face = face[pf+len('facebook.com/'):]
        registro.append(face)
        print(face)
    else:
        registro.append(None)
        print(None)  
    #Computrabajo
    if comp.find('computrabajo')!=-1 and comp.find('trabajo-')==-1 and comp.find('evaluaciones-')==-1 and comp.count('/')<5:
        pc = comp.find('computrabajo.com/')
        comp = comp[pc+len('computrabajo.com/'):]
        registro.append(comp)
        print(comp)
    else:
        registro.append(None)
        print(None)
    return registro
