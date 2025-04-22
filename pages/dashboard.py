import dash
import plotly.graph_objects as go
import pandas as pd
import dash_mantine_components as dmc
import plotly.express as px
from dash import html
from dash_iconify import DashIconify
from constants import PAGE_TITLE_PREFIX
from dash import Dash, dcc, html, Input, Output, dash_table, callback
from components.grid import Row,Column
from core.bd import listYear,spGetTopSellingProductsByYear

lista_year = list(listYear()["Year"])
dash.register_page(__name__,"/dashboard",title= PAGE_TITLE_PREFIX+ "Dashboard")
dmc.add_figure_templates(default="mantine_light")
layout = dmc.Container(
    fluid=True,
    #px=60,
    children=[
        dmc.Title("Dashboard", order=1, mt=0,mb=15),
        dmc.Divider(variant="solid",mb=15),
        Row([
            Column([
                dmc.Select(
                    label="Año",
                    placeholder="Seleccione Año",
                    id="year-select",
                    value=lista_year[0],
                    data=lista_year,
                    #w=200,
                    mb=10,
                ),
            ],size=6),
            Column([
                dmc.Select(
                    label="Top",
                    placeholder="Seleccione Top",
                    id="top-select",
                    value="10",
                    data=['10','15','20'],
                    #w=200,
                    mb=10,
                ),
            ],size=6)
        ]),
        dcc.Graph(id='bar-comercial')
        
    ]
)
@callback(
    Output('bar-comercial','figure'),
    Input('year-select','value'),
    Input('top-select','value'),
)
def update_graph(year,top):
    df = spGetTopSellingProductsByYear(year,top)
    df = df.groupby(["ProductName"])[["TotalSales","TotalQuantitySold"]].sum().reset_index()
    fig = px.bar(df, x='ProductName', y='TotalSales',template="mantine_light",title=f"Top {top} Productos Vendidos ({year})")
    fig.add_trace(
        go.Scatter(
            x=df["ProductName"],
            y=df["TotalQuantitySold"],
            name="Cantidad Vendida",
            mode="lines+markers",
            yaxis="y2",
            line=dict(color="crimson", width=3)
        )
    )

    # Configurar el segundo eje Y (eje derecho)
    fig.update_layout(
        yaxis2=dict(
            title="Cantidad Vendida",
            overlaying="y",
            side="right",
            showgrid=False
        ),
        yaxis=dict(title="Total Ventas"),
        legend=dict(x=0.5, y=1.1, xanchor="center", orientation="h")
    )
    return fig