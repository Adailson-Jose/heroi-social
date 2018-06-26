from flask import render_template
from app import app
import gviz_api

bancoDados = [
    ['Lat', 'Long', 'Name'],
    [37.4232, -122.0853, 'Work'],
    [37.4289, -122.1697, 'University'],
    [37.6153, -122.3900, 'Airport'],
    [37.4422, -122.1731, 'Shopping']
    ]

def main():
  # Creating the data
  description = {"lat": ("number", "Lat"),
                 "long": ("number", "Long"),
                 "name": ("string", "Name")}
  data = [{"lat":37.4232, "long":-122.0853, "name": "Work"},
          {"lat": 37.4289, "long": -122.1697, "name": "University"},
          {"lat": 37.6153, "long": -122.3900, "name": "Airport"},
          {"lat": 37.4422, "long": -122.1731, "name": "Shopping"}]

  # Loading it into gviz_api.DataTable
  data_table = gviz_api.DataTable(description)
  data_table.LoadData(data)

  ''''# Create a JavaScript code string.
  jscode = data_table.ToJSCode("jscode_data",
                               columns_order=("name", "salary", "full_time"),
                             order_by="salary")
   '''
  # Create a JSON string.
  json = data_table.ToJSon(columns_order=("lat", "long", "name"))

  return json

json_string = '{"estado":"São Paulo", "capital":"São Paulo"}'
json_string = '{"Lat", "Long", "Name"}, {37.4232, -122.0853,"Work"}'


'''def main():
    json_decodificado = json.loads(json_string)

    print("Objeto  Python: ", json_decodificado)

    json_codificado = json.dumps(json_decodificado)#Codifica para json
    print ("String json: ", json_codificado)

    print('Dados json:', type(json_codificado))
    print('Dados python :', type(json_decodificado))

    return json_codificado
'''
@app.route('/mapa-acidente')
def mapa_acidente():
    json = main()
    return render_template('mapa_acidente.html', title='Mapa de acidentes', set=json)
