import folium
from folium import plugins
from folium.plugins import MarkerCluster
from folium.plugins import Draw

import shutil
import os

def moverArquivo(nomeDoArquivo, diretorio='app/tempalates'):
    if shutil.move(nomeDoArquivo + '.html', diretorio):
        print("Arquivo  MOVIDO da pasta controllers para template")
        return True
    return False

def deletarAquivo(nomeDoArquivo,  diretorio='app/tempalates'):
    dir = os.listdir(diretorio)
    for file in dir:
        if file == nomeDoArquivo + '.html':
            os.remove(file)
            print("Arquivo deletado com sucesso.")
            return True
    return False

def gerarMapadePonto(listaDeCoordenadas, nomeDoMapa):

    mapa = folium.Map(location=[-8.05428,-34.8813],zoom_start=12)
    marker_cluster = MarkerCluster().add_to(mapa)
    draw = Draw()
    draw.add_to(mapa)

    if listaDeCoordenadas != None:
        for la,lo, rua, in zip(listaDeCoordenadas[0],listaDeCoordenadas[1], listaDeCoordenadas[2]):
            folium.Marker(location=[la, lo], popup=rua, icon=folium.Icon(color='red')) .add_to(marker_cluster)
    mapa.save('app/templates/' + nomeDoMapa + ".html")

def gerarMapadeCalor(listaDeCoordenadas, nomeDoMapa):
    lCoordenadas = []
    mapa_calor = folium.Map(location=[-8.05428,-34.8813],zoom_start=12)
    print(len(listaDeCoordenadas[0]))
    if listaDeCoordenadas != None:
        for la,lo in zip(listaDeCoordenadas[0],listaDeCoordenadas[1]):
            lCoordenadas.append([la,lo])

        mapa_calor.add_child(plugins.HeatMap(lCoordenadas))
        mapa_calor.save('app/templates/' + nomeDoMapa + ".html")

