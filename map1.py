import folium
import pandas as pd
df=pd.read_csv("Volcanoes.txt")
#print(df)
lat=list(df['LAT'])
lon=list(df['LON'])
name=list(df['NAME'])
elev=list(df['ELEV'])
#print(lat)
#print(lon)


def color_producer(elevation):
    if(elevation>0 and elevation<=1500):
        return "red"
    elif(elevation>1500 and elevation<=3000):
        return "orange"
    else:
        return "blue"


map = folium.Map(location=[38.58, -99.09],zoom_start=5,tiles = "Stamen Terrain")
fg=folium.FeatureGroup(name="My Map")#Feature Group
for lt,ln,nm,elv in zip(lat,lon,name,elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=nm+" "+str(elv)+" m",fill_color=color_producer(elv),color="grey",fill_opacity=0.9))
map.add_child(fg)
map.save("Map1.html")