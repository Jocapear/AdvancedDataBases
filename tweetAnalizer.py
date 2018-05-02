import json
from datetime import date
import time


def tweetsPerDay(json_data):
    #mapear el mes con su numero
    numMonth = {"Jan": 1,
            "Feb": 2,
            "Mar" : 3,
            "Apr" : 4,
            "May" : 5,
            "Jun" : 6,
            "Jul" : 7,
            "Aug" : 8,
            "Sep" : 9,
            "Oct" : 10,
            "Nov" : 11,
            "Dec": 12}
    
    #obtener la fecha en que la cuenta fue creada
    fecha = json.loads(json_data["info"])["created_at"]
    
    lista = fecha.split()
    creationMonth = lista[1]
    creationDay = lista[2]
    creationYear = lista[5]
    
    #obtener fecha actual
    currentDate = (time.strftime("%d/%m/%Y")).split("/")
    currentMonth = currentDate[1]
    currentDay = currentDate[0]
    currentYear = currentDate[2]

    #transformas ambas fechas a tipo date
    currentDate = date(int(currentYear),int(currentMonth), int(currentDay))
    creationDate = date(int(creationYear),numMonth[creationMonth],int(creationDay))
    #creationDate = date(2010, 1, 1)

    #obtener el numero de dia a partir de que se creo la cuenta
    numDays = str(currentDate - creationDate)
    print(numDays)
    strDays = numDays.split()
    print(strDays)
    days = int(strDays[0])

    #obtener el numero de tweets desde que se creo la cuenta
    tweets = json.loads(json_data["info"])["statuses_count"]

    #obtener el numero de tweets por dia
    tweetsPerDay =(tweets/days)

    #si tiene mas de 100 regresa true
    return tweetsPerDay > 100

def usingHashtag(json_data) :
    list = {}

    for x in range (len(json_data["tweets"])):
        texto = json.loads(json_data["tweets"][x])["text"]
        texto = texto.split()
        for y in texto:
            if("#" in y):
                if(y not in list):
                    list[y] = 1
                else:
                    list[y] = list[y] + 1

    for key,value in sorted(list.items()):
        return(value > 10)



def sameTweet(json_data) :
    list = {}

    for x in range (len(json_data["tweets"])):
        texto = json.loads(json_data["tweets"][x])["text"]
        if(x not in list):
                list[x] = 1
            else:
                list[x] = list[x] + 1

    for key,value in sorted(list.items()):
        return(value > 1)
    


def isBot(subject_data):
    json_data = subject_data #"tweets.json" es la direccion donde se ubican los tweets minados

    porcentaje = 0

    if(tweetsPerDay(json_data)):
        porcentaje += 60
    if(usingHashtag(json_data)):
        porcentaje += 10
    if(sameTweet(json_data)):
        porcentaje += 30

    print("probabilidad de ser bot: " , porcentaje , "%")
    return porcentaje


#subject = "RicardoAnayaC"
#isBot(subject)


