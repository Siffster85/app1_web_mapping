import folium
map = folium.Map(location=[53.48, -2.24], zoom_start=12)

fg = folium.FeatureGroup(name="Test Map")

fg.add_child(folium.Marker(location=[53.46, -2.22], popup="Test Marker", icon=folium.Icon(color='blue')))

map.add_child(fg)

map.save("Map1.html")