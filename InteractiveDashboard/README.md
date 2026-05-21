# SpaceX Launch Dashboard

Interactive dashboard built with Dash and Plotly for exploring SpaceX launch outcomes by launch site, payload mass, and booster category.

## Live Dashboard

https://huggingface.co/spaces/shannymonte/SpaceLaunchDashboard

## Features

- Interactive launch site filtering
- Payload mass range filtering
- Launch success visualization
- Scatterplot analysis by booster category

## Technologies Used

- Python
- Dash
- Plotly
- Pandas

## Files

- `Dashboard.ipynb` — original notebook development workflow
- `app.py` — deployable dashboard application
- `requirements.txt` — project dependencies
- `spacex_launch_dash.csv` — launch dataset

## Running Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
python app.py
```

Then open the local URL shown in the terminal.