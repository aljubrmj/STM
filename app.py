#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------------
# GeoCLUSTER, data tool and app that runs visuals on Closed-Loop Geothermal Data
# -------------------------------------------------------------------------------------

# --------------------
# Libraries.
# --------------------

# web app and interactive graphics libraries 
import dash
from dash.dependencies import Input, Output, State
from dash import Dash, dcc, html, ctx
# import dash_daq as daq                  # Adds more data acquisition (DAQ) and controls to dash callbacks 
import dash_bootstrap_components as dbc # Adds bootstrap components for more web themes and templates
from dash.exceptions import PreventUpdate
import dash_leaflet as dl
import dash_leaflet.express as dlx
from dash_extensions.javascript import assign, arrow_function

# sourced scripts
# from write2excel import write_excelsheet
# from sliders import *
from dropdowns import *
from text import *
# from tables import generate_summary_table
# from plots import * # u_sCO2, u_H2O, c_sCO2, c_H2O

import pickle
import os
from reader import initialize_data
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
import numpy as np
from shapely.geometry import Point
import plotly.graph_objs as go

# fig_maps, df_maps = initialize_data()
# fig_maps = initialize_data()
# -----------------------------------------------------------------------------
# Create dash app with CSS styles and HTML components.
#
#   layout:      Describes the HTML layout of the app.
#   callbacks:   Interactivity of the app.
#
# -----------------------------------------------------------------------------
# assets_path = os.getcwd() +'/src/new_assets'
# url_base_pathname = "/".join(os.getcwd().split("/")[:-1]) + "/"

chroma = "https://cdnjs.cloudflare.com/ajax/libs/chroma-js/2.1.0/chroma.min.js"  # js lib used for colors
#source: https://github.com/gka/chroma.js/blob/main/src/colors/colorbrewer.js
Spectral = ['#9e0142', '#d53e4f', '#f46d43', '#fdae61', '#fee08b', '#ffffbf', '#e6f598', '#abdda4', '#66c2a5', '#3288bd', '#5e4fa2']
colorscale = Spectral[::-1]
geojson_style = dict(weight=2, opacity=0.5, dashArray='3', fillOpacity=0.5)
geojson_style_handle = assign("""function(feature, context){
    const {min, max, colorscale, style, colorProp} = context.hideout;  // get props from hideout
    const csc = chroma.scale(colorscale).domain([min, max]);  // chroma lib to construct colorscale
    const mycolor = csc(feature.properties[colorProp]) ;
    style.fillColor = mycolor ;  // set color based on color prop
    style.color = mycolor ;  // set color based on color prop
    style.weight = 0.9 ;  // set color based on color prop
    return style;
}""")
    
app = dash.Dash(__name__, 
                external_stylesheets=[dbc.themes.BOOTSTRAP], 
                external_scripts=[chroma],
                # url_base_pathname=url_base_pathname
                # url_base_pathname="/GeoCLUSTER/"
                )

##########
# app.css.config.serve_locally = True
# app.scripts.config.serve_locally = True
##########

# -----------------------------------------------
# Globl styles, configurations, and colors.
# -----------------------------------------------

tabs = ["energy-tab"]#"energy-time-tab", "energy-tab"]#, "econ-time-tab", "summary-tab"]


plotly_config = {'displaylogo': False,
                'modeBarButtonsToRemove': ['autoScale', 'resetScale'], # High-level: zoom, pan, select, zoomIn, zoomOut, autoScale, resetScale
                'toImageButtonOptions': {
                    'format': 'png', # one of png, svg, jpeg, webp
                    'filename': 'custom_image',
                    'height': None,
                    'width': None,
                    'scale': 6 # Multiply title/legend/axis/canvas sizes by this factor
                        }
                  }


darkergrey = "#383838"
lightbrown = '#ede6dd'
dropdown_guidance_style = {'position': 'relative',
                            # 'marginTop': '28px',
                            # 'marginTop': '-18px',
                            # 'marginLeft': '20px',
                            'height': '25px',
                            'width': '100%',
                            # "paddingBottom": "7px",
                            "paddingLeft": "20px",
                            "paddingRight": "20px",
                            'border':'1.5px white solid',
                            'backgroundColor': lightbrown,
                            "color": darkergrey,
                            "fontWeight": "bold",
                            "fontSize": "11px",
                            }
