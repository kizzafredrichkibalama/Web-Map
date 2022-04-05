from flask import Flask
import folium


#Create flask object for this application
app = Flask(__name__)


#Define main view function
@app.route('/')
def index():
    # Define Uganda coordinates
    location = [0.4390, 33.2032]

    #Create new map 
    new_map = folium.Map(location=location, zoom_start=8, tiles="OpenStreetMap")

    #Add marker showing my current location
    folium.Marker(location=[0.4390, 33.2032], tooltip="Current Location",
     popup="<b>Jiinja, Ugaanda</b>").add_to(new_map)

    #Return folium HTML representation
    return new_map._repr_html_()


