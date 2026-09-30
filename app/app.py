from pathlib import Path

import streamlit as st
import pandas as pd
import plotly.graph_objects as go


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Football Match Intelligence",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# PATHS
# ============================================================

APP_DIR = Path(__file__).resolve().parent
PROJECT_DIR = APP_DIR.parent

ASSETS_DIR = PROJECT_DIR / "assets"
RAW_DIR = PROJECT_DIR / "data" / "raw"

CITY_LOGO = ASSETS_DIR / "city.png"
QPR_LOGO = ASSETS_DIR / "qpr.png"

EVENTS_FILE = RAW_DIR / "city_qpr_events.csv"
STATS_FILE = RAW_DIR / "city_qpr_match_stats.csv"


# ============================================================
# CSS
# ============================================================

st.html("""
<style>

.stApp {
    background:
        radial-gradient(circle at 85% 5%, rgba(38,105,145,0.10), transparent 25%),
        linear-gradient(135deg, #04111a 0%, #061722 55%, #041018 100%);
    color: #edf5fa;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #06131d 0%, #041019 100%);
    border-right: 1px solid #164057;
}

h1, h2, h3, h4, p, span, div {
    font-family: Arial, Helvetica, sans-serif;
}

.side-brand {
    padding: 20px 5px 28px 5px;
    border-bottom: 1px solid #173b4e;
    margin-bottom: 25px;
}

.side-kicker {
    color: #69b9e9;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.side-title {
    color: #f4f8fb;
    font-size: 25px;
    font-weight: 900;
    line-height: 0.95;
    margin-top: 8px;
}

.side-subtitle {
    color: #66899d;
    font-size: 9px;
    letter-spacing: 1px;
    margin-top: 10px;
    text-transform: uppercase;
}

.side-section {
    color: #70a7c5;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 2px;
    margin: 22px 0 10px 0;
    text-transform: uppercase;
}

.competition-bar {
    background: linear-gradient(90deg, #0b2637, #09202f, #0b2637);
    border: 1px solid #164a65;
    border-radius: 12px;
    padding: 10px;
    text-align: center;
    color: #6e94a7;
    font-size: 8px;
    font-weight: 800;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 12px;
}

.team-name {
    color: #6fb9e5;
    font-size: 11px;
    font-weight: 900;
    letter-spacing: 1px;
    text-transform: uppercase;
    text-align: center;
}

.qpr-name {
    color: #e8edf0;
}

.score {
    color: #f5f8fa;
    font-size: 43px;
    font-weight: 900;
    line-height: 1;
    text-align: center;
    letter-spacing: 2px;
}

.full-time {
    color: #7893a1;
    font-size: 8px;
    font-weight: 800;
    letter-spacing: 2px;
    text-align: center;
    margin-top: 5px;
}

.comeback-tag {
    color: #f1c84f;
    font-size: 8px;
    font-weight: 900;
    letter-spacing: 1px;
    text-align: center;
    margin-top: 7px;
    text-transform: uppercase;
}

.kpi-card {
    position: relative;
    overflow: hidden;
    background: linear-gradient(145deg, #0b2535, #081b28);
    border: 1px solid #17465d;
    border-radius: 8px;
    padding: 14px;
    min-height: 66px;
}

.kpi-card:after {
    content: "";
    position: absolute;
    width: 55px;
    height: 55px;
    right: -18px;
    bottom: -22px;
    border-radius: 50%;
    background: rgba(69,142,184,0.10);
}

.kpi-label {
    color: #6e8fa1;
    font-size: 7px;
    font-weight: 900;
    letter-spacing: 1.5px;
    text-transform: uppercase;
}

.kpi-value {
    color: #eef6fa;
    font-size: 21px;
    font-weight: 900;
    margin-top: 5px;
}

.kpi-primary {
    color: #70bce9;
}

.section-head {
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid #173d50;
    padding-bottom: 8px;
    margin-top: 28px;
    margin-bottom: 14px;
}

.section-title {
    color: #eaf3f7;
    font-size: 12px;
    font-weight: 900;
    letter-spacing: 1.5px;
    text-transform: uppercase;
}

.section-meta {
    color: #567688;
    font-size: 7px;
    font-weight: 800;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.panel-title {
    background: linear-gradient(145deg, #0b2230, #081a26);
    border: 1px solid #17445b;
    border-radius: 9px;
    padding: 11px;
    margin-bottom: 5px;
}

.panel-title-main {
    color: #e9f1f5;
    font-size: 10px;
    font-weight: 900;
}

.panel-title-sub {
    color: #68899a;
    font-size: 7px;
    margin-top: 3px;
}

.comeback-card {
    background: linear-gradient(145deg, #091e2b, #071721);
    border: 1px solid #17465d;
    border-radius: 12px;
    padding: 20px;
    min-height: 145px;
}

.comeback-card.gold {
    border-color: #66552a;
}

.comeback-kicker {
    color: #67b6e5;
    font-size: 9px;
    font-weight: 900;
    letter-spacing: 1.5px;
}

.comeback-kicker.gold {
    color: #f0c54a;
}

.comeback-number {
    color: #f1f7fa;
    font-size: 27px;
    font-weight: 900;
    margin-top: 10px;
}

.comeback-description {
    color: #8da5b2;
    font-size: 12px;
    line-height: 1.5;
    margin-top: 8px;
}

.insight-box {
    background: #081b27;
    border-left: 3px solid #5ba9d7;
    border-radius: 5px;
    padding: 15px 17px;
    color: #9db3be;
    font-size: 12px;
    line-height: 1.6;
}

.insight-title {
    color: #e8f1f5;
    font-weight: 900;
    font-size: 11px;
    letter-spacing: 1px;
    margin-bottom: 6px;
}

/* KEY INSIGHTS */

.key-insight {
    background: linear-gradient(145deg, #091f2d, #071821);
    border: 1px solid #17465d;
    border-radius: 10px;
    padding: 18px;
    min-height: 135px;
}

.key-number {
    color: #5da9d7;
    font-size: 10px;
    font-weight: 900;
    letter-spacing: 2px;
}

.key-title {
    color: #eef6fa;
    font-size: 15px;
    font-weight: 900;
    margin-top: 8px;
    text-transform: uppercase;
}

.key-text {
    color: #8ea7b5;
    font-size: 11px;
    line-height: 1.55;
    margin-top: 8px;
}

.key-highlight {
    color: #70bce9;
    font-weight: 900;
}

.key-gold {
    color: #f1c84f;
    font-weight: 900;
}

.footer {
    border-top: 1px solid #173d50;
    margin-top: 35px;
    padding: 18px;
    text-align: center;
    color: #4d7182;
    font-size: 7px;
    letter-spacing: 1px;
    text-transform: uppercase;
}

</style>
""")


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    events = pd.read_csv(EVENTS_FILE)
    stats = pd.read_csv(STATS_FILE)

    events.columns = [str(c).strip() for c in events.columns]
    stats.columns = [str(c).strip() for c in stats.columns]

    if "metric" in stats.columns:
        stats = stats.rename(columns={"metric": "Metric"})

    # Your CSV contains score_after.
    # Rename it internally so the rest of the app can use score.
    if "score_after" in events.columns:
        events = events.rename(
            columns={"score_after": "score"}
        )

    events["minute"] = pd.to_numeric(
        events["minute"],
        errors="coerce"
    )

    if "minute_display" not in events.columns:

        def format_minute(x):

            if pd.isna(x):
                return ""

            if int(x) == 92:
                return "90+2'"

            if int(x) == 94:
                return "90+4'"

            return f"{int(x)}'"

        events["minute_display"] = events["minute"].apply(
            format_minute
        )

    return events, stats


