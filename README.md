# Visual Data Science

## About
I want to visualize energy production data across different countries and energy sources. 
The goal is to create visualizations that allow users to explore trends in energy production over time.

## Data
The data comes from the [Energy Institute Statistical Review of World Energy](https://www.energyinst.org/statistical-review/home).
The dataset also allows for comparison with e.g. CO2 emissions and energy prices.

### Relevant Columns
### Electricity Generation (total and by fuel)
- `elect_twh`: Electricity Generation (total)  
- `electbyfuel_total`: Electricity Generation by Fuel (total of all fuels)  
- `electbyfuel_coal`: Electricity Generation from Coal  
- `electbyfuel_gas`: Electricity Generation from Natural Gas  
- `electbyfuel_oil`: Electricity Generation from Oil  
- `electbyfuel_nuclear`: Electricity Generation from Nuclear  
- `electbyfuel_hydro`: Electricity Generation from Hydro  
- `electbyfuel_ren_power`: Electricity Generation from Renewables (incl. hydro)  
- `electbyfuel_other`: Electricity Generation from Other Sources (e.g., biomass, geothermal)

### Renewable and Low-Carbon Sources (detailed)
- `hydro_twh`: Hydro Generation  
- `hydro_twh_net`: Hydro Generation (net)  
- `wind_twh`: Wind Generation  
- `wind_twh_net`: Wind Generation (net)  
- `solar_twh`: Solar Generation  
- `solar_twh_net`: Solar Generation (net)  
- `biogeo_twh`: Geothermal, Biomass, and Other Renewable Generation  
- `biogeo_twh_net`: Geothermal, Biomass, and Other Renewable Generation (net)  
- `ren_power_twh`: Total Renewable Power Generation (gross)  
- `ren_power_twh_net`: Total Renewable Power Generation (net)

### Emissions (energy-related CO₂)
- `co2_combust_mtco2`: CO₂ from Energy Combustion  
- `co2_combust_pc`: CO₂ from Energy per Capita  
- `co2_combust_per_ej`: CO₂ Intensity (per unit of energy)  
- `co2_mtco2`: Total CO₂ Emissions (incl. process)  
- `gasflared_mtco2`: CO₂ from Gas Flaring  
- `methane_process_mtco2`: Process-related Emissions (Methane to CO₂ equivalent)