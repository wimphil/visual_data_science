import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Country Renewable Share",
    page_icon="⚡",
    layout="wide",
)

st.title("Country Renewable Share")
st.markdown("Click on one of the points in the scatter plot to select a country in a deeper drilldown!")

@st.cache_data
def load_data():
    return pd.read_csv("data/preprocessed.csv")

df = load_data()

year_scatter = st.select_slider(
    "Select Year",
    options=list(range(1985, 2025)),
    value=2024
)

df_scatter = df[df["Year"] == year_scatter]

col1, col2 = st.columns(2)

fig = px.scatter(
    df_scatter,
    x="ren_power_share",
    y="electbyfuel_total",
    color="Region",
    hover_name="Country",
    custom_data=["Country"]
)
fig.update_yaxes(
    type="log",
    showgrid=True,
    gridcolor="rgba(255,255,255,0.1)",
    minor=dict(
        showgrid=False,
        ticks=""
    ),
    title_text="Log(Total electricity production in TWh)"
)
fig.update_xaxes(showgrid=True, title_text="Share of Renewable Power in total Electricity Production")

fig.update_traces(marker=dict(size=10))
with col1:
    event = st.plotly_chart(
        fig,
        width='stretch',
        on_select='rerun',
        config={
            "displayModeBar": False
        }
    )

with col2:
    st.bar_chart(
        df_scatter,
        y="ren_power_share",
        x="Country",
        horizontal=True,
        sort="-ren_power_share",
        color="Region"
    )

# Extract selected country (works with Streamlit's plot selection object)
selected_country = st.session_state.get("selected_country")

sel = getattr(event, "selection", None)
if sel and getattr(sel, "points", None) and len(sel.points) > 0:
    # first selected point
    selected_country = sel.points[0]["customdata"][0]
    st.session_state["selected_country"] = selected_country

country_section = st.container()

with country_section:
    # country specific
    if selected_country:
        st.markdown(f"## Close look at {selected_country}")

        c1, c2 = st.columns(2)

        df_country = df[df["Country"] == selected_country].copy()

        source_cols = [
        'electbyfuel_coal', 'electbyfuel_gas', 'electbyfuel_oil',
        'electbyfuel_nuclear', 'electbyfuel_hydro',
        'electbyfuel_ren_power',
        'electbyfuel_other'
    ]

        df_long = df_country.melt(
            id_vars=["Country", "Year"],
            value_vars=source_cols,
            var_name="Source",
            value_name="TWh"
        )

        # 100 % stacked area
        fig_mix = px.area(
            df_long,
            x="Year",
            y="TWh",
            color="Source",
            groupnorm="fraction",  # <-- makes it 100% stacked
            title=f"Electricity mix over time (share) — {selected_country}",
        )
        fig_mix.update_yaxes(tickformat=".0%", title_text="Share of total")
        fig_mix.update_xaxes(title_text="Year")
        fig_mix.update_layout(legend_title_text="Source")

        # multiline chart
        fig_abs = px.line(
            df_long,
            x="Year",
            y="TWh",
            color="Source",
            title=f"Electricity generation by source (TWh) — {selected_country}",
        )
        fig_abs.update_yaxes(title_text="TWh")
        fig_abs.update_xaxes(title_text="Year")
        fig_abs.update_layout(legend_title_text="Source")

        with c1:
            st.plotly_chart(fig_mix, width="stretch", config={"displayModeBar": False})

        with c2:
            st.plotly_chart(fig_abs, width="stretch", config={"displayModeBar": False})
