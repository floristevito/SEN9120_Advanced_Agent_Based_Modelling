import pandas as pd
import geopandas as gpd
import osmnx as ox

print("Test")
G = ox.graph_from_place('Netherlands', network_type='drive', custom_filter='["highway"]')
print("G loaded")
ox.save_graphml(G, 'roads.hml')