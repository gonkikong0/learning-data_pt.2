import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


#Exploring Data Structure
filename = "eq_data_30_day_m1.json"
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = "eq_data_readable.json"
with open(readable_file, "w") as f:
    json.dump(all_eq_data, f, indent=4)

#List of all the earthquakes

all_eq_dicts = all_eq_data['features']



mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

    

#Map the earthquakes.

# data = [Scattergeo(lon =lons, lat=lats)]
data = [{'type':'scattergeo',
         'lon': lons,
         'lat': lats,
         'text': hover_texts,
         'marker': {
             'size': [3*mag for mag in mags],
             'color' : mags,
             'reversescale' : True,
             'colorbar': {'title': 'Magnitude'},
         },
         }]
my_layout = Layout(title = 'Global Earthquakes, 2018')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = 'global_earthquakes.html')