events, match_stats = load_data()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.html("""
    <div class="side-brand">
        <div class="side-kicker">Football Analytics</div>
        <div class="side-title">MATCH<br>INTELLIGENCE</div>
        <div class="side-subtitle">Manchester City × QPR</div>
    </div>
    """)

    st.html('<div class="side-section">Dashboard</div>')

    view = st.radio(
        "Dashboard",
        ["Overview", "Match Events", "Statistics"],
        label_visibility="collapsed"
    )

    st.html('<div class="side-section">Event Filter</div>')

    event_types = sorted(
        events["event"].dropna().unique().tolist()
    )

    selected_events = st.multiselect(
        "Event types",
        event_types,
        default=event_types,
        label_visibility="collapsed"
    )

    st.html('<div class="side-section">Match Window</div>')

    minute_range = st.slider(
        "Match minute",
        min_value=0,
        max_value=95,
        value=(0, 95),
        label_visibility="collapsed"
    )

    st.markdown("---")

    st.caption("13 MAY 2012")
    st.caption("PREMIER LEAGUE")
    st.caption("ETIHAD STADIUM")


# ============================================================
# FILTER EVENTS
# ============================================================

filtered_events = events[
    (events["event"].isin(selected_events))
    & (events["minute"] >= minute_range[0])
    & (events["minute"] <= minute_range[1])
].copy()


