import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

spacex_df = pd.read_csv("spacex_launch_dash.csv")

launch_sites = spacex_df["Launch Site"].unique().tolist()
site_options = [{"label": "All Sites", "value": "All Sites"}] + [
    {"label": site, "value": site} for site in launch_sites
]

min_payload = spacex_df["Payload Mass (kg)"].min()
max_payload = spacex_df["Payload Mass (kg)"].max()

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1(
        "SpaceX Launch Records Dashboard",
        style={"textAlign": "center", "color": "#503D36", "font-size": 40}
    ),

    html.Div([
        html.H2("Launch Site:", style={"margin-right": "2em"}),
        dcc.Dropdown(
            id="site-dropdown",
            options=site_options,
            value="All Sites",
            clearable=False,
            style={"width": "80%"}
        )
    ], style={"display": "flex"}),

    html.Br(),

    html.Div(dcc.Graph(id="success-pie-chart")),

    html.Br(),

    html.P("Payload range (Kg):"),

    dcc.RangeSlider(
        id="payload-slider",
        min=0,
        max=10000,
        step=1000,
        marks={0: "0", 2500: "2500", 5000: "5000", 7500: "7500", 10000: "10000"},
        value=[min_payload, max_payload]
    ),

    html.Div(dcc.Graph(id="success-payload-scatter-chart"))
])


@app.callback(
    Output("success-pie-chart", "figure"),
    Input("site-dropdown", "value")
)
def get_pie_chart(entered_site):
    if entered_site == "All Sites":
        fig = px.pie(
            spacex_df,
            values="class",
            names="Launch Site",
            title="Total Successful Launches by Site"
        )
    else:
        filtered_df = spacex_df[spacex_df["Launch Site"] == entered_site]
        fig = px.pie(
            filtered_df,
            names="class",
            title=f"Launch Outcomes for {entered_site}"
        )
    return fig


@app.callback(
    Output("success-payload-scatter-chart", "figure"),
    [
        Input("site-dropdown", "value"),
        Input("payload-slider", "value")
    ]
)
def get_scatter_chart(entered_site, payload_range):
    low, high = payload_range

    filtered_df = spacex_df[
        (spacex_df["Payload Mass (kg)"] >= low) &
        (spacex_df["Payload Mass (kg)"] <= high)
    ]

    if entered_site != "All Sites":
        filtered_df = filtered_df[filtered_df["Launch Site"] == entered_site]

    fig = px.scatter(
        filtered_df,
        x="Payload Mass (kg)",
        y="class",
        color="Booster Version Category",
        title="Payload Mass vs Launch Outcome"
    )
    return fig


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)