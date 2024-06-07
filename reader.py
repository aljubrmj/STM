#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# sourced scripts
# import clgs as clgs
import pickle
import plotly.express as px

def initialize_data():

    fig_maps = pickle.load(open("assets/test_plot.pkl", "rb"))
    # df_maps = pickle.load(open("assets/gnn_temperature_maps_geopandas.pkl", "rb"))
        
    return fig_maps#, df_maps


# def data_dict(u_sCO2, u_H2O, c_sCO2, c_H2O):

# 	param_dict = {("utube", "sCO2", "mdot"): u_sCO2.mdot,
# 	              ("utube", "sCO2", "Horizontal Extent (m)"): u_sCO2.L2,
# 	              ("utube", "sCO2", "Vertical Extent (m)"): u_sCO2.L1,
# 	              ("utube", "sCO2", "Geothermal Gradient (K/m)"): u_sCO2.grad,
# 	              ("utube", "sCO2", "Borehole Diameter (m)"): u_sCO2.D,
# 	              ("utube", "sCO2", "Injection Temperature (˚C)"): u_sCO2.Tinj,
# 	              ("utube", "sCO2", "Rock Thermal Conductivity (W/m-K)"): u_sCO2.k,

# 	              ("utube", "H2O", "mdot"): u_H2O.mdot,
# 	              ("utube", "H2O", "Horizontal Extent (m)"): u_H2O.L2,
# 	              ("utube", "H2O", "Vertical Extent (m)"): u_H2O.L1,
# 	              ("utube", "H2O", "Geothermal Gradient (K/m)"): u_H2O.grad,
# 	              ("utube", "H2O", "Borehole Diameter (m)"): u_H2O.D,
# 	              ("utube", "H2O", "Injection Temperature (˚C)"): u_H2O.Tinj,
# 	              ("utube", "H2O", "Rock Thermal Conductivity (W/m-K)"): u_H2O.k,

# 	              ("coaxial", "sCO2", "mdot"): c_sCO2.mdot,
# 	              ("coaxial", "sCO2", "Horizontal Extent (m)"): c_sCO2.L2,
# 	              ("coaxial", "sCO2", "Vertical Extent (m)"): c_sCO2.L1,
# 	              ("coaxial", "sCO2", "Geothermal Gradient (K/m)"): c_sCO2.grad,
# 	              ("coaxial", "sCO2", "Borehole Diameter (m)"): c_sCO2.D,
# 	              ("coaxial", "sCO2", "Injection Temperature (˚C)"): c_sCO2.Tinj,
# 	              ("coaxial", "sCO2", "Rock Thermal Conductivity (W/m-K)"): c_sCO2.k,

# 	              ("coaxial", "H2O", "mdot"): c_H2O.mdot,
# 	              ("coaxial", "H2O", "Horizontal Extent (m)"): c_H2O.L2,
# 	              ("coaxial", "H2O", "Vertical Extent (m)"): c_H2O.L1,
# 	              ("coaxial", "H2O", "Geothermal Gradient (K/m)"): c_H2O.grad,
# 	              ("coaxial", "H2O", "Borehole Diameter (m)"): c_H2O.D,
# 	              ("coaxial", "H2O", "Injection Temperature (˚C)"): c_H2O.Tinj,
# 	              ("coaxial", "H2O", "Rock Thermal Conductivity (W/m-K)"): c_H2O.k,          
# 	            }
	
# 	return param_dict

def create_lcoe_plot(df_econ):
    fig = px.scatter(df_econ[::100], x='Cumulative Supply Capacity [GW]', y="LCOE [MWh]", 
                 color="T [°C]",
                 facet_col="Region",
                 color_continuous_scale='Spectral_r')

    fig.update_yaxes(range=[0, 150])
    fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1], font={"size":14}))
    fig.for_each_xaxis(lambda x: x.update({'title': '', "showgrid": True}))
    fig.for_each_yaxis(lambda y: y.update({'title': '', "showgrid": True}))
    
    fig.update_traces(
                    hovertemplate =
                        'LCOE: %{y:.0f} USD/MWh'+
                        '<br>Cum Capacity: %{x:.0f} GW<br>'
    )
    
    fig.add_annotation(
        showarrow=False,
        xanchor='center',
        xref='paper', 
        x=0.5, 
        yref='paper',
        y=-0.17,
        font=dict(
            size=14
        ),
        text='Cumulative Supply Capacity [GW]'
    )

    fig.add_annotation(
        showarrow=False,
        xanchor='center',
        xref='paper', 
        x=-0.06, 
        yanchor='middle',
        yref='paper',
        y=0.5,
        textangle=270,
        font=dict(
            size=14
        ),
        text='LCOE [USD/MWh]'
    )

    fig.update_layout(template="simple_white",
                    #    margin=dict(b=0, t=0, l=0, r=0), 
                       width=1500, height=500,
                       )

    return fig


