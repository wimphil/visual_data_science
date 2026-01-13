import pandas as pd

df = pd.read_csv("../data/EL_Stats_Review/panel_format.csv")

# keep relevant columns
columns_to_keep = [
    # general information
    "Country", "Year", "pop", "Region", "SubRegion", "ISO3166_alpha3",
    # metrics
    'elect_twh', 'electbyfuel_total',
    'electbyfuel_coal', 'electbyfuel_gas', 'electbyfuel_oil',
    'electbyfuel_nuclear', 'electbyfuel_hydro', 'hydro_twh',
    'electbyfuel_ren_power', 'wind_twh', 'solar_twh',
    'electbyfuel_other', 'biogeo_twh',
    'co2_combust_mtco2', 'co2_combust_pc',
]
df_all_countries = df[columns_to_keep].copy()

# remove all years before 1985
df_all_countries = df_all_countries[df_all_countries.Year >= 1985]

df_all_countries = df_all_countries.dropna(axis=0, subset=['Region'])

ren_power_cols = ['electbyfuel_ren_power', 'electbyfuel_hydro']

df_all_countries['ren_power_share'] = df_all_countries[ren_power_cols].sum(axis=1) / df_all_countries['electbyfuel_total']*100

df_all_countries = df_all_countries.dropna(axis=0, subset=['ren_power_share'])

df_all_countries.to_csv("../data/preprocessed.csv", index=False)
