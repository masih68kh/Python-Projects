#%%
import folium

import pandas as pd
volcanoes = pd.read_csv("Volcanoes.txt")

mp = folium.Map(location=[43.527, -120.93],
                zoom_start=5)

fg = folium.FeatureGroup(name="My Map")
for coor , name in zip(zip(volcanoes['LAT'].values, volcanoes['LON'].values), volcanoes['NAME'].values):
    fg.add_child(folium.Marker(location=coor,popup=name,icon=folium.Icon('blue')))





#%%
# adding another layer to the map
fg.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig').read()))


mp.add_child(fg)
mp.save('maps.html')

#%%
