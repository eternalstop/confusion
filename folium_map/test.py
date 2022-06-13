import folium

print(folium.__version__)

# define the world map
world_map = folium.Map()
# save world map
world_map.save('test_01.html')
