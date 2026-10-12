import streamlit as st
import pandas as pd
from pathlib import Path
from itertools import product

# ============================================================
# 1. PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="Green India | Environmental Optimization",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

BASE_DIR = Path(__file__).resolve().parent

# ============================================================
# 2. PROFESSIONAL NATURE-INSPIRED THEME
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');

:root {
    --forest: #075b3b;
    --leaf: #168653;
    --mint: #eaf7ef;
    --ink: #15382e;
    --muted: #587268;
    --line: #d7e9de;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background:
        radial-gradient(ellipse at 8% 4%, rgba(201, 239, 213, .42), transparent 30%),
        radial-gradient(ellipse at 95% 18%, rgba(222, 245, 229, .55), transparent 27%),
        linear-gradient(180deg, #f8fcf9 0%, #f3f9f5 52%, #ffffff 100%);
    color: var(--ink);
}

.block-container {
    max-width: 1450px;
    padding-top: 1.3rem;
    padding-bottom: 2.4rem;
}

h1, h2, h3 {
    font-family: 'Manrope', sans-serif !important;
    color: var(--forest) !important;
    letter-spacing: -0.025em;
}

h1 { font-weight: 800 !important; }
h2, h3 { font-weight: 700 !important; }

.hero {
    position: relative;
    overflow: hidden;
    border-radius: 24px;
    padding: 2.3rem 2.5rem;
    margin-bottom: 1.35rem;
    color: #fff;
    background:
      linear-gradient(100deg, rgba(4, 61, 40, .96) 0%, rgba(8, 94, 59, .88) 48%, rgba(16, 105, 65, .60) 100%),
      url("https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?auto=format&fit=crop&w=1800&q=85");
    background-size: cover;
    background-position: center 48%;
    box-shadow: 0 12px 30px rgba(8, 81, 51, .14);
    border: 1px solid rgba(255,255,255,.5);
}
.hero:after {
    content: "🌿";
    position: absolute;
    right: 4%;
    top: 4%;
    font-size: 5rem;
    opacity: .22;
    transform: rotate(-18deg);
}
.hero-kicker {
    color: #c9f5d8;
    font-size: .82rem;
    font-weight: 700;
    letter-spacing: .16em;
    text-transform: uppercase;
    margin-bottom: .5rem;
}
.hero h1 {
    color: #fff !important;
    font-size: clamp(2rem, 4vw, 3.3rem) !important;
    line-height: 1.12;
    margin: 0 0 .4rem 0;
}
.hero-subtitle {
    color: #effff4;
    font-size: clamp(1rem, 1.8vw, 1.3rem);
    font-weight: 600;
    margin-bottom: .7rem;
}
.hero-copy {
    color: #e2f5e9;
    font-size: 1rem;
    max-width: 780px;
    line-height: 1.65;
    margin-bottom: 0;
}
.section-card {
    background: rgba(255,255,255,.92);
    border: 1px solid var(--line);
    border-radius: 18px;
    padding: 1.15rem 1.3rem;
    box-shadow: 0 5px 18px rgba(14, 82, 52, .045);
    margin-bottom: 1rem;
}
.about-card {
    background: linear-gradient(125deg, rgba(237, 250, 241, .98), rgba(255,255,255,.96));
    border: 1px solid #cfe8d8;
    border-radius: 20px;
    padding: 1.45rem 1.5rem;
    box-shadow: 0 7px 22px rgba(14, 82, 52, .055);
    margin-bottom: 1.2rem;
}
.about-label {
    font-size: .76rem;
    font-weight: 800;
    letter-spacing: .12em;
    text-transform: uppercase;
    color: var(--leaf);
    margin-bottom: .4rem;
}
.about-title {
    font-family: 'Manrope', sans-serif;
    font-size: 1.55rem;
    font-weight: 800;
    color: var(--forest);
    margin-bottom: .5rem;
}
.about-copy {
    color: #35584a;
    line-height: 1.65;
    font-size: .98rem;
}
.mini-heading {
    color: var(--forest);
    font-weight: 800;
    font-size: 1rem;
    margin-bottom: .35rem;
}
div[data-testid="stMetric"] {
    background: linear-gradient(145deg, #ffffff, #f1faf4);
    border: 1px solid #d5ebdd;
    border-radius: 15px;
    padding: 1rem 1.05rem;
    box-shadow: 0 4px 14px rgba(9, 82, 50, .04);
}
div[data-testid="stMetricLabel"] {
    color: #426657;
    font-weight: 600;
}
div[data-testid="stMetricValue"] {
    color: var(--forest);
    font-family: 'Manrope', sans-serif;
    font-weight: 800;
}
div[data-testid="stDataFrame"] {
    border: 1px solid #d8e9df;
    border-radius: 12px;
    overflow: hidden;
}
.stButton > button, .stDownloadButton > button {
    border-radius: 10px;
    border: 1px solid #168653;
    background: linear-gradient(135deg, #0d7448, #19945a);
    color: white;
    font-weight: 700;
    padding: .55rem 1rem;
    transition: all .18s ease;
}
.stButton > button:hover, .stDownloadButton > button:hover {
    background: #075b3b;
    border-color: #075b3b;
    color: white;
    transform: translateY(-1px);
}
div[data-baseweb="select"] > div {
    border-radius: 10px;
    border-color: #cfe3d7;
    background-color: #fff;
}
div[data-testid="stSlider"] [role="slider"] {
    background-color: #168653;
}
hr {
    border-color: #dcece2;
    margin-top: 1.35rem;
    margin-bottom: 1.35rem;
}
div[data-testid="stAlert"] {
    border-radius: 12px;
}
.footer {
    text-align: center;
    color: #678476;
    font-size: .83rem;
    padding: 1rem .5rem .3rem .5rem;
}
@media (max-width: 700px) {
    .hero { padding: 1.6rem 1.25rem; border-radius: 17px; }
    .about-card { padding: 1.1rem; }
    
/* Darker metric labels for better readability */
div[data-testid="stMetricLabel"],
div[data-testid="stMetricLabel"] p {
    color: #244b3b !important;
    font-weight: 700 !important;
    opacity: 1 !important;
}
}

/* Number metric boxes */
div[data-testid="stMetric"] {
    background-color: #d9f0df !important;
    border: 1px solid #a8d5b5 !important;
    padding: 18px 20px !important;
    border-radius: 14px !important;
    box-shadow: 0 4px 12px rgba(7, 91, 59, 0.08);
}

/* Numbers inside the boxes */
div[data-testid="stMetricValue"],
div[data-testid="stMetricValue"] div {
    color: #075b3b !important;
    font-weight: 800 !important;
}

/* Labels above the numbers */
div[data-testid="stMetricLabel"],
div[data-testid="stMetricLabel"] p {
    color: #244b3b !important;
    font-weight: 700 !important;
}



/* Environmental Data metric box labels */
div[data-testid="stMetricLabel"],
div[data-testid="stMetricLabel"] p {
    color: #102f23 !important;
    font-size: 16px !important;
    font-weight: 800 !important;
    opacity: 1 !important;
    line-height: 1.4 !important;
}

/* Environmental Data numbers */
div[data-testid="stMetricValue"],
div[data-testid="stMetricValue"] div {
    color: #075b3b !important;
    font-size: 28px !important;
    font-weight: 800 !important;
}

/* Ensure metric boxes have enough space */
div[data-testid="stMetric"] {
    padding: 18px !important;
    background-color: #d9f0df !important;
    border: 1px solid #a8d5b5 !important;
    border-radius: 14px !important;
    min-height: 100px !important;
}

/* Make metric names visible */
[data-testid="stMetric"] [data-testid="stMetricLabel"] {
    color: #102f23 !important;
    background-color: transparent !important;
    opacity: 1 !important;
}

[data-testid="stMetric"] [data-testid="stMetricLabel"] p,
[data-testid="stMetric"] [data-testid="stMetricLabel"] span {
    color: #102f23 !important;
    font-size: 15px !important;
    font-weight: 800 !important;
    opacity: 1 !important;
}

/* Metric numbers */
[data-testid="stMetric"] [data-testid="stMetricValue"] {
    color: #075b3b !important;
    font-weight: 800 !important;
}

/* Metric box background */
[data-testid="stMetric"] {
    background-color: #d9f0df !important;
    border: 1px solid #a8d5b5 !important;
    border-radius: 14px !important;
    padding: 18px !important;
}

/* Improve visibility of all metric boxes */
div[data-testid="stMetric"] {
    background-color: #d9f0df !important;
    border: 1px solid #a8d5b5 !important;
    border-radius: 14px !important;
    padding: 18px !important;
}

/* Make box labels dark and readable */
div[data-testid="stMetricLabel"],
div[data-testid="stMetricLabel"] p,
div[data-testid="stMetricLabel"] span {
    color: #123c2a !important;
    font-size: 15px !important;
    font-weight: 800 !important;
    opacity: 1 !important;
}

/* Make numbers dark green */
div[data-testid="stMetricValue"],
div[data-testid="stMetricValue"] div {
    color: #075b3b !important;
    font-weight: 800 !important;
    opacity: 1 !important;
}

/* Make text below the boxes visible */
div[data-testid="stMetric"] + div,
div[data-testid="stMarkdownContainer"] p {
    color: #15382e;
}


</style>
""", unsafe_allow_html=True)

# ============================================================
# 3. HERO HEADER
# ============================================================
st.markdown("""
<div class="hero">
  <div class="hero-kicker">A greener tomorrow through data and innovation</div>
  <h1>🌱 Green India</h1>
  <div class="hero-subtitle">Quantum Computing-Based Environmental Optimization System</div>
  <p class="hero-copy">
    Explore Indian pollutant readings, investigate environmental data,
    and compare budget-constrained initiative plans using classical
    optimization and quantum computing experiments.
  </p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# 4. ABOUT THE PROJECT - FIRST SECTION
# ============================================================
st.markdown("""
<div class="about-card">
  <div class="about-label">Project overview</div>
  <div class="about-title">📘 About the Project</div>
  <div class="about-copy">
    <b>Green India</b> is an academic environmental analysis and
    optimization project exploring how classical optimization and
    quantum computing techniques can help select environmental initiatives
    within a limited budget. Environmental pollutant readings provide
    context, while a separate illustrative model demonstrates budget planning.
  </div>
</div>
""", unsafe_allow_html=True)

about_cols = st.columns(4)
with about_cols[0]:
    st.markdown("**🎯 Objectives**")
    st.markdown(
        "- Explore pollutant readings\n"
        "- Filter states, cities, pollutants\n"
        "- Download filtered data\n"
        "- Optimize initiatives by budget"
    )
with about_cols[1]:
    st.markdown("**🧩 Project Modules**")
    st.markdown(
        "- Environmental data analysis\n"
        "- Interactive dashboard\n"
        "- Classical optimization\n"
        "- QAOA result comparison"
    )
with about_cols[2]:
    st.markdown("**🛠️ Technologies**")
    st.markdown(
        "- Python and Pandas\n"
        "- Streamlit dashboard\n"
        "- Qiskit\n"
        "- QAOA experiment"
    )
with about_cols[3]:
    st.markdown("**⚠️ Important Note**")
    st.markdown(
        "Initiative costs and impact scores are illustrative assumptions, "
        "not verified environmental outcomes. Similar results do not "
        "demonstrate quantum advantage."
    )

st.divider()

# ============================================================
# ENVIRONMENTAL DATA
# ============================================================

st.markdown("---")
st.header("🌿 Environmental Data")

aqi_path = BASE_DIR / "india_aqi.csv"

if aqi_path.exists():

    # Load environmental dataset
    aqi = pd.read_csv(aqi_path)

    # Clean column names
    aqi.columns = aqi.columns.str.strip()

    # Convert average readings to numeric values
    if "avg" in aqi.columns:
        aqi["avg"] = pd.to_numeric(aqi["avg"], errors="coerce")

    # Keep a complete copy for other sections
    df = aqi.copy()

    st.success("Environmental dataset loaded successfully!")

    # --------------------------------------------------------
    # ENVIRONMENTAL METRICS
    # --------------------------------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Pollution Records",
            f"{len(aqi):,}"
        )

    with col2:
        st.metric(
            "Number of States",
            aqi["state"].nunique()
            if "state" in aqi.columns else "N/A"
        )

    with col3:
        st.metric(
            "Different Pollutant Types",
            aqi["pollutant"].nunique()
            if "pollutant" in aqi.columns else "N/A"
        )

    # ============================================================
    # 5.1 INTERACTIVE POLLUTION DATA EXPLORER
    # ============================================================

    st.markdown("---")
    st.subheader("🔎 Interactive Pollution Data Explorer")

    filtered_aqi = aqi.copy()

    # Clean the filter columns
    for column in ["state", "city", "pollutant"]:
        if column in filtered_aqi.columns:
            filtered_aqi[column] = (
                filtered_aqi[column].astype("string").str.strip()
            )

    # State filter
    if "state" in filtered_aqi.columns:
        states = sorted(filtered_aqi["state"].dropna().unique().tolist())
        selected_state = st.selectbox(
            "📍 Select State",
            ["All States"] + states,
            key="filter_state"
        )

        if selected_state != "All States":
            filtered_aqi = filtered_aqi[
                filtered_aqi["state"] == selected_state
            ]

    # City filter
    if "city" in filtered_aqi.columns:
        cities = sorted(filtered_aqi["city"].dropna().unique().tolist())
        selected_city = st.selectbox(
            "🏙️ Select City",
            ["All Cities"] + cities,
            key="filter_city"
        )

        if selected_city != "All Cities":
            filtered_aqi = filtered_aqi[
                filtered_aqi["city"] == selected_city
            ]

    # Pollutant filter
    if "pollutant" in filtered_aqi.columns:
        pollutants = sorted(
            filtered_aqi["pollutant"].dropna().unique().tolist()
        )
        selected_pollutant = st.selectbox(
            "🧪 Select Pollutant",
            ["All Pollutants"] + pollutants,
            key="filter_pollutant"
        )

        if selected_pollutant != "All Pollutants":
            filtered_aqi = filtered_aqi[
                filtered_aqi["pollutant"] == selected_pollutant
            ]

    # Convert average readings to numbers
    if "avg" in filtered_aqi.columns:
        filtered_aqi["avg"] = pd.to_numeric(
            filtered_aqi["avg"], errors="coerce"
        )

    # Display filter results
    metric1, metric2, metric3 = st.columns(3)

    metric1.metric("Matching Records", len(filtered_aqi))

    if "state" in filtered_aqi.columns:
        metric2.metric(
            "States Included",
            filtered_aqi["state"].nunique()
        )
    else:
        metric2.metric("States Included", "N/A")

    if "pollutant" in filtered_aqi.columns:
        metric3.metric(
            "Pollutant Types",
            filtered_aqi["pollutant"].nunique()
        )
    else:
        metric3.metric("Pollutant Types", "N/A")

    # Chart and data preview
    chart_col, table_col = st.columns([1, 1])

    with chart_col:
        st.markdown("### 📈 Pollution Chart")

        if {"pollutant", "avg"}.issubset(filtered_aqi.columns):
            chart_data = filtered_aqi.dropna(
                subset=["pollutant", "avg"]
            )

            if not chart_data.empty:
                chart_summary = chart_data.groupby(
                    "pollutant"
                )["avg"].mean()

                st.bar_chart(chart_summary)
            else:
                st.info(
                    "No numeric average readings are available "
                    "for the selected filters."
                )
        else:
            st.warning("The dataset needs pollutant and avg columns.")

    with table_col:
        st.markdown("### 🗂️ Data Preview")

        st.dataframe(
    filtered_aqi.head(20),
    width="stretch",
    hide_index=True
)

        st.download_button(
            "📥 Download Filtered Data",
            data=filtered_aqi.to_csv(index=False).encode("utf-8"),
            file_name="filtered_pollution_data.csv",
            mime="text/csv"
        )

    # ---------------- CONCENTRATION FILTER ----------------

    if "avg" in filtered_aqi.columns:
        valid_values = filtered_aqi["avg"].dropna()

        if not valid_values.empty:
            min_value = float(valid_values.min())
            max_value = float(valid_values.max())

            if min_value < max_value:
                selected_range = st.slider(
                    "📊 Average Pollutant Concentration",
                    min_value=min_value,
                    max_value=max_value,
                    value=(min_value, max_value),
                    key="explorer_concentration"
                )

                filtered_aqi = filtered_aqi[
                    filtered_aqi["avg"].between(
                        selected_range[0], selected_range[1]
                    )
                ]

    # ---------------- RESULTS SUMMARY ----------------

    st.markdown("### 📊 Filter Results")

    result1, result2, result3 = st.columns(3)

    with result1:
        st.metric("Matching Records", f"{len(filtered_aqi):,}")

    with result2:
        st.metric(
            "States Included",
            filtered_aqi["state"].nunique()
            if "state" in filtered_aqi.columns else "N/A"
        )

    with result3:
        st.metric(
            "Pollutant Types",
            filtered_aqi["pollutant"].nunique()
            if "pollutant" in filtered_aqi.columns else "N/A"
        )


    # ---------------- DOWNLOAD ----------------

    st.download_button(
        label="📥 Download Filtered Data (CSV)",
        data=filtered_aqi.to_csv(index=False).encode("utf-8"),
        file_name="green_india_filtered_data.csv",
        mime="text/csv",
        key="explorer_download"
    )

    # Preserve the filtered records for later sections
    df = filtered_aqi.copy()
    
# ============================================================
# 6. STATE-WISE POLLUTION COMPARISON
# ============================================================

st.divider()
st.header("🇮🇳 State-wise Pollution Comparison")

st.write(
    "Compare the average reported concentration of a selected "
    "pollutant across Indian states."
)

pollution_comparison_path = BASE_DIR / "india_aqi.csv"

if pollution_comparison_path.exists():
    pollution_comparison = pd.read_csv(pollution_comparison_path)

    pollution_comparison.columns = (
        pollution_comparison.columns.astype(str).str.strip()
    )

    required_columns = {"state", "pollutant", "avg"}

    if required_columns.issubset(pollution_comparison.columns):

        # Clean data
        for column in ["state", "pollutant"]:
            pollution_comparison[column] = (
                pollution_comparison[column]
                .astype("string")
                .str.strip()
            )

        pollution_comparison["avg"] = pd.to_numeric(
            pollution_comparison["avg"],
            errors="coerce"
        )

        pollution_comparison = pollution_comparison.dropna(
            subset=["state", "pollutant", "avg"]
        )

        if not pollution_comparison.empty:

            # Pollutant selector
            pollutant_list = sorted(
                pollution_comparison["pollutant"]
                .unique()
                .tolist()
            )

            selected_pollutant_comparison = st.selectbox(
                "Select pollutant for state comparison",
                pollutant_list,
                key="state_pollutant_comparison"
            )

            # Filter selected pollutant
            selected_pollution_data = pollution_comparison[
                pollution_comparison["pollutant"]
                == selected_pollutant_comparison
            ]

            # Calculate mean concentration for each state
            state_summary = (
                selected_pollution_data
                .groupby("state", as_index=False)
                .agg(
                    Average_Concentration=("avg", "mean"),
                    Number_of_Readings=("avg", "count")
                )
                .sort_values(
                    "Average_Concentration",
                    ascending=False
                )
            )

            if not state_summary.empty:

                # Choose how many states to display
                max_states = min(15, len(state_summary))

                states_to_display = st.slider(
                    "Number of states to display",
                    min_value=1,
                    max_value=max_states,
                    value=max_states,
                    key="comparison_state_count"
                )

                displayed_states = state_summary.head(
                    states_to_display
                ).copy()

                # Summary metrics
                metric1, metric2, metric3 = st.columns(3)

                metric1.metric(
                    "States Compared",
                    len(state_summary)
                )

                metric2.metric(
                    "Selected Pollutant",
                    selected_pollutant_comparison
                )

                metric3.metric(
                    "Total Readings",
                    int(selected_pollution_data.shape[0])
                )

                # Chart
                st.subheader("📊 Average Concentration by State")

                chart_data = displayed_states.set_index("state")[
                    ["Average_Concentration"]
                ]

                st.bar_chart(chart_data)

                st.caption(
                    "States are ranked by mean reported concentration "
                    "for the selected pollutant. This is not an overall "
                    "AQI ranking, and readings may vary by station and date."
                )

                # Table
                st.subheader("📋 State Comparison Table")

                display_table = displayed_states.rename(
                    columns={
                        "state": "State",
                        "Average_Concentration":
                            "Average Concentration",
                        "Number_of_Readings": "Number of Readings"
                    }
                )

                st.dataframe(
                    display_table.round(3),
                    use_container_width=True,
                    hide_index=True
                )

                # Download full state comparison
                st.download_button(
                    label="📥 Download State Comparison CSV",
                    data=state_summary.to_csv(
                        index=False
                    ).encode("utf-8"),
                    file_name="state_wise_pollution_comparison.csv",
                    mime="text/csv",
                    key="download_state_pollution"
                )
                st.download_button(
    label="📥 Download Filtered Pollution Data",
    data=filtered_aqi.to_csv(index=False).encode("utf-8"),
    file_name="filtered_pollution_data.csv",
    mime="text/csv",
    key="download_filtered_pollution"
)

            else:
                st.info(
                    "No valid state-wise readings are available "
                    "for this pollutant."
                )

        else:
            st.warning(
                "No valid numeric average readings were found "
                "in the environmental dataset."
            )

    else:
        st.error(
            "The dataset needs the columns 'state', 'pollutant', and 'avg'."
        )

else:
    st.warning("The file india_aqi.csv was not found.")

# ============================================================
# ENVIRONMENTAL INITIATIVES
# ============================================================

initiatives = pd.DataFrame({
    "Initiative": [
        "Tree Plantation",
        "Solar Energy",
        "Waste Management",
        "Pollution Control",
        "Water Conservation"
    ],
    "Cost": [3, 4, 2, 3, 2],
    "Estimated Impact Score": [8, 9, 5, 7, 6]
})

budget = 7
# ============================================================
# 7. CLASSICAL BUDGET OPTIMIZATION
# ============================================================
best_score = -1
best_selection = None
best_cost = 0

for selection in product([0, 1], repeat=len(initiatives)):
    cost = sum(
        selection[i] * int(initiatives.iloc[i]["Cost"])
        for i in range(len(initiatives))
    )
    score = sum(
        selection[i] * int(initiatives.iloc[i]["Estimated Impact Score"])
        for i in range(len(initiatives))
    )
    if cost <= budget and score > best_score:
        best_score = score
        best_cost = cost
        best_selection = selection

plan = initiatives[[bool(value) for value in best_selection]].copy()

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Budget Units Available",
    budget
)

col2.metric(
    "Total Cost of Selected Initiatives",
    best_cost
)

col3.metric(
    "Total Estimated Impact Points",
    best_score
)

st.subheader("✅ Recommended Classical Plan")
st.dataframe(plan, use_container_width=True)
st.write("**Budget Remaining (cost units):**", budget - best_cost)

# ============================================================
# 8. CLASSICAL VS QUANTUM COMPARISON
# ============================================================
st.divider()
st.header("⚛️ Classical vs Quantum Optimization")

comparison_path = BASE_DIR / "green_india_final_comparison.csv"

if comparison_path.exists():
    comparison = pd.read_csv(comparison_path)
    st.subheader("Saved Optimization Results")
    st.dataframe(comparison, use_container_width=True)

    required_columns = {"Method", "Estimated Impact Score"}
    if required_columns.issubset(comparison.columns) and not comparison.empty:
        comparison["Estimated Impact Score"] = pd.to_numeric(
            comparison["Estimated Impact Score"], errors="coerce"
        )
        valid_comparison = comparison.dropna(
            subset=["Estimated Impact Score"]
        )
        if not valid_comparison.empty:
            comparison_chart = valid_comparison.set_index("Method")[
                ["Estimated Impact Score"]
            ]
            st.subheader("📊 Estimated Impact Score by Method")
            st.bar_chart(comparison_chart)
        else:
            st.info("The comparison file has no numeric impact scores.")
    else:
        st.info(
            "The comparison CSV needs 'Method' and "
            "'Estimated Impact Score' columns to display the chart."
        )
else:
    st.info(
        "The QAOA comparison file is missing. Run the QAOA cells in your "
        "notebook and save green_india_final_comparison.csv beside app.py."
    )

st.caption(
    "This section displays saved results. Similar scores do not establish "
    "quantum advantage. The budget slider recalculates the classical plan "
    "and does not rerun QAOA."
)

# Download Classical vs Quantum results
comparison_file = BASE_DIR / "green_india_final_comparison.csv"

if comparison_file.exists():
    comparison_df = pd.read_csv(comparison_file)

    st.download_button(
        label="Download Classical vs Quantum Results",
        data=comparison_df.to_csv(index=False).encode("utf-8"),
        file_name="green_india_final_comparison.csv",
        mime="text/csv"
    )
else:
    st.warning(
        "Comparison CSV file not found. "
        "Please save green_india_final_comparison.csv "
        "inside the GreenIndia project folder."
    )

# ============================================================
# 9. FOOTER
# ============================================================
st.divider()
st.markdown(
    '<div class="footer">🌱 <b>Green India Academic Project</b> · '
    'Environmental readings provide context; initiative impact scores '
    'are illustrative.</div>',
    unsafe_allow_html=True
)
