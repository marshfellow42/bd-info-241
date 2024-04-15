import sqlite3
import webbrowser

conn = sqlite3.connect('atividades/atividade-03/project_DB.db')

latitude_result = ""
longitude_result = ""

while True:
    consulta = conn.execute("SELECT nome FROM TB_MUNICIPIOS")

    x = 0

    for row in consulta:
        lista = row[0]
        x += 1
        print(x, ")", lista)
        
    id_muni = input("Qual município você deseja ver a localização?: ")
    
    if int(id_muni) > x:
        print("Você não pode colocar um número maior do que está disponível")
        print("")
        continue

    lati = conn.execute("SELECT latitude from TB_MUNICIPIOS WHERE id=" + id_muni)

    for row in lati:
        if type(row[0]) == str:
            latitude = row[0]
        else:
            latitude = str(row[0])
        
    longi = conn.execute("SELECT longitude from TB_MUNICIPIOS WHERE id=" + id_muni)

    for row in longi:
        if type(row[0]) == str:
            longitude = row[0]
        else:
            longitude = str(row[0])
        
    if (latitude == "") or (longitude == ""):
        print("Esse município ainda não foi completado")
        print("")
        continue
    else:
        latitude_result = latitude
        longitude_result = longitude
        break

url = "https://epsg.io/map#srs=4326&x=" + latitude_result + "&y=" + longitude_result + "&z=15&layer=streets"

webbrowser.open(url, new=0)