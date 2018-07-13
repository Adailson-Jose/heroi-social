import folium
import pandas as pd
from folium import plugins

'''
mapa = folium.Map(location=[-15.788497,-47.879873],zoom_start=04)
folium.Marker([-19.9166813,-43.9344931]).add_to(mapa)
mapa.save("mapa1.html")
'''
'''
acidentes = pd.read_excel('acidentes-2015.xlsx',encoding='latin1')

latitude = acidentes['latitude'][:500].values
longitude = acidentes['longitude'][:500].values

mapa = folium.Map(location=[-8.05428,-34.8813],zoom_start=12)

for la,lo in zip(latitude,longitude):
    folium.Marker([la, lo]).add_to(mapa)

mapa.save("mapa2.html")

'''
semaforos = pd.read_excel('semaforos.txt',encoding='latin1')

latitude = semaforos['Latitude'][:500].values
longitude = semaforos['Longitude'][:500].values

mapa = folium.Map(location=[-8.05428,-34.8813],zoom_start=12)

for la,lo in zip(latitude,longitude):
    folium.Marker([la, lo]).add_to(mapa)

mapa.save("mapa-semaforos.html")


coordenadas = []
mapa_calor = folium.Map(location=[-8.05428,-34.8813],zoom_start=12)

for la,lo in zip(latitude,longitude):
    coordenadas.append([la,lo])

mapa_calor.add_child(plugins.HeatMap(coordenadas))
mapa_calor.save("mapa-semaforos-calor.html")

