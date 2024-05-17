from cliente.webScraping import Webdriver
from cliente.models import *
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

def crearDataset():
    cont = 0
    registros = Empresa.objects.all()
    for i in registros:
        print(cont)
        cont = cont + 1
        userComputrabajo = i.usernameComputrabajo
        if userComputrabajo != None:
            if userComputrabajo.find('empresas/acerca-de-') != -1 or userComputrabajo.find('/') == -1:
                if userComputrabajo.find('empresas/acerca-de-') != -1:
                    user = userComputrabajo.replace('acerca-de', 'evaluaciones-en')
                else:
                    user = f'{userComputrabajo}/evaluaciones'
                url = f'https://co.computrabajo.com/{user}'
                driver = Webdriver()
                driver.get(url)
                try:
                    listaGeneral = []
                    general = driver.find_elements('//div[1]/div[3]/div[1]/div[4]/div/p[3]')
                    iterador = 8
                    for i in general:
                        if driver.find_elements(f'//div[1]/div[3]/div[1]/div[4]/div[{iterador}]/p[@class="fc_ok"]') != []:
                            listaGeneral.append(i.text)
                        iterador = iterador + 1
                    listaRecomienda = []
                    recomienda = driver.find_elements('//div[1]/div[3]/div[1]/div[4]/div/p[@class="fc_ok"]')
                    for i in recomienda:
                        listaRecomienda.append(i.text)
                    for i in range(len(listaGeneral)):
                        if len(listaGeneral[i]) > 3:
                            if listaRecomienda[i] == 'Recomienda trabajar aquí':
                                instanciaGeneral = ComentarioDataset(
                                    comentario = listaGeneral[i],
                                    etiqueta = 'positivo'
                                )
                            else:
                                instanciaGeneral = ComentarioDataset(
                                    comentario = listaGeneral[i],
                                    etiqueta = 'negativo'
                                )
                            instanciaGeneral.save()
                    loMejor = driver.find_elements('//div[1]/div[3]/div[1]/div[4]/div/p[4]/span')
                    for i in loMejor:
                        if len(i.text) > 3:
                            print(f'loMejor: {i.text}')
                            instanciaLoMejor = ComentarioDataset(
                                comentario = i.text,
                                etiqueta = 'lo mejor'
                            )
                            instanciaLoMejor.save()
                    aMejorar = driver.find_elements('//div[1]/div[3]/div[1]/div[4]/div/p[5]/span')
                    for i in aMejorar:
                        if len(i.text) > 3:
                            print(f'aMejorar: {i.text}')
                            instanciaAMejorar = ComentarioDataset(
                                comentario = i.text,
                                etiqueta = 'a mejorar'
                            )
                            instanciaAMejorar.save()
                except NoSuchElementException:
                    continue
def vectorizarComentario():
    #DataFrame
    df = pd.read_csv('.\cliente\comentario.csv', encoding='UTF-8')
    df = df.fillna('')    
    nltk.download('punkt')
    nltk.download('stopwords')
    stemmer = SnowballStemmer('spanish')
    def tokenizeStem(texto):
        tokens = word_tokenize(texto.lower())
        stems = [stemmer.stem(token) for token in tokens if token.isalpha()]
        return ' '.join(stems)
    df['comentarioStemmer'] = df['comentario'].apply(tokenizeStem)
    x = df['comentarioStemmer']
    y = df['etiqueta']
    xEntrenar, xProbar, yEntrenar, yProbar = train_test_split(x, y, test_size=0.2)
    vectorizar = CountVectorizer()
    xEntrenarVectorizar = vectorizar.fit_transform(xEntrenar)
    xProbarVectorizar = vectorizar.transform(xProbar)
    modelo = MultinomialNB()
    modelo.fit(xEntrenarVectorizar, yEntrenar)
    yPredecir = modelo.predict(xProbarVectorizar)
    print(metrics.accuracy_score(yProbar, yPredecir))





  

    



    






    

 