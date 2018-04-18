import json
from datetime import date
import time
subject = "@lopezobrador_"
json_data = json.load(open(subject + ".json")) #"tweets.json" es la direccion donde se ubican los tweets minados

print("+++++++++++++++++++++++++++++++++++++++++++")
fecha = json.loads(json_data["info"])["created_at"]

lista = fecha.split()
creationMonth = lista[1]
creationDay = lista[2]
creationYear = lista[5]

#print(mes + dia + año)


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

#creationMonth = "Oct"
#creationDay = "13"
#creationYear = "2009"

currentDate = (time.strftime("%d/%m/%Y")).split("/")
currentMonth = currentDate[1]
currentDay = currentDate[0]
currentYear = currentDate[2]

currentDate = date(int(currentYear),int(currentMonth), int(currentDay))
creationDate = date(int(creationYear),numMonth[creationMonth],int(creationDay))
numDays = str(currentDate - creationDate)
strDays = numDays.split()
days = int(strDays[0])
print(days)

