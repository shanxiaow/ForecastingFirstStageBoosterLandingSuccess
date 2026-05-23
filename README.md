# Forecasting First Stage Booster Landing Success
 

---

## Project Overview

SpaceX has transformed commercial spaceflight by making rockets partially reusable. The defining innovation of these rockets is that the first-stage booster can return and land vertically after launch, allowing it to be reused instead of discarded. The successful reusability dramatically lowers launch costs and enables an unprecedented launch frequency. Predicting first‑stage landing outcomes is essential for mission planning, cost modeling, and understanding the operational reliability of reusable rockets.

This project builds a full end-to-end data science project to predict whether the first stage will land successfully. The project covers the complete pipeline from raw data collection through to machine learning model deployment.



This project walks through:
- Collecting and enriching launch data from the SpaceX API and web scraping
- Data wrangling; SQL-based exploration
- Exploratory data analysis; data visualization
- An interactive dashboard for exploring launch outcomes
- Geospatial analysis of launch site locations (Folium maps)
- Training and comparing multiple classification models

---

## Project Structure

```
├── DataCollection/
│   ├── DataCollection_API.ipynb
│   └── WebScraping.ipynb
├── EDA&DataWrangling/
│   ├── DataWrangling.ipynb
│   ├── EDAwithSQL.ipynb
│   └── Visualization.ipynb
├── InteractiveDashboard/
│   ├── Dashboard.ipynb
│   ├── app.py
│   ├── requirements.txt
│   └── spacex_launch_dash.csv
├── InteractiveFoliumMap/
│   └── Folium.ipynb
└── ML Prediction/
    └── Prediction.ipynb
```

---

## Pipeline

### 1. Data Collection
Launch data is gathered from two sources:

- **SpaceX REST API** — queries `api.spacexdata.com/v4/launches/past` and enriches ID fields (rocket, launchpad) by querying additional endpoints. Filters to Falcon 9 only and handles missing payload mass values.
- **Web Scraping** — uses BeautifulSoup to scrape supplemental Falcon 9 launch records from public HTML tables.

### 2. EDA and Data Wrangling
- Initial inspection, cleaning, and standardization of the dataset
- Creation of the binary classification target variable (landing success/failure)
- SQL-based exploration to validate assumptions and uncover patterns
- Visual analysis to identify potential predictors and inform feature engineering


### 3. Interactive Dashboard
A Dash + Plotly dashboard for exploring launch outcomes by site, payload mass, and booster category.


  <a href="https://huggingface.co/spaces/shannymonte/SpaceLaunchDashboard" target="_blank" style="font-size: 17px; font-weight: bold; color: orange; margin-bottom: 7px;">
  View Live Dashboard
  </a>


To run locally:
```bash
pip install -r requirements.txt
python app.py
```




### 4. Geospatial Analysis
Interactive map analysis using Folium to explore how launch site location relates to outcomes. Measures distances from KSC LC-39A to surrounding infrastructure:

| Map | Description |
|-----|-------------|
| [map_marker.html](https://shanxiaow.github.io/forecasting-first-stage-booster-landing-success/InteractiveFoliumMap/map_marker.html) | All launch sites with success (green) / failure (red) markers |
| [map_coast.html](https://shanxiaow.github.io/forecasting-first-stage-booster-landing-success/InteractiveFoliumMap/map_coast.html) | Distance to closest coastline (~6.41 km) |
| [map_city.html](https://shanxiaow.github.io/forecasting-first-stage-booster-landing-success/InteractiveFoliumMap/map_city.html) | Distance to closest city (~16.31 km) |
| [map_railway.html](https://shanxiaow.github.io/forecasting-first-stage-booster-landing-success/InteractiveFoliumMap/map_railway.html) | Distance to closest railway (~6.03 km) |


### 5. Machine Learning
Four classification models trained and evaluated using GridSearchCV with 10-fold cross-validation:

- Logistic Regression
- Support Vector Machine (SVM)
- Decision Tree
- K-Nearest Neighbors (KNN)

Models evaluated on accuracy score, confusion matrices, and comparative performance visualization.

---

## Technologies Used

- **Data:** Python, Pandas, NumPy, BeautifulSoup, Requests
- **EDA:** SQL, Matplotlib, Seaborn
- **Geospatial:** Folium
- **Dashboard:** Dash, Plotly
- **ML:** scikit-learn (StandardScaler, GridSearchCV, LogisticRegression, SVC, DecisionTreeClassifier, KNeighborsClassifier)

---

<br><br>
[View the full code on GitHub →](https://github.com/shanxiaow/SpaceX-Rocket-Launch)


<br><br>
A successful land launch:

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/lab_v2/images/landing_1.gif)


