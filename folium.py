import folium

# Create a map object
mymap = folium.Map(location=[3.9356, 41.8551], zoom_start=12, tiles="Stamen Terrain")

# Add a marker to the map
folium.Marker(location=[3.9356, 41.8551], popup="My Location", icon=folium.Icon(color="red")).add_to(mymap)

# Save the map to an HTML file
mymap.save("mymap.html")