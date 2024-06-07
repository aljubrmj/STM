#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------
# Contains text content for dash app.
# -----------------------------------------------------------------------------


# Left Panel Text
scenario1_text = "Evaluates thermal and economic performance of a commercial-scale operation, \
                                which is representative of hot-dry-rock (HDR) geothermal reservoirs within the continental United States."

scenario2_text = "Calculates HDR results for operations that optimize power output."

scenario3_text = "Calculates near-minima levelized-cost-of-heat (LCOH) and levelized-cost-of-electricity (LCOE) results."

disclaimer_text = "The information on this website is for general informational purposes only. \
                    Your use of the site is solely at your own risk."


# Graph Guidance Text

# dropdown_text1_old = "Graphs show CLGS HDR results over time as well as average power output and thermal output by mass flow rate."

dropdown_text1 = "Click on the map to get temperature predictions at your location. You can also view predictions \
                for a specific depth using the Input Target Location column on the left."

dropdown_text2 = "This tool provides the predicted temperature profile based on coordinates (latitude, longitude) and depth you specify."
# dropdown_text2_old = "Contours show CLGS HDR results show where parameters maximize or minimize. \
#             			Maximation occurs in areas with lighter colors and minimization in areas with darker colors."

# dropdown_econ_old_text = "Graphs show heat and electricity forecasts, which can be altered by selecting thermal performance values. \
# 		                    Levelized Cost of Heating (LCOH) and Levelized Cost of Energy (LCOE) measures are also computed and displayed by \
# 		                    altering both thermal performance and economic forecast values. \
# 		                    Hover over the legend bar to interact with the graphs by clicking on 'Autoscale' or 'Reset axes' to rescale axes."


dropdown_econ_text1 = "To address the economic aspects of CLGSs, levelized cost of heating (LCOH) and levelized cost of electricity (LCOE), \
                        which represent net average present costs, were calculated as follows:"

dropdown_econ_markdown_text1 = """where, **_$C_t$_** is capital expenditures (CAPEX) in year **_t_**, \
                            **_$O_t$_** is operating and maintenance expenditures (OPEX) in year **_t_**, \
                            **_n_** is expected lifetime of the CLGS, \
                            **_r_** is discount rate, \
                            **_$E_h$_** is heat produced in year **_t_**, \
                            and **_$E_e$_** is electricity generated in year **_t_**."""

dropdown_econ_text2 = "Finally, different assumptions were defined based on the working fluid. \
                            For H2O as the heat transfer fluid, an organic Rankine cycle was assumed. \
                            For sCO2 as the circulating fluid, a direct turbine expansion cycle was assumed \
                            where the circulating CO2 is also the working fluid through the cycle."

# title = "About Our Research"
bio1 = " is a PhD student in Energy Resources Engineering working with Professor Roland Horne at \
    the Stanford Doerr School of Sustainability. His PhD research is focused on the \
    optimization of flexible geothermal power and energy storage techno-economics using reinforcement \
    learning algorithms."

team_info1 = "This work was condcuted at the "
team_info2 = "For questions, you may contact "
team_info3 = " at "
team_info4 = " and/or "
ack1 = "We acknowledge the "
ack2 = "  for providing computational resources and support. We also thank "
ack3 = " for their web application template, which facilitated the development of this interface."

user_instructions = "You can either click on the map to specify your location, OR manually input \
    latitude and longitude here. Additionally, you can change depth to select the temperature-at-detph \
    layer on the map view."
    
bio2 = " is the Thomas Davies Barrow Professor of Earth Sciences at Stanford University and Director \
    of the Precourt Institute for Energy. He holds BE, PhD and DSc degrees from the University of\
    Auckland, New Zealand, all in Engineering Science."
    
note = "This is a temperature-at-depth model for the conterminous Untied States, spanning depths of 0-7 kilometers.\
       It was developed using various physical quantities as inputs to a physics-informed graph neural network.\
        This API hosts an upscaled version of our model alongside handy search utilities below. \
        The detailed model alongside its inputs/outputs are accessible on "
        

note2 = " and GDR at "