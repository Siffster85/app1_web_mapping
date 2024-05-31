import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])

map = folium.Map(location=[40.73, -114.07], zoom_start=6)

fg = folium.FeatureGroup(name="Test Map")

for lt, ln, nm, el in zip(lat, lon, name, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=nm + " volcano elevation stands at " + str(el) + " metres", icon=folium.Icon(color='red')))

map.add_child(fg)

map.save("Map1.html")