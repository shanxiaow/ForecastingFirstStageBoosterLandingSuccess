
## Data Collection

This folder contains the notebooks used to gather raw launch data for the first‑stage landing prediction project. Data is collected from two sources: the SpaceX REST API and web‑scraped HTML tables.


<br>

## 1. Collecting Launch Data from the SpaceX REST API

- Send GET requests to the SpaceX API endpoint:  
  `https://api.spacexdata.com/v4/launches/past`
- The response is a JSON list where each element represents a launch.
- Convert the JSON response into a Pandas DataFrame.
- Perform initial cleaning and type normalization.

### Additional API Queries
Some fields (e.g., `rocket`, `launchpad`) contain ID references rather than descriptive data.

To enrich the dataset:
- Query additional API endpoints (e.g., `/rockets`, `/launchpads`) using the IDs.
- Merge the returned metadata into the main launch DataFrame by ID number.

### Additional Data Cleaning
- Remove duplicate records.
- Filter out Falcon 1 launches and keep only Falcon 9 missions.
- Handle missing values: Replace null values in `PayloadMass` with the mean payload mass.



<br>

## 2. Collecting Launch Data via Web Scraping

- Use `BeautifulSoup` to scrape HTML tables containing Falcon 9 launch records.
- Parse and clean the raw HTML table data.
- Convert the cleaned table into a Pandas DataFrame.
- Align scraped fields with API‑collected fields for later merging.



<br><br><br>



## Notebooks in This Folder

- **DataCollection_API.ipynb** — Queries the SpaceX REST API and constructs the primary dataset.
- **WebScraping.ipynb** — Scrapes supplemental launch data from public HTML tables.



