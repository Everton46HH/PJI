import mysql.connector
import folium
import time
import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371000
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def atualizar_mapa():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Janeiro.01",
        database="PeTAG"
    )
    cursor = mydb.cursor()
    cursor.execute("SELECT latitude, longitude, nomePet FROM pet WHERE idPet = 1")
    resultado = cursor.fetchone()

    if resultado:
        latitude, longitude, nome_pet = resultado
        centro_lat, centro_lon = latitude, longitude
        mymap = folium.Map(location=[latitude, longitude], zoom_start=20)
        folium.Marker(location=[latitude, longitude], popup=f"{nome_pet}").add_to(mymap)
        raio = 50
        folium.Circle(
            location=[centro_lat, centro_lon],
            radius=raio,
            color='blue',
            fill=True,
            fill_color='lightblue'
        ).add_to(mymap)
        # distancia = haversine(centro_lat, centro_lon, latitude, longitude)
        # if distancia > raio:
        #     print(f"O pet {nome_pet} saiu do raio de {raio} metros!")
        # else:
        #     print(f"O pet {nome_pet} está dentro do raio :)"s)
        mymap.save("pet_location.html")
    cursor.close()
    mydb.close()

def loop_atualizacao(intervalo):
    while True:
        atualizar_mapa()
        time.sleep(intervalo)

loop_atualizacao(10)
