# Discover Report – Philipp Wimmer

## Topic Description
The focus of my project is to visualize and analyze global electricity production and its composition over time.  
The main goals are to explore how different countries generate electricity, how the share of renewable and non-renewable sources has evolved
and also how these trends relate to environmental impact, particularly CO₂ emissions.

Special attention will be given to Austria, Germany and the top countries worldwide by total GDP.  
The analysis will examine the transition towards renewable energy, identifying leading nations in renewable adoption 
and observing significant developments such as the rapid rise of solar and wind power in recent decades.

My visualizations will include:
- Line charts that show the growth and mix of electricity generation over time
- Stacked area charts comparing renewable vs. non-renewable sources over time
- Bar charts comparing countries or regions  
- Geographical maps to visualize spatial differences in electricity generation

Through these visualizations, my project seeks to provide clear insights into how the global electricity mix is changing
and how different countries are progressing towards sustainable energy goals.

---

## Dataset Description
The dataset used for this project originates from the  
Energy Institute Statistical Review of World Energy
([https://www.energyinst.org/statistical-review/home](https://www.energyinst.org/statistical-review/home)).

It provides comprehensive global data on energy production, consumption, reserves, and emissions across all major energy sources.  
The dataset is available both as an Excel file with multiple sheets and as a consolidated CSV file, 
which merges all relevant information into a single structured format.

For this analysis, the focus is on columns related to electricity generation and also CO₂ emissions, which allow for evaluating energy trends, fuel mix
and environmental impact at a national level.

### Columns of Interest of the Dataset
- **Electricity Generation**
  - `elect_twh` / `electbyfuel_total`: Total Electricity Generation
  - `electbyfuel_coal`: Electricity Generation from Coal
  - `electbyfuel_gas`: Electricity Generation from Natural Gas
  - `electbyfuel_oil`: Electricity Generation from Oil
  - `electbyfuel_nuclear`: Electricity Generation from Nuclear
  - `electbyfuel_hydro` / `hydro_twh`: Electricity Generation from Hydro
  - `electbyfuel_ren_power`: Electricity Generation from Renewables (excluding hydro)
    - `wind_twh`: Wind Generation
    - `solar_twh`: Solar Generation
  - `electbyfuel_other`: Electricity Generation from Other Sources (e.g., biomass, geothermal)
    - `biogeo_twh`: Geothermal, Biomass, and Other Renewable Generation
- **CO₂**
  - `co2_combust_mtco2`: CO₂ Emissions from Energy Combustion
  - `co2_combust_pc`: CO₂ Emissions per Capita

This dataset provides a robust foundation for analyzing electricity generation patterns, comparing renewable vs. non-renewable sources
and assessing the relationship between electricity production and CO₂ emissions** on both national and global scales.
