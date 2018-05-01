import json
from datetime import date
import time
subject = "RicardoAnayaC"
json_data = json.load(open(subject + ".json")) #"tweets.json" es la direccion donde se ubican los tweets minados

def tweetsPerDay():
    #mapear el mes con su numero
    numMonth = {"Jan": 1,
            "Feb": 2,
            "Mar" : 3,
            "Apr" : 4,
            "May" : 5,
            "Jun" : 6,
            "Jul" : 7,
            "Ago" : 8,
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
    strDays = numDays.split()
    days = int(strDays[0])

    #obtener el numero de tweets desde que se creo la cuenta
    tweets = json.loads(json_data["info"])["statuses_count"]

    #obtener el numero de tweets por dia
    tweetsPerDay =(tweets/days)

    #si tiene mas de 100 regresa true
    return tweetsPerDay > 1

def usingHashtag() :
    list = {}
    for x in range (0, 20):
        texto = json.loads(json_data["tweets"][x])["text"]
        texto = texto.split()
        for y in texto:
            if("#" in y):
                if(y not in list):
                    list[y] = 1
                else:
                    list[y] = list[y] + 1

    for key,value in sorted(list.items()):
        return(value > 1)
    

print(tweetsPerDay())
print(usingHashtag())

porcentaje = 0

if(tweetsPerDay()):
    porcentaje += 65
if(usingHashtag()):
    porcentaje += 35

print("probabilidad de ser bot: " , porcentaje , "%")


