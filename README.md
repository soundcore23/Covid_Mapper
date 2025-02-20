# COVID-19 Vaccination & Death Rates in Washington State

## Overview
This project visualizes COVID-19 vaccination rates per 10K** as a choropleth map and COVID-19 deaths per 10K as proportional circles for each county in Washington State**. 

- The choropleth** represents full vaccination per 10K.
- The **symbol circles overlay represents COVID-19 deaths per 10K.
- **Hover interactions display county names and vaccination data when hovering over counties.
- Hovering over symbol circles reveals COVID-19 death rates per 10K.

## Technologies Used
- **Mapbox GL JS** for interactive mapping.
- **GeoJSON** for spatial data storage.
- **Python** (to compute county centroids from multipolygon geometries).

## Data Processing
- The county boundaries were stored as **multipolygons**.
- A **Python script** was used to compute the **centroids** of each county.
- The **choropleth** is based on a **GeoJSON file** containing county boundaries and vaccination data.
- The **symbol circle layer** is based on a **GeoJSON file** containing the computed centroids and death rate data.

Available at: https://soundcore23.github.io/Covid_Mapper/covidvaccination.html
