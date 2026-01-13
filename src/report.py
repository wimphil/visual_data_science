import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Country Renewable Share",
    page_icon="⚡",
    layout="wide",
)

COLOR_PALETTE = px.colors.qualitative.Safe_r

st.markdown("### Electricity Generation and Renewable Share by Country")

@st.cache_data
def load_data():
    return pd.read_csv("data/preprocessed.csv")

df = load_data()

chart_col, ctrl_col = st.columns([2, 1])

with ctrl_col:
    st.markdown("**Click on one of the points in the scatter plot to select a country in a deeper drilldown!**")
    year_scatter = st.select_slider(
        "Select Year for Scatter Plot",
        options=list(range(1985, 2025)),
        value=2024
    )

    st.text("Note: only countries that provided information about the electricity production per source are included")
    st.text("This dashboard is part of an exercise of the Visual Data Science Course at TU Wien and submitted by Philipp Wimmer")

df_scatter = df[df["Year"] == year_scatter]


fig = px.scatter(
    df_scatter,
    x="ren_power_share",
    y="electbyfuel_total",
    color="Region",
    hover_name="Country",
    custom_data=["Country"],
    title="Renewable Share vs. Log(Total electricity production)",
    color_discrete_sequence=COLOR_PALETTE
)
fig.update_yaxes(
    type="log",
    showgrid=True,
    gridcolor="rgba(255,255,255,0.1)",
    minor=dict(
        showgrid=False,
        ticks=""
    ),
    title_text="Log(Total elect. prod. in TWh)"
)
fig.update_xaxes(showgrid=True, title_text="Share of Renewable Power in total Electricity Production in %")

fig.update_traces(marker=dict(size=10))
with chart_col:
    event = st.plotly_chart(
        fig,
        width='stretch',
        height=300,
        on_select='rerun',
        config={
            "displayModeBar": False
        }
    )

# Default from session state
selected_country = st.session_state.get("selected_country")

sel = getattr(event, "selection", None)

# If we got a selection object, decide whether to set or clear
if sel is not None:
    points = getattr(sel, "points", None)

    # User cleared selection -> points is empty list
    if points is not None and len(points) == 0:
        st.session_state["selected_country"] = None
        selected_country = None

    # User selected a point
    elif points is not None and len(points) > 0:
        selected_country = points[0]["customdata"][0]
        st.session_state["selected_country"] = selected_country


country_section = st.container()

with country_section:
    # country specific
    if selected_country:
        #st.markdown(f"#### Close look at {selected_country}")

        c1, c2, c3 = st.columns(3)

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
            title=f"Electricity mix over time (share) - {selected_country}",
            color_discrete_sequence=COLOR_PALETTE
        )
        fig_mix.update_yaxes(tickformat=".0%", title_text="Share of total")
        fig_mix.update_xaxes(title_text="Year")
        fig_mix.update_layout(
            legend_title_text="Source",
            legend=dict(
                orientation="h",
                yanchor="top",
                y=-0.2,
                xanchor="center",
                x=0.5
            )
        )

        # multiline chart
        fig_abs = px.line(
            df_long,
            x="Year",
            y="TWh",
            color="Source",
            title=f"Electricity generation by source (TWh) - {selected_country}",
            color_discrete_sequence=COLOR_PALETTE
        )
        fig_abs.update_yaxes(title_text="TWh")
        fig_abs.update_xaxes(title_text="Year")
        fig_abs.update_layout(
            legend_title_text="Source",
            legend=dict(
                orientation="h",
                yanchor="top",
                y=-0.2,
                xanchor="center",
                x=0.5
            )
        )

        # line chart (ren and total)
        fig_dual = go.Figure()

        # Total electricity production (left axis)
        fig_dual.add_trace(
            go.Scatter(
                x=df_country["Year"],
                y=df_country["electbyfuel_total"],
                name="Total electricity production (TWh)",
                line=dict(width=3),
                yaxis="y1"
            )
        )

        # Renewable share (right axis)
        fig_dual.add_trace(
            go.Scatter(
                x=df_country["Year"],
                y=df_country["ren_power_share"],
                name="Renewable share (%)",
                line=dict(width=3, dash="dash"),
                yaxis="y2"
            )
        )

        fig_dual.update_layout(
            title=f"Total electricity production and renewable share - {selected_country}",
            xaxis=dict(title="Year"),
            yaxis=dict(
                title="Total electricity production (TWh)",
                showgrid=True
            ),
            yaxis2=dict(
                title="Renewable share (%)",
                overlaying="y",
                side="right",
                range=[0, 100],
                showgrid=False
            ),
            legend=dict(
                orientation="h",
                yanchor="top",
                y=-0.25,
                xanchor="center",
                x=0.5
            ),
            margin=dict(b=120)
        )

        with c1:
            st.plotly_chart(fig_mix, width="stretch", config={"displayModeBar": False}, height=400)

        with c2:
            st.plotly_chart(fig_abs, width="stretch", config={"displayModeBar": False}, height=400)

        with c3:
            st.plotly_chart(fig_dual, width="stretch", config={"displayModeBar": False}, height=400)