carousel_image_style = {
                        # 'height': '10%',
                        # 'width': '100%',
                        'objectFit': 'contain',
                        }

white = '#ffffff'
bluewhite = "#8C1515"
solidblue = "#8C1515"

tab_selected_style = {'background': solidblue, 
                        'width': '50%',
                         'fontSize': '14px',
                         'color': white,
                         'fontWeight': 'bold',
                         'alignItems': 'center',
                         'justifyContent': 'center',
                         'padding':'7px',
                         'borderTop': '2px solid #8C1515',
                         'borderLeft': '1px solid #8C1515',
                         'borderBottom': '5px solid #f2810a'} # #d6d6d6


# -----------------------------------------------
# HTML components.
# -----------------------------------------------
    
def logo_card():
    return  html.Div(id="logo-card",
                     children=[
                                # html.Hr(id="hr-break1"),
                               html.Img(id="logo", src=app.get_asset_url('stm_logo.png')),
                               html.Hr(id="hr-break2")
                                ]
                    )

def description_card():

    # -----------------------------------------------------------------------
    # A Div containing dashboard title & descriptions.
    # -----------------------------------------------------------------------
                    
    return html.Div(
        id="description-card2",
        children=[
            logo_card(),        
            html.P("Model Description", id='ab-title1'),
            html.Label([
                # html.P(note, 'note'),
                note,
                html.A("ArcGIS", 
                href='https://arcg.is/nLzzT0',
                id='arcgis-link1',
                target="_blank"),
                " and ",
                html.A("GDR", 
                href='https://gdr.openei.org/submissions/1592',
                id='arcgis-link2',
                target="_blank"),
                "."
            ]),
            html.P("User Input", id='ab-title2'),
            # html.Div(id="profile-div",
            # children=[
                dbc.Col([
                    # dbc.Row([
                    #         dbc.Row(html.P("You may click on the map directly to specify \
                    #             your location or input latitude and longitude directly here.", id='collapse2')),
                    #         ], id="latlon-inputs0"),
                    dbc.Row([
                            dbc.Col(
                                dbc.Card(
                                children=[
                                    dbc.CardBody(
                                        children=[
                                            html.B("Instructions: "),
                                            user_instructions
                            ]
                        )]
                    )
                                ),
                            ], id="latlon-inputs0"),
                    dbc.Row([
                            dbc.Col(html.B("Longitude [deg]"), width=4),  
                            dbc.Col(dcc.Input(id='lon-input', value=-101.317918, 
                                    type='number', min=-124.736342, max=-66.945392, 
                                    debounce=False, style = {"width": "100%", "height": "90%"}), width=4)
                            ], justify="center", style={"padding-top": "2%", "padding-bottom": "2%"}),
                    dbc.Row([
                            dbc.Col(html.B("Latitude [deg]"), width=4),  
                            dbc.Col(dcc.Input(id='lat-input', value=40.330871,
                                    type='number', min=24.521208, max=49.382808, 
                                    debounce=False, style = {"width": "100%", "height": "90%"}), width=4)
                            ], justify="center", style={"padding-top": "2%", "padding-bottom": "2%"}),
                    dbc.Row([
                            dbc.Col(html.B("Depth [meters]"), width=4),  
                            dbc.Col(dcc.Input(id='depth-input', value=3000,
                                    type='number', min=0, max=7000,
                                    debounce=True, style = {"width": "100%", "height": "90%"}), width=4)
                            ], justify="center", style={"padding-top": "2%", "padding-bottom": "2%"})
                        # ], id="profile-div"),
                ]
                    ),
            html.P("Contact Info", id="contact-us1"),
            html.Label([
            team_info2,
            html.A("Mohammad Aljubran", 
            href='https://www.linkedin.com/in/mohammad-aljubran/',
            id='developer-name1',
            target="_blank"
                ),
            team_info3,     
            html.A("aljubrmj@stanford.edu", 
                href='mailto: aljubrmj@stanford.edu',
                id='team-info2',
                target="_blank"
                    ),
            team_info4,
            html.A("Professor Roland Horne", 
                href='https://www.linkedin.com/in/roland-horne-7906b956/',
                id='developer-name2',
                target="_blank"
                    ),
            team_info3,
            html.A("horne@stanford.edu", 
                href='mailto: horne@stanford.edu',
                id='team-info3',
                target="_blank"
                    ),
            "."
                    ]),
                                            
            ],
    )

