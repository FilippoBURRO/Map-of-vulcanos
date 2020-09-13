import folium
import pandas

data=pandas.read_csv("Volcanoes_USA.txt") #sets file to readable variable
lat=list(data['LAT']) #gives variable name to carachteriscs contained in the file
lon=list(data['LON'])
elev=list(data['ELEV'])
type=list(data['TYPE'])


 tipo = {"Stratovolcano" or "Stratovolcanoes" : 'red',
     "Caldera" or "Maars" or "Maar" or "Calderas" : 'lightblue',
     "Volcanic field" : 'lightgreen',
     "Cinder cones" or "Cinder cone" : 'gray',
     "Lava domes" : 'black',
     "Fissure vents" : 'orange',
     "Shield volcano" or "Shield volcanoes" : 'lightbrown'} # defines a color palette based on the type of vulcano


map = folium.Map(location=[38, 15], zoom_start=2) # imports world map,defines map center and broadness of view

fgv = folium.FeatureGroup(name="Volcanoes")#defines a feature group for volcanoes

for lt, ln, el, tp in zip(lat, lon, elev, type):
    fgv.add_child(folium.CircleMarker(location=[lt, ln],
     radius = 8, popup=str(el)+" m", fill_color=tipo.get(tp,'blue'),
     color='grey' , fill=True, fill_opacity=0.8))#adds a loop defining the chracteristics of Volcanoes_USA.txt file and assigning custom style and color palette(defined earlier)


fgp = folium.FeatureGroup(name="population")#defines a feature group for population
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding ='utf-8-sig').read(),#opens a transparent polygon layer on top of the map with countries border (coordinates in file world.json)
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<8000000 #define color of polygon based on population of the country(file world.json)
else'orange' if 8000000<= x['properties']['POP2005']<90000000 else 'red' if 90000000<= x['properties']['POP2005']<800000000 else 'blue'}))

map.add_child(fgv)#features group of Volcanoes
map.add_child(fgp)#feature group of population
map.add_child(folium.LayerControl())#toogles the layer control

map.save("Map1.html")#opens or refreshes an HTML file to be opened by web broswer