# ============================================================
# HEADER
# ============================================================

st.html("""
<div class="competition-bar">
    Premier League · 2011/12 · Etihad Stadium
</div>
""")


header_left, header_score, header_right = st.columns(
    [1.5, 1, 1.5],
    vertical_alignment="center"
)


with header_left:

    logo_col, name_col = st.columns(
        [0.65, 1.35],
        vertical_alignment="center"
    )

    with logo_col:
        if CITY_LOGO.exists():
            st.image(CITY_LOGO, width=58)

    with name_col:
        st.html("""
        <div class="team-name">
            Manchester City
        </div>
        """)


with header_score:

    st.html("""
    <div class="score">3–2</div>
    <div class="full-time">FULL TIME</div>
    <div class="comeback-tag">THE 90+4 COMEBACK</div>
    """)


with header_right:

    logo_col, name_col = st.columns(
        [0.65, 1.35],
        vertical_alignment="center"
    )

    with logo_col:
        if QPR_LOGO.exists():
            st.image(QPR_LOGO, width=58)

    with name_col:
        st.html("""
        <div class="team-name qpr-name">
            QPR
        </div>
        """)


# ============================================================
# KPI CARDS
# ============================================================

home_stats = {}

for _, row in match_stats.iterrows():
    home_stats[row["Metric"]] = row["Manchester City"]


kpi_data = [
    ("Possession", f"{home_stats.get('Possession', 81.3)}%"),
    ("Shots", f"{home_stats.get('Shots', 44)}"),
    ("Shots on Target", f"{home_stats.get('Shots on Target', 15)}"),
    ("Corners", f"{home_stats.get('Corners', 19)}"),
    ("Passes", f"{home_stats.get('Passes', 710)}"),
]

kpi_cols = st.columns(5)

for i, (label, value) in enumerate(kpi_data):

    with kpi_cols[i]:

        primary_class = (
            "kpi-primary"
            if i == 0
            else ""
        )

        st.html(f"""
        <div class="kpi-card">
            <div class="kpi-label">{label}</div>
            <div class="kpi-value {primary_class}">
                {value}
            </div>
        </div>
        """)


# ============================================================
# PLOTLY THEME
# ============================================================

PLOT_BG = "rgba(0,0,0,0)"
GRID_COLOR = "#173847"
TEXT_COLOR = "#dce8ee"
CITY_COLOR = "#6fb6e4"
QPR_COLOR = "#e5ebef"


def style_figure(fig):

    fig.update_layout(
        paper_bgcolor=PLOT_BG,
        plot_bgcolor=PLOT_BG,
        font=dict(
            family="Arial",
            color=TEXT_COLOR,
            size=10
        ),
        margin=dict(
            l=45,
            r=25,
            t=20,
            b=45
        ),
        hoverlabel=dict(
            bgcolor="#081722",
            font_color="#ffffff"
        ),
        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            font=dict(size=10)
        )
    )

    fig.update_xaxes(
        gridcolor=GRID_COLOR,
        zerolinecolor=GRID_COLOR,
        tickfont=dict(size=9)
    )

    fig.update_yaxes(
        gridcolor=GRID_COLOR,
        zerolinecolor=GRID_COLOR,
        tickfont=dict(size=9)
    )

    return fig


# ============================================================
# OVERVIEW
# ============================================================

