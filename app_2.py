import folium
import pandas
data = pandas.read_csv("volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
def color_producer():
    return 'green'


map = folium.Map(location=[38.58,-99.09],zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat,lon,elev):
    print(type(el))
    fg.add_child(folium.Marker(location=[lt,ln],popup=str(el)+"m",icon=folium.Icon(color=color_producer())))

map.add_child(fg)

map.save("Map1.html")
 

