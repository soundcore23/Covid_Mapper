#The prop. symbols in the html file were not displaying properly due to the data format of the geometry (multipolygons). So, I decided to use the centroid of each region to represent the region in the map. This script generates a new GeoJSON file with the centroids of each region.

import geopandas as gpd
gdf = gpd.read_file("assets/wa_coviddata.geojson")
gdf["geometry"] = gdf.centroid
gdf.to_file("assets/wa_coviddata_centroids.geojson", driver="GeoJSON")
print("Centroids GeoJSON saved successfully!")
