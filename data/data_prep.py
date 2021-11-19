import pandas as pd
import geopandas as gpd
import osmnx as ox

G = ox.graph_from_place('Netherlands', network_type='drive', custom_filter='["highway"]')

ox.save_graphml(G, 'roads.hml')