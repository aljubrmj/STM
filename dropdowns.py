#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# web app and interactive graphics libraries 
from dash import dcc, html

# ---------------------------
# Define dropdown options.
# ---------------------------

interp_list = ["True", "False"]
case_list = ["utube", "coaxial"]
fluid_list = ["All", "H2O", "sCO2"]
end_use_list = ["All", "Heating", "Electricity"] 

param_list = ["Horizontal Extent (m)", "Vertical Extent (m)", "Geothermal Gradient (K/m)", "Borehole Diameter (m)", 
                "Injection Temperature (˚C)", "Rock Thermal Conductivity (W/m-K)"]

dropdown_list = ["Run Interpolation", "Heat-Exchanger", "Working Fluid", "End-Use"]

def dropdown_card():

    # -----------------------------------------------------------------------
    # A Div containing controls for graphs. Controls include the following:
    #
    #   Dropdowns for categories:
    #           interpolation, case, fluid
    #
    # -----------------------------------------------------------------------

    return html.Div(id="dropdown-container",
                    children=[
                        html.Div(id="dropdown-card1",
                            style={'display': 'none'},
                            children=[
                                html.P("Run Interpolation"),
                                dcc.Dropdown(
                                    id="interpolation-select",
                                    options=[{"label": i, "value": i} for i in interp_list],
                                    value=interp_list[0],
                                    clearable=False,
                                    searchable=False
                                ),
                            ]
                        ),
                        
                        html.Div(id="dropdown-card2",
                            children=[
                                html.P("Heat-Exchanger"),
                                dcc.Dropdown(
                                        id="case-select",
                                        options=[{"label": i, "value": i} for i in case_list],
                                        value=case_list[0],
                                        clearable=False,
                                        searchable=False
                                    ),
                                ]
                            ),
                        html.Div(id="dropdown-card3",
                            children=[
                                html.P("Working Fluid"),
                                dcc.Dropdown(
                                    id="fluid-select",
                                    options=[{"label": i, "value": i} for i in fluid_list],
                                    value=fluid_list[0],
                                    clearable=False,
                                    searchable=False
                                    )
                                ]
                            ),
                        html.Div(id="dropdown-card4",
                            children=[
                                html.P("End-Use"),
                                dcc.Dropdown(
                                    id="end-use-select",
                                    options=[{"label": i, "value": i} for i in end_use_list],
                                    value=end_use_list[0],
                                    clearable=False,
                                    searchable=False
                                ),
                            ]
                        ),
                ]
            )