# @app.callback(
#     Output("arcgis_src", "src"),
#     Input("lon-input", "value"),
#     Input("lat-input", "value")
# )
# def arcgis_map_card(lon, lat):
#     lon = -101.317918 if lon is None else lon
#     lat = 40.330871 if lat is None else lat
    
#     return f"//stanford.maps.arcgis.com/apps/Embed/index.html?webmap=bf4d25d2a4164d0a94a32bb4cb877c01&home=true&zoom=true&level=7&legend=false&scale=false&disable_scroll=false&theme=light&legend=true&legendlayers=true&show_panel=true&popup_sidepanel=false&zoom_position=bottom-left&marker={lon};{lat}"

def carousel_card():
    return html.Div(id='left-column-div',
            children=[
                    html.Iframe(id='arcgis_src',
                                style={"position": "relative", "width": "100%"})
                    ]
            )
    
def graph_guidance_card(btnID, cardID, dropdown_children):

    # -----------------------------------------------------------------------
    # A Div containing graph guidance dropdowns for extra user context.
    # -----------------------------------------------------------------------

    return html.Div(
        [
            dbc.Button(
                "ⓘ Map Guidance",
                id=btnID,
                color="primary",
                n_clicks=0,
                style=dropdown_guidance_style
            ),
            dbc.Collapse(
                dbc.Card(
                    children=[
                        dbc.CardBody(
                            children=[
                                dropdown_children
                            ]
                        )]
                    ),
                id=cardID,
                is_open=False,
            ),
        ], id="button-div"
    )


# @app.callback(
#     Output(component_id="collapse2", component_property="is_open"),
#     [Input(component_id="collapse-button2", component_property="n_clicks")],
#     [State(component_id="collapse2", component_property="is_open")],
# )
# def toggle_collapse(n, is_open):

#     # ----------------------------------------------
#     # Subsurface results graph guidance.
#     # ----------------------------------------------

#     if n:
#         return not is_open
#     return is_open

def contact_us_card():

    # -----------------------------------------------------------------------
    # A Div containing graph guidance dropdowns for extra user context.
    # -----------------------------------------------------------------------

    return html.Div(
        [
            html.P(
                "Contact Info",
                id="contact-us1",
            ),
            html.Label([
            team_info2,
            html.A("Mohammad Aljubran", 
            href='https://www.linkedin.com/in/mohammad-aljubran/',
            id='developer-name1',
            target="_blank"
                ),
            team_info3,     
            html.A("aljubrmj@stanford.edu", 
                href='mailto: aljubrmj@stanford.edu',
                id='team-info2',
                target="_blank"
                    ),
            team_info4,
            html.A("Professor Roland Horne", 
                href='https://www.linkedin.com/in/roland-horne-7906b956/',
                id='developer-name2',
                target="_blank"
                    ),
            team_info3,
            html.A("horne@stanford.edu", 
                href='mailto: horne@stanford.edu',
                id='team-info3',
                target="_blank"
                    ),
            ]),
        ],
        id="contact-us2",
    )
    
# info = html.Div(children=get_info(), id="info", className="info",
#                 style={"position": "absolute", "top": "10px", "right": "10px", "zIndex": "1000"})

def generate_analysis():
    return html.Div(children=[
                    # dbc.Row([graph_guidance_card(btnID="collapse-button2", cardID="collapse2", 
                    # dropdown_children=html.P(dropdown_text1))], id="profile-row0"),
                    dbc.Row([create_map()], id="profile-row2"),   
                    dbc.Row([
                        dbc.Col([
                                dcc.Graph(id="tempprofile-out", responsive=True),
                                ], width=4),
                        dbc.Col([
                            dcc.Graph(id="ggprofile-out", responsive=True)
                                ], width=4),
                        dbc.Col([
                                dcc.Graph(id="condprofile-out", responsive=True),
                                ], width=4),
                            ], id="profile-row1", justify="evenly")
                ])
    
