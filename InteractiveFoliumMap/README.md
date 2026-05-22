# Launch Sites Locations Analysis with Folium

The launch success rate may depend on the location and attributes of the launch site — specifically, the initial position of rocket trajectories. This notebook uses interactive visual map analytics to discover factors about launch location that may contribute to successful outcomes.

---

## Contents

- Mark all SpaceX launch sites on a map
- Mark all launch outcomes (successful/failed launches) for each site on the map
- Calculate and mark the distance between a launch site and its surrounding infrastructure:
  - Distance to Closest Coastline
  - Distance to Closest City
  - Distance to Closest Railway

---

## Requirements

Install the following before running the notebook:

```bash
pip install folium wget pandas numpy
```

---

## Dataset

The notebook automatically downloads the dataset on first run:

- **spacex_launch_geo.csv** — SpaceX launch records augmented with coordinates for each launch site

> Note: Running the notebook multiple times will download additional copies (`spacex_launch_geo (1).csv`, etc.). You can safely delete the numbered duplicates and keep only the original.

---

## Output Maps

The notebook saves the following interactive HTML maps to your working directory. Open them in any browser to explore:

| File | Description |
|------|-------------|
| [map_marker.html](https://htmlpreview.github.io/?https://github.com/shanxiaow/ForecastingFirstStageBoosterLandingSuccess/blob/main/InteractiveFoliumMap/map_marker.html) | All launch sites with success (green) / failure (red) markers clustered by site |
| [map_coast.html](https://htmlpreview.github.io/?https://github.com/shanxiaow/ForecastingFirstStageBoosterLandingSuccess/blob/main/InteractiveFoliumMap/map_coast.html) | Distance from KSC LC-39A to the closest coastline (~6.41 km) |
| [map_city.html](https://htmlpreview.github.io/?https://github.com/shanxiaow/ForecastingFirstStageBoosterLandingSuccess/blob/main/InteractiveFoliumMap/map_city.html) | Distance from KSC LC-39A to the closest city (~16.31 km) |
| [map_railway.html](https://htmlpreview.github.io/?https://github.com/shanxiaow/ForecastingFirstStageBoosterLandingSuccess/blob/main/InteractiveFoliumMap/map_railway.html) | Distance from KSC LC-39A to the closest railway (~6.03 km) |

---




## Key Observations

**Launch site placement:**
- All sites are located in either Florida or southern California
- Sites are close to the coastline to minimize risk of debris landing near residential areas
- Sites are near the equator, making it easier to reach equatorial orbit
- Sites are close to railways and highways to ensure supply of resources
- Sites are far from cities to minimize danger to populated areas in case of a failed launch

**Launch success by site:**
- KSC LC-39A has the best overall performance
- The other three sites (CCAFS LC-40, CCAFS SLC-40, VAFB SLC-4E) have more failures than successes

---

## Folium Plugins Used

- `folium.plugins.MarkerCluster` — groups nearby markers when zoomed out
- `folium.plugins.MousePosition` — displays lat/long coordinates on hover
- `folium.features.DivIcon` — renders custom text labels as map markers