if view == "Overview":

    # --------------------------------------------------------
    # MATCH FLOW
    # --------------------------------------------------------

    st.html("""
    <div class="section-head">
        <div class="section-title">Match Flow</div>
        <div class="section-meta">
            Score · Attacking Volume
        </div>
    </div>
    """)

    flow_left, flow_right = st.columns(2)


    # SCORE EVOLUTION

    with flow_left:

        st.html("""
        <div class="panel-title">
            <div class="panel-title-main">
                Score evolution
            </div>

            <div class="panel-title-sub">
                Goals accumulated throughout the match
            </div>
        </div>
        """)

        city_score = 0
        qpr_score = 0

        score_minutes = [0]
        city_scores = [0]
        qpr_scores = [0]

        for _, row in events.sort_values("minute").iterrows():

            if row["event"] == "Goal":

                if row["team"] == "Manchester City":
                    city_score += 1

                elif row["team"] == "Queens Park Rangers":
                    qpr_score += 1

                score_minutes.append(row["minute"])
                city_scores.append(city_score)
                qpr_scores.append(qpr_score)

        fig_score = go.Figure()

        fig_score.add_trace(
            go.Scatter(
                x=score_minutes,
                y=city_scores,
                name="Manchester City",
                mode="lines+markers",
                line=dict(
                    color=CITY_COLOR,
                    width=3,
                    shape="hv"
                ),
                marker=dict(size=6)
            )
        )

        fig_score.add_trace(
            go.Scatter(
                x=score_minutes,
                y=qpr_scores,
                name="QPR",
                mode="lines+markers",
                line=dict(
                    color=QPR_COLOR,
                    width=2,
                    shape="hv"
                ),
                marker=dict(size=5)
            )
        )

        fig_score.update_layout(
            xaxis_title="Minute",
            yaxis_title="Goals",
            yaxis=dict(
                dtick=1,
                range=[0, 3.5]
            ),
            hovermode="x unified"
        )

        st.plotly_chart(
            style_figure(fig_score),
            use_container_width=True,
            config={"displayModeBar": False}
        )


    # ATTACKING PRESSURE

    with flow_right:

        st.html("""
        <div class="panel-title">
            <div class="panel-title-main">
                Attacking pressure
            </div>

            <div class="panel-title-sub">
                Shot volume across key phases
            </div>
        </div>
        """)

        pressure_labels = [
            "City",
            "QPR",
            "City 2H",
            "City after QPR final shot"
        ]

        pressure_values = [44, 3, 34, 23]

        fig_pressure = go.Figure()

        fig_pressure.add_trace(
            go.Bar(
                x=pressure_labels,
                y=pressure_values,
                marker_color=[
                    "#6fb6e4",
                    "#e5ebef",
                    "#86c0e6",
                    "#4c98c7"
                ],
                text=pressure_values,
                textposition="outside",
                hovertemplate=(
                    "%{x}: %{y} shots<extra></extra>"
                )
            )
        )

        fig_pressure.update_layout(
            yaxis_title="Shots",
            showlegend=False,
            yaxis=dict(range=[0, 50])
        )

        st.plotly_chart(
            style_figure(fig_pressure),
            use_container_width=True,
            config={"displayModeBar": False}
        )


    # --------------------------------------------------------
    # MATCH ANALYTICS
    # --------------------------------------------------------

    st.html("""
    <div class="section-head">
        <div class="section-title">
            Match Analytics
        </div>

        <div class="section-meta">
            Efficiency · Volume
        </div>
    </div>
    """)

    analytics_left, analytics_right = st.columns(2)


    # SHOT EFFICIENCY

    with analytics_left:

        st.html("""
        <div class="panel-title">
            <div class="panel-title-main">
                Shot efficiency
            </div>

            <div class="panel-title-sub">
                Conversion through the attacking chain
            </div>
        </div>
        """)

        efficiency = pd.DataFrame({
            "Stage": [
                "Shot → Goal",
                "Shot → On Target",
                "On Target → Goal"
            ],
            "Manchester City": [
                3 / 44 * 100,
                15 / 44 * 100,
                3 / 15 * 100
            ],
            "QPR": [
                2 / 3 * 100,
                3 / 3 * 100,
                2 / 3 * 100
            ]
        })

        fig_eff = go.Figure()

        fig_eff.add_trace(
            go.Bar(
                x=efficiency["Stage"],
                y=efficiency["Manchester City"],
                name="Manchester City",
                marker_color=CITY_COLOR
            )
        )

        fig_eff.add_trace(
            go.Bar(
                x=efficiency["Stage"],
                y=efficiency["QPR"],
                name="QPR",
                marker_color=QPR_COLOR
            )
        )

        fig_eff.update_layout(
            barmode="group",
            yaxis_title="Percentage",
            yaxis=dict(range=[0, 110])
        )

        st.plotly_chart(
            style_figure(fig_eff),
            use_container_width=True,
            config={"displayModeBar": False}
        )


    # CITY SHOT VOLUME

    with analytics_right:

        st.html("""
        <div class="panel-title">
            <div class="panel-title-main">
                City shot volume
            </div>

            <div class="panel-title-sub">
                Match-wide attacking output
            </div>
        </div>
        """)

        fig_volume = go.Figure()

        fig_volume.add_trace(
            go.Bar(
                x=[
                    "Total shots",
                    "Second-half shots",
                    "After QPR final shot"
                ],
                y=[
                    44,
                    34,
                    23
                ],
                marker_color=[
                    "#6fb6e4",
                    "#86c0e6",
                    "#4c98c7"
                ],
                text=[
                    44,
                    34,
                    23
                ],
                textposition="outside"
            )
        )

        fig_volume.update_layout(
            yaxis_title="Shots",
            showlegend=False,
            yaxis=dict(range=[0, 50])
        )

        st.plotly_chart(
            style_figure(fig_volume),
            use_container_width=True,
            config={"displayModeBar": False}
        )


    # --------------------------------------------------------
    # KEY INSIGHTS
    # --------------------------------------------------------

    st.html("""
    <div class="section-head">
        <div class="section-title">
            Key Insights
        </div>

        <div class="section-meta">
            Data-driven match story
        </div>
    </div>

    <div style="
        color:#8099a8;
        font-size:12px;
        margin-bottom:16px;
    ">
        Three observations that explain the shape of the match.
    </div>
    """)

    insight1, insight2, insight3 = st.columns(3)


    with insight1:

        st.html("""
        <div class="key-insight">

            <div class="key-number">
                01 / DOMINANCE
            </div>

            <div class="key-title">
                City controlled the ball
            </div>

            <div class="key-text">
                Manchester City recorded
                <span class="key-highlight">81.3%</span>
                possession and produced
                <span class="key-highlight">44 shots</span>,
                compared with QPR's 3.
            </div>

        </div>
        """)


    with insight2:

        st.html("""
        <div class="key-insight">

            <div class="key-number">
                02 / PRESSURE
            </div>

            <div class="key-title">
                Pressure continued late
            </div>

            <div class="key-text">
                After QPR's final recorded shot,
                City generated another
                <span class="key-highlight">23 shots</span>
                before the final whistle.
            </div>

        </div>
        """)


    with insight3:

        st.html("""
        <div class="key-insight">

            <div class="key-number">
                03 / TURNAROUND
            </div>

            <div class="key-title">
                Two goals changed everything
            </div>

            <div class="key-text">
                Džeko equalised at
                <span class="key-gold">90+2'</span>
                before Agüero scored at
                <span class="key-gold">90+4'</span>.
                The goals arrived about 125 seconds apart.
            </div>

        </div>
        """)


