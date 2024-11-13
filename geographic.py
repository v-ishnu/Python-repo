"""
Represent geographic features (e.g., points, lines, polygons) as dictionaries with properties like location, color, and attributes. 
Operations: 
Create new features 

Find features within a specific region"""

# Feature = Weather, T.Dress, Flok, Fruit ---- Key
# Prop = location, color, --- values


Punjab = {'Weather': 'Extreme Hot', 'Dress': 'Pagdi', 'Dish': 'Lassi', 'Color': 'Orange'}
Maharashtra = {'Weather': 'Hot', 'Dress': 'Saree', 'Dish': '', 'Color': 'Orange'}

regions = {
    'Punjab': Punjab,
    'Maharashtra': Maharashtra
}

# Find specific region with feature
def findprop(prop, value):

match_prop = findprop(prop, value) 


