import folium
import pandas as pd
data=pd.read_csv("volcanoes.txt")
lon=list(data['LON'])
lat=list(data['LAT'])
elev=list(data['ELEV'])
map=folium.Map(location=[33.9503449,11.4613988],zoom_start=7,tiles="Stamen Terrain",min_zoom=2.5 )
fg=folium.FeatureGroup(name='Volcanoes')
for lt,ln,el in zip(lat,lon,elev):
    color ='red'
    if el<2000: 
        color='green'
    elif el <3000:
        color='orange'
    fg.add_child(folium.CircleMarker(location=[lt,ln],raduis=6,
    popup='elevation: '+str(el),fill_color=color,fill_opacity=0.7,color='grey'))
fgp=folium.FeatureGroup(name='Population')
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function= lambda x:{'fillColor':'red' if x['properties']['POP2005']>15000000 else 'green'}))
map.add_child(fgp)
map.add_child(fg)
map.add_child(folium.LayerControl())
map.save('Map.html')