# ============================================================
# MATCH EVENTS
# ============================================================

elif view == "Match Events":

    st.html("""
    <div class="section-head">
        <div class="section-title">
            Match Events
        </div>

        <div class="section-meta">
            Filtered event timeline
        </div>
    </div>
    """)


    # EVENT TIMELINE

    fig_events = go.Figure()

    city_events = filtered_events[
        filtered_events["team"] == "Manchester City"
    ]

    qpr_events = filtered_events[
        filtered_events["team"] == "Queens Park Rangers"
    ]


    fig_events.add_trace(
        go.Scatter(
            x=city_events["minute"],
            y=[1] * len(city_events),
            mode="markers+text",
            name="Manchester City",
            text=city_events["player"],
            textposition="top center",
            marker=dict(
                size=11,
                color=CITY_COLOR,
                line=dict(
                    color="#d7efff",
                    width=1
                )
            ),
            customdata=city_events[
                [
                    "minute_display",
                    "event",
                    "player",
                    "score"
                ]
            ],
            hovertemplate=(
                "<b>Manchester City</b><br>"
                "%{customdata[0]}<br>"
                "%{customdata[2]}<br>"
                "%{customdata[1]}<br>"
                "Score: %{customdata[3]}"
                "<extra></extra>"
            )
        )
    )


    fig_events.add_trace(
        go.Scatter(
            x=qpr_events["minute"],
            y=[0] * len(qpr_events),
            mode="markers+text",
            name="QPR",
            text=qpr_events["player"],
            textposition="bottom center",
            marker=dict(
                size=11,
                color=QPR_COLOR,
                line=dict(
                    color="#ffffff",
                    width=1
                )
            ),
            customdata=qpr_events[
                [
                    "minute_display",
                    "event",
                    "player",
                    "score"
                ]
            ],
            hovertemplate=(
                "<b>QPR</b><br>"
                "%{customdata[0]}<br>"
                "%{customdata[2]}<br>"
                "%{customdata[1]}<br>"
                "Score: %{customdata[3]}"
                "<extra></extra>"
            )
        )
    )


    fig_events.update_layout(
        height=310,
        xaxis_title="Match minute",
        yaxis=dict(
            showticklabels=False,
            range=[-0.7, 1.7],
            gridcolor=GRID_COLOR
        ),
        xaxis=dict(
            range=[
                max(0, minute_range[0] - 3),
                min(95, minute_range[1] + 3)
            ]
        ),
        hovermode="closest"
    )

    st.plotly_chart(
        style_figure(fig_events),
        use_container_width=True,
        config={"displayModeBar": False}
    )


    # EVENT LOG

    st.html("""
    <div class="section-head">
        <div class="section-title">
            Event Log
        </div>

        <div class="section-meta">
            Match chronology
        </div>
    </div>
    """)

    display_events = filtered_events.copy()

    display_columns = [
        "minute_display",
        "team",
        "player",
        "event",
        "score"
    ]

    display_events = display_events[
        [
            c
            for c in display_columns
            if c in display_events.columns
        ]
    ]

    display_events = display_events.rename(
        columns={
            "minute_display": "Minute",
            "team": "Team",
            "player": "Player",
            "event": "Event",
            "score": "Score"
        }
    )

    st.dataframe(
        display_events,
        use_container_width=True,
        hide_index=True,
        height=280
    )


    # COMEBACK ANALYSIS

    st.html("""
    <div class="section-head">
        <div class="section-title">
            Comeback Analysis
        </div>

        <div class="section-meta">
            Late-game turnaround
        </div>
    </div>

    <div style="
        color:#8099a8;
        font-size:12px;
        margin-bottom:18px;
    ">
        How Manchester City turned a 1–2 deficit into a 3–2 victory
        in the final minutes.
    </div>
    """)


    comeback_col1, comeback_col2, comeback_col3, comeback_col4 = st.columns(4)


    with comeback_col1:

        st.html("""
        <div class="comeback-card">

            <div class="comeback-kicker">
                QPR LEAD
            </div>

            <div class="comeback-number">
                2–1
            </div>

            <div class="comeback-description">
                Jamie Mackie puts QPR ahead at 66'.
            </div>

        </div>
        """)


    with comeback_col2:

        st.html("""
        <div class="comeback-card">

            <div class="comeback-kicker">
                CITY SHOTS AFTER
            </div>

            <div class="comeback-number">
                23
            </div>

            <div class="comeback-description">
                City recorded 23 shots after QPR's final recorded shot.
            </div>

        </div>
        """)


    with comeback_col3:

        st.html("""
        <div class="comeback-card gold">

            <div class="comeback-kicker gold">
                EQUALISER
            </div>

            <div class="comeback-number">
                90+2'
            </div>

            <div class="comeback-description">
                Edin Džeko makes it 2–2.
            </div>

        </div>
        """)


    with comeback_col4:

        st.html("""
        <div class="comeback-card gold">

            <div class="comeback-kicker gold">
                WINNER
            </div>

            <div class="comeback-number">
                90+4'
            </div>

            <div class="comeback-description">
                Sergio Agüero completes the turnaround.
            </div>

        </div>
        """)


    st.markdown("")

    sequence_left, sequence_right = st.columns(2)


    with sequence_left:

        st.html("""
        <div class="insight-box">

            <div class="insight-title">
                ATTACKING PRESSURE
            </div>

            Manchester City recorded
            <b>44 shots</b> compared with QPR's
            <b>3</b>.

            After QPR's final recorded shot around
            the 65th minute, City produced
            <b>23 additional shots</b>
            before the final whistle.

        </div>
        """)


    with sequence_right:

        st.html("""
        <div class="insight-box">

            <div class="insight-title">
                LATE-GAME IMPACT
            </div>

            City scored twice in stoppage time:
            <b>90+2' — Džeko</b>
            and
            <b>90+4' — Agüero</b>.

            The final two goals were separated by approximately
            <b>125 seconds</b>.

        </div>
        """)


