import json
from datetime import date
import time
subject = "@lopezobrador_"
json_data = json.load(open(subject + ".json")) #"tweets.json" es la direccion donde se ubican los tweets minados

def daysSinceCreated():
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
    return tweetsPerDay > 100
print(daysSinceCreated())


