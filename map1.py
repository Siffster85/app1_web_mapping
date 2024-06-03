import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])

def colour_set(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 2500:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[40.73, -114.07], zoom_start=6)

fg = folium.FeatureGroup(name="Test Map")

for lt, ln, nm, el in zip(lat, lon, name, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=7, popup=nm + " volcano elevation stands at " + str(el) + " metres above sea level.", fill_color=colour_set(el), color='black', fill_opacity=0.8))

map.add_child(fg)

map.save("Map1.html")