# ============================================================
# STATISTICS
# ============================================================

elif view == "Statistics":

    st.html("""
    <div class="section-head">
        <div class="section-title">
            Match Statistics
        </div>

        <div class="section-meta">
            Manchester City vs QPR
        </div>
    </div>
    """)

    stat_left, stat_right = st.columns(2)


    # POSSESSION

    with stat_left:

        st.html("""
        <div class="panel-title">

            <div class="panel-title-main">
                Possession
            </div>

            <div class="panel-title-sub">
                Share of the ball
            </div>

        </div>
        """)

        possession_city = float(
            match_stats.loc[
                match_stats["Metric"] == "Possession",
                "Manchester City"
            ].iloc[0]
        )

        possession_qpr = float(
            match_stats.loc[
                match_stats["Metric"] == "Possession",
                "Queens Park Rangers"
            ].iloc[0]
        )

        fig_possession = go.Figure()

        fig_possession.add_trace(
            go.Bar(
                x=[
                    "Manchester City",
                    "QPR"
                ],
                y=[
                    possession_city,
                    possession_qpr
                ],
                marker_color=[
                    CITY_COLOR,
                    QPR_COLOR
                ],
                text=[
                    f"{possession_city:.1f}%",
                    f"{possession_qpr:.1f}%"
                ],
                textposition="outside"
            )
        )

        fig_possession.update_layout(
            yaxis_title="Possession %",
            yaxis=dict(range=[0, 105]),
            showlegend=False
        )

        st.plotly_chart(
            style_figure(fig_possession),
            use_container_width=True,
            config={"displayModeBar": False}
        )


    # ATTACKING OUTPUT

    with stat_right:

        st.html("""
        <div class="panel-title">

            <div class="panel-title-main">
                Attacking output
            </div>

            <div class="panel-title-sub">
                Shots and shots on target
            </div>

        </div>
        """)

        shots_city = float(
            match_stats.loc[
                match_stats["Metric"] == "Shots",
                "Manchester City"
            ].iloc[0]
        )

        shots_qpr = float(
            match_stats.loc[
                match_stats["Metric"] == "Shots",
                "Queens Park Rangers"
            ].iloc[0]
        )

        target_city = float(
            match_stats.loc[
                match_stats["Metric"] == "Shots on Target",
                "Manchester City"
            ].iloc[0]
        )

        target_qpr = float(
            match_stats.loc[
                match_stats["Metric"] == "Shots on Target",
                "Queens Park Rangers"
            ].iloc[0]
        )

        fig_attack = go.Figure()

        fig_attack.add_trace(
            go.Bar(
                x=[
                    "Manchester City",
                    "QPR"
                ],
                y=[
                    shots_city,
                    shots_qpr
                ],
                name="Shots",
                marker_color=CITY_COLOR
            )
        )

        fig_attack.add_trace(
            go.Bar(
                x=[
                    "Manchester City",
                    "QPR"
                ],
                y=[
                    target_city,
                    target_qpr
                ],
                name="Shots on Target",
                marker_color=QPR_COLOR
            )
        )

        fig_attack.update_layout(
            barmode="group",
            yaxis_title="Attempts"
        )

        st.plotly_chart(
            style_figure(fig_attack),
            use_container_width=True,
            config={"displayModeBar": False}
        )


    # FULL MATCH TABLE

    st.html("""
    <div class="section-head">

        <div class="section-title">
            Full Match Table
        </div>

        <div class="section-meta">
            Recorded statistics
        </div>

    </div>
    """)

    st.dataframe(
        match_stats,
        use_container_width=True,
        hide_index=True,
        height=360
    )


# ============================================================
# FOOTER
# ============================================================

st.html("""
<div class="footer">

    Football Match Intelligence · Manchester City 3–2 QPR · 13 May 2012

    <br>

    Data storytelling · Match analytics · Interactive dashboard

</div>
""")