def create_map():
    geojson = html.Div(children=get_geojson_filename(), id="geojson-div")
    # Create info control.
    info = html.Div(children=get_info(), id="info", className="info",
                    style={"position": "absolute", "top": "10px", "right": "10px", "zIndex": "1000"})
    
    colorbar = dl.Colorbar(colorscale=colorscale, width=30, height=150, 
                           min=25, max=250, unit='° C', tooltip=True,
                           style={"fontSize": "small"}, position="bottomleft")

    # dropdown_depths = dcc.Dropdown(id="dd", value=3000, label="Depth",
    #                                options=np.linspace(0, 7000, 8), 
    #                                clearable=False, multi=False)
    
    # dropdown_depths = dbc.DropdownMenu(
    #                     label="Depth",
    #                     menu_variant="dark",
    #                     children=[
    #                         dbc.DropdownMenuItem("Item 1"),
    #                         dbc.DropdownMenuItem("Item 2"),
    #                         dbc.DropdownMenuItem("Item 3"),
    #                     ],
    #                 )
    
    eventHandlers = dict(
    click=assign("function(e, ctx){ctx.setProps({latlng_data: e.latlng})}"))
    
    return html.Div([
                    # dropdown_depths,
                    dl.Map(id='map', center=[39, -98], zoom=4, eventHandlers=eventHandlers,
                   children=[
                        dl.TileLayer(),
                        geojson,
                        colorbar,
                        info,
                            ], 
                   style={'height': '40vh'},
                   ),
        ])

# @app.callback(Output("depth-input", "value"), Input("dd", "value"))
# def update_filter(value):
#     return value

@app.callback(Output("geojson-div", "children"),
              Input("depth-input", "value"))

def get_geojson_filename(depth=None):
    # import pdb
    # pdb.set_trace()
    # print(depth)
    if not depth:
        depth = 3000
    return [dl.GeoJSON(id='geojson',
                        # url=app.get_asset_url("stm_map_6km.json"),
                        url=app.get_asset_url(f"stm_map_{depth/1000:.0f}km.json"),
                        # url = app.get_asset_url("geojson-src"),
                        zoomToBounds=True,
                        # zoomToBoundsOnClick=True,
                        options={"style": geojson_style_handle},
                        hoverStyle=arrow_function(dict(weight=5, color='#666', dashArray='')),
                        hideout=dict(colorProp="T", colorscale=colorscale, 
                                        style=geojson_style, min=25, max=350)
                            )]
    

def get_info(feature=None, lat=40.330871, lon=-101.317918, depth=None):
    
    if (not feature):
        return [html.H4("Action"), html.P("Click on a Location")]
    
    header = [html.H4("Summary")]
    header += [html.P(html.B(f'Lon: {lon:0.6f}°'))]
    header += [html.P(html.B(f'Lat: {lat:0.6f}°'))]
    if depth:
        header += [html.P(html.B(f'Depth: {round(depth, -3):.0f} meters'))]
    
    return header + [html.P(html.B(f'Temperature: {feature["properties"]["T"]:.1f}° C'))]

@app.callback(Output("info", "children"),
              Output("lat-input", "value"),
              Output("lon-input", "value"),
              Input("geojson", "clickData"),
              Input("map", "latlng_data"),
              Input("depth-input", "value"))

def info_hover(feature=None, click_lat_lng=None, depth=None):
    if click_lat_lng:
        lat = click_lat_lng["lat"]
        lon = click_lat_lng["lng"]
    else:
        lat = 40.330871
        lon = -101.317918
    
    return get_info(feature, lat, lon, depth), lat, lon

def generate_tabs():

    about_tab = dcc.Tab(label='Geothermal Economics',
                        id="about-tab",
                         value='about-tab',
                         selected_style=tab_selected_style,
                         children=[
                                html.Div([
                                html.P("COMING SOON: This work will be based on the Flexible Geothermal Economics Model (FGEM)", style={"color": "red"}),
                                "References: ",
                                html.A("Journal Article",
                                href='https://www.sciencedirect.com/science/article/pii/S0306261923014897?via%3Dihub',
                                id='comingsoon-label1',
                                target="_blank"
                                     ),
                                "     ",
                                html.A("GitHub Repo",
                                href='https://github.com/aljubrmj/FGEM/tree/main',
                                id='comingsoon-label2',
                                target="_blank")
                                ], id="coming-soon")
                                    ]
                                            )

    energy_tab = dcc.Tab(label='Temperature Profile',
                         id="contour-tab",
                         value='energy-tab',
                         selected_style=tab_selected_style,
                         children=[
                                    html.Div(id="dropdown-card5",
                                             children=[
                                                        generate_analysis(),
                                                    ]
                                            )
                                    ] 
                        )

    tabs = dcc.Tabs(id="tabs", 
                    value='energy-tab', 
                    children=[
                        energy_tab,
                        about_tab,
                            #   energy_time_tab,
                            #   economics_time_tab,
                            #   summary_tab,
                              ])

    return tabs

# -----------------------------------------------------------------------------
# Define dash app layout here.
# -----------------------------------------------------------------------------

app.layout = html.Div(
    id="app-container",
    children=[
        # dcc.Store(id='econ-memory'),
        # dcc.Store(id='econ-results'),
        # dcc.Store(id='econ-errors'),
        # dcc.Store(id='thermal-memory'),
        dcc.Store(id='thermal-results-mass'),
        dcc.Store(id='thermal-results-time'),
        dcc.Store(id='thermal-results-errors'),
        dcc.Store(id='thermal-contours-errors'),
        # dcc.Store(id='depth-input'),

        # banner_card(),
        
        # Left column
        html.Div(
            id="left-column",
            className="columns",
            children=[
                      description_card(), 
                    #   carousel_card()
                      ]
        ),
        # Right column
        html.Div(
            id="right-column",
            className="columns",
            children=[
                    # logo_card(),
                    # generate_analysis(),
                    generate_tabs()
            ],
        ),
    ],
)

@app.callback(
    Output("tempprofile-out", "figure"),
    Output("ggprofile-out", "figure"),
    Output("condprofile-out", "figure"),
    Input("lon-input", "value"),
    Input("lat-input", "value"),
    Input("depth-input", "value"),
)

def number_render(lon=None, lat=None, depth=None):

    lon = -101.317918 if lon is None else lon
    lat = 40.330871 if lat is None else lat
    depth = 3000 if depth is None else depth
        
    northing_easting = gpd.GeoDataFrame(geometry=[Point(lon, lat)], crs="EPSG:4326").to_crs("EPSG:3857").loc[0, "geometry"]
    easting, northing = northing_easting.xy[0][0], northing_easting.xy[1][0]
    location = Point(easting, northing)
    target_depths = np.array([0, 1000, 2000, 3000, 4000, 5000, 6000, 7000])
    Ts, T_stds, Ks, K_stds = [], [], [], []
    df_maps =  pickle.load(open("assets/gnn_temperature_maps_geopandas.pkl", "rb"))
    for d in target_depths:
        df = df_maps[d]
        idx = (np.abs(df["Easting"] - location.coords.xy[0][0]) + \
            np.abs(df["Northing"] - location.coords.xy[1][0])).argmin()
        Ts.append(df.iloc[idx]["T"])
        T_stds.append(df.iloc[idx]["T_std"])
        Ks.append(df.iloc[idx]["K"])
        K_stds.append(df.iloc[idx]["K_std"])
        # idx = (np.abs(df_maps[d]["Easting"] - location.coords.xy[0][0]) + \
        #     np.abs(df_maps[d]["Northing"] - location.coords.xy[1][0])).argmin()
        # Ts.append(df_maps[d].iloc[idx]["T"])
        # T_stds.append(df_maps[d].iloc[idx]["T_std"])
    Ts = np.array(Ts)
    T_stds = np.array(T_stds)
    T = np.interp(depth, target_depths, Ts)
    Ks = np.array(Ks)
    K_stds = np.array(K_stds)
    K = np.interp(depth, target_depths, Ks)
    
    temp_fig = create_temp_plot(target_depths, Ts, T_stds, T, depth, lat, lon)
    gg_fig = create_gg_plot(target_depths, Ts, T_stds, T, depth, lat, lon)
    k_fig = create_K_plot(target_depths, Ks, K_stds, K, depth, lat, lon)
    
    return temp_fig, gg_fig, k_fig

def create_K_plot(target_depths, Ks, K_stds, K, depth, lat, lon):
    fig = go.Figure([
    go.Scatter(
        x=Ks+K_stds,
        y=target_depths,
        mode='lines',
        marker=dict(color="#8C1515"),
        line=dict(width=0),
        showlegend=False,
        name="",
        hoverinfo='skip'
    ),
    go.Scatter(
        x=Ks-K_stds,
        y=target_depths,
        marker=dict(color="#8C1515"),
        line=dict(width=0, color="#8C1515"),
        mode='lines',
        fillcolor='#F3E9E9',
        fill='tonexty',
        showlegend=False,
        name="",
        hoverinfo='skip'
    ),
    go.Scatter(
        x=Ks,
        y=target_depths,
        mode='lines',
        line=dict(color='#8C1515'),
        showlegend=False,
        name="",
        hovertemplate =
        'Depth: %{y:.0f} meters'+
        '<br>Thermal Conductivity: %{x} W/(C-m)<br>',
        
    ),
    go.Scatter(
    x=[K],
    y=[depth],
    mode='markers',
    marker=dict(color="#016895", symbol="star", size=20),#, opacity=[0]),
    showlegend=False,
    hovertemplate =
        'Depth: %{y:.0f} meters'+
        '<br>Thermal Conductivity: %{x} W/(C-m)<br>',
    hoverlabel = dict(font=dict(color='white'), bordercolor='white'),
    name="",
    )
    ])

    fig.update_yaxes(autorange="reversed")

    fig.update_layout(template="simple_white", 
                      margin=dict(b=0, t=0, l=0, r=0), width=350, height=200,
                    xaxis_title="Thermal Conductivity [W/(C-m)]",
                    yaxis_title="Depth [meters]",
                    xaxis=dict(showgrid=True), 
                    yaxis=dict(showgrid=True),
                    font=dict(size=11)
                    )
    return fig

def create_temp_plot(target_depths, Ts, T_stds, T, depth, lat, lon):
    fig = go.Figure([
    go.Scatter(
        x=Ts+T_stds,
        y=target_depths,
        mode='lines',
        marker=dict(color="#8C1515"),
        line=dict(width=0),
        showlegend=False,
        name="",
        hoverinfo='skip'
    ),
    go.Scatter(
        x=Ts-T_stds,
        y=target_depths,
        marker=dict(color="#8C1515"),
        line=dict(width=0, color="#8C1515"),
        mode='lines',
        fillcolor='#F3E9E9',
        fill='tonexty',
        showlegend=False,
        name="",
        hoverinfo='skip'
    ),
    go.Scatter(
        x=Ts,
        y=target_depths,
        mode='lines',
        line=dict(color='#8C1515'),
        showlegend=False,
        name="",
        hovertemplate =
        'Depth: %{y:.0f} meters'+
        '<br>Temperature: %{x}° C<br>',
        
    ),
    go.Scatter(
    x=[T],
    y=[depth],
    mode='markers',
    marker=dict(color="#016895", symbol="star", size=20),#, opacity=[0]),
    showlegend=False,
    hovertemplate =
        'Depth: %{y:.0f} meters'+
        '<br>Temperature: %{x}° C<br>',
    hoverlabel = dict(font=dict(color='white'), bordercolor='white'),
    name="",
    )
    ])

    fig.update_yaxes(autorange="reversed")

    fig.update_layout(template="simple_white", 
                      margin=dict(b=0, t=0, l=0, r=0), width=500, height=200,
                    xaxis_title="Temperature [° C]",
                    yaxis_title="Depth [meters]",
                    xaxis=dict(showgrid=True), 
                    yaxis=dict(showgrid=True),
                    font=dict(size=11)
                    # xaxis_range=[0, 500]
                    )

    # fig.add_annotation(
    #     x=max(Ts + T_stds)*0.8, y=200,
    #     xref="x", yref="y",  # Reference system for text's x and y coordinates
    #     text=f"Longitude = {lon:.3f}° <br>Latitude = {lat:.3f}° <br>Depth = {depth:.0f} meters<br>Temperature = {T:.0f}° C",
    #     showarrow=False,
    #     bordercolor="black",
    #     borderwidth=1,
    #     font=dict(
    #     size=12,
    #     color="black"
    #     ),
    #     bgcolor="white"
    # )
    return fig

def create_gg_plot(target_depths, Ts, T_stds, T, depth, lat, lon):
    # gg_avg = (Ts[-1] - Ts[0])/(target_depths[-1] - target_depths[0])*1000
    ggs = np.diff(Ts)/np.diff(target_depths)*1000
    ggs = np.hstack((np.array(ggs[0]), ggs))
    gg_stds = (T_stds[1:]-T_stds[0]) / target_depths[1:] * 1000
    gg_stds = np.hstack((np.array(gg_stds[0]), gg_stds))
    gg = np.interp(depth, target_depths, ggs)

    fig = go.Figure([
    go.Scatter(
        x=ggs+gg_stds,
        y=target_depths,
        mode='lines',
        marker=dict(color="#8C1515"),
        line=dict(width=0),
        showlegend=False,
        name="",
        hoverinfo='skip'
    ),
    go.Scatter(
        x=ggs-gg_stds,
        y=target_depths,
        marker=dict(color="#8C1515"),
        line=dict(width=0, color="#8C1515"),
        mode='lines',
        fillcolor='#F3E9E9',
        fill='tonexty',
        showlegend=False,
        name="",
        hoverinfo='skip'
    ),
    go.Scatter(
        x=ggs,
        y=target_depths,
        mode='lines',
        line=dict(color='#8C1515'),
        showlegend=False,
        name="",
        hovertemplate =
        'Depth: %{y:.0f} meters'+
        '<br>Gradiant: %{x} C/km<br>',
        
    ),
    go.Scatter(
    x=[gg],
    y=[depth],
    mode='markers',
    marker=dict(color="#016895", symbol="star", size=20),#, opacity=[0]),
    showlegend=False,
    hovertemplate =
        'Depth: %{y:.0f} meters'+
        '<br>Gradiant: %{x} C/km<br>',
    hoverlabel = dict(font=dict(color='white'), bordercolor='white'),
    name="",
    )
    ])

    fig.update_yaxes(autorange="reversed")

    fig.update_layout(template="simple_white", 
                      margin=dict(b=0, t=0, l=0, r=0), width=500, height=200,
                    xaxis_title="Geothermal Gradient [C/km]",
                    yaxis_title="Depth [meters]",
                    xaxis=dict(showgrid=True), 
                    yaxis=dict(showgrid=True),
                    font=dict(size=11)
                    # xaxis_range=[0, 500]
                    )

    # fig.add_annotation(
    #     x=max(ggs + gg_stds)*0.95, y=200,
    #     xref="x", yref="y",  # Reference system for text's x and y coordinates
    #     text=f"Longitude = {lon:.3f}° <br>Latitude = {lat:.3f}° <br>Depth = {depth:.0f} meters<br>Gradient = {gg:.0f} C/km",
    #     showarrow=False,
    #     bordercolor="black",
    #     borderwidth=1,
    #     font=dict(
    #     size=12,
    #     color="black"
    #     ),
    #     bgcolor="white"
    # )
    return fig

# -----------------------------------------------------------------------------
# App run here. Define configurations, proxies, etc.
# -----------------------------------------------------------------------------

server = app.server 
# from app import server as application # in the wsgi.py file -- this targets the Flask server of Dash app

if __name__ == '__main__':
    # app.run_server(debug=True)
    app.run_server(port=8060, debug=True) 
    # app.run(debug=True)
    # EXAMPLE: *************
    # app.run_server(port=8050, proxy="http://127.0.0.1:8059::https://<site>/<page_name>")




