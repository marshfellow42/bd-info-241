import sqlite3
import webbrowser
import os

script_dir = os.path.realpath(os.path.dirname(__file__))

db_path = os.path.join(script_dir, 'projeto_BD.db')

conn = sqlite3.connect(db_path)

latitude_result = ""
longitude_result = ""

print("""1) IFCAMPUS
2) EscolaCampo
3) Assentamento""")
escolha = int(input("Do que você deseja saber? "))

def consulta_geral (nome_tabela):
    global latitude_result, longitude_result

    while True:
        consulta = conn.execute("SELECT nome FROM " + nome_tabela)

        x = 0

        for row in consulta:
            lista = row[0]
            x += 1
            print(x, ")", lista)
            
        id_muni = input("Qual lugar você deseja ver a localização? ")

        if int(id_muni) > x:
            print("Você não pode colocar um número maior do que está disponível")
            print("")
            continue

        lati = conn.execute("SELECT latitude FROM " + nome_tabela + " WHERE id=" + id_muni)

        for row in lati:
            if type(row[0]) == str:
                latitude = row[0]
            else:
                latitude = str(row[0])
            
        longi = conn.execute("SELECT longitude FROM " + nome_tabela + " WHERE id=" + id_muni)

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

match escolha:
    case 1:
        nome = "IFCAMPUS"
        consulta_geral(nome)
    case 2:
        nome = "ESCOLACAMPO"
        consulta_geral(nome)
    case 3:
        nome = "ASSENTAMENTO"
        consulta_geral(nome)

url = "https://epsg.io/map#srs=4326&x=" + latitude_result + "&y=" + longitude_result + "&z=19&layer=streets"

webbrowser.open(url, new=0)