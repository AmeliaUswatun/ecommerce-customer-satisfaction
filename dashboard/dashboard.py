# ============================================================
# E-COMMERCE CUSTOMER SATISFACTION DASHBOARD
# Executive Analytics | Light Mode
# ============================================================

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

import pandas as pd
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import seaborn as sns
import textwrap


# ============================================================
# 1. PAGE CONFIGURATION & CUSTOM STYLE
# ============================================================

st.set_page_config(
    page_title="E-Commerce Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)



st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

:root {
    --pink: #E7A8C9;
    --lilac: #D7A8E4;
    --lavender: #B8A8E7;
    --plum: #68465F;
    --muted: #98758E;
}

.stApp {
    background:
        radial-gradient(ellipse at 5% 5%, #F1D8EA 0%, transparent 42%),
        radial-gradient(ellipse at 95% 15%, #E7DDF5 0%, transparent 38%),
        linear-gradient(135deg, #FBF5FA, #F4ECF8 55%, #F9F0F5);
    color: var(--plum);
    font-family: 'DM Sans', sans-serif;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

h1, h2, h3, h4 {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    color: var(--plum);
}

.hero-header {
    text-align: center;
    padding: 22px 18px 8px;
    margin: 0 auto 8px;
    animation: heroEnter 1s ease-out both;
}

.main-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: clamp(27px, 3vw, 40px);
    line-height: 1.2;
    font-weight: 800;
    color: #68465F;
    letter-spacing: -1.25px;
    text-align: center;
    text-shadow: 0 3px 18px rgba(183, 110, 145, 0.14);
}

.subtitle {
    color: #98758E;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 1.7px;
    text-align: center;
    margin-top: 9px;
}

.period-banner {
    position: relative;
    overflow: hidden;
    max-width: 760px;
    margin: 15px auto 27px;
    padding: 17px 24px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.9);
    border-radius: 17px;
    background: linear-gradient(
        110deg,
        rgba(252, 230, 241, 0.94),
        rgba(239, 222, 247, 0.94),
        rgba(250, 231, 242, 0.94)
    );
    background-size: 220% 220%;
    box-shadow: 0 9px 26px rgba(145, 95, 137, 0.10);
    animation: periodGlow 9s ease-in-out infinite, heroEnter 1.15s ease-out both;
}

.period-label {
    color: #A17F91;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.8px;
    margin-bottom: 7px;
}

.period-value {
    color: #68465F;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: clamp(15px, 1.7vw, 19px);
    font-weight: 800;
    letter-spacing: 0.1px;
}

@keyframes heroEnter {
    from { opacity: 0; transform: translateY(16px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes periodGlow {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

@media (max-width: 640px) {
    .hero-header { padding: 16px 8px 5px; }
    .main-title { letter-spacing: -0.7px; }
    .subtitle { font-size: 9px; letter-spacing: 1px; }
    .period-banner { margin: 12px auto 20px; padding: 14px 10px; }
}

/* Floating glass sidebar */
section[data-testid="stSidebar"] {
    background: transparent !important;
    /* Do not set min-width here: Streamlit must be able to collapse the sidebar
       and reclaim its grid column for the main dashboard. */
}

section[data-testid="stSidebar"] > div:first-child {
    background: linear-gradient(
        155deg,
        rgba(255,255,255,0.58),
        rgba(239,218,239,0.48),
        rgba(221,207,241,0.54)
    ) !important;
    backdrop-filter: blur(22px);
    -webkit-backdrop-filter: blur(22px);
    border: 1px solid rgba(255,255,255,0.78);
    border-radius: 0 26px 26px 0;
    box-shadow: 8px 0 30px rgba(119,79,119,0.10);
}

section[data-testid="stSidebar"] * {
    color: #68465F;
}

.sidebar-nav-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #68465F;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.5px;
    margin: 8px 0 12px 4px;
}

.sidebar-icon-nav {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 12px;
    padding: 8px 0 16px;
}

.sidebar-icon-nav a {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 48px;
    height: 48px;
    border-radius: 16px;
    text-decoration: none !important;
    font-size: 21px;
    color: #79566F !important;
    background: rgba(255,255,255,0.42);
    border: 1px solid rgba(255,255,255,0.62);
    box-shadow: 0 5px 14px rgba(129,87,128,0.07);
    transition: all 180ms ease;
}

.sidebar-icon-nav a:hover {
    color: #FFFFFF !important;
    background: linear-gradient(135deg, #DFA5C9, #BDA5E3);
    transform: translateX(4px);
    box-shadow: 0 8px 18px rgba(157,104,157,0.20);
}

.sidebar-icon-nav a::after {
    content: attr(data-tooltip);
    position: absolute;
    left: 60px;
    top: 50%;
    transform: translate(5px, -50%);
    white-space: nowrap;
    padding: 8px 12px;
    border-radius: 9px;
    color: #FFFFFF;
    background: rgba(104,70,95,0.94);
    font-family: 'DM Sans', sans-serif;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.2px;
    opacity: 0;
    visibility: hidden;
    pointer-events: none;
    transition: all 160ms ease;
    z-index: 9999;
    box-shadow: 0 5px 16px rgba(70,45,70,0.18);
}

.sidebar-icon-nav a:hover::after {
    opacity: 1;
    visibility: visible;
    transform: translate(0, -50%);
}

/* Highlighted business-question section headers */
.question-heading {
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 17px 20px;
    margin: 22px 0 8px;
    border-radius: 17px;
    background: linear-gradient(110deg, rgba(232,177,207,0.88), rgba(204,177,229,0.88));
    border: 1px solid rgba(255,255,255,0.88);
    box-shadow: 0 8px 22px rgba(145,95,137,0.12);
}

.question-number {
    display: flex;
    align-items: center;
    justify-content: center;
    flex: 0 0 43px;
    width: 43px;
    height: 43px;
    border-radius: 14px;
    color: #FFFFFF;
    background: rgba(255,255,255,0.25);
    border: 1px solid rgba(255,255,255,0.55);
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 15px;
    font-weight: 800;
}

.question-title {
    color: #593D50;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 17px;
    line-height: 1.35;
    font-weight: 800;
}

.question-description {
    color: #76566D;
    font-family: 'DM Sans', sans-serif;
    font-size: 11px;
    line-height: 1.5;
    margin-top: 3px;
}

.section-anchor {
    display: block;
    position: relative;
    top: -12px;
    visibility: hidden;
}

html {
    scroll-behavior: smooth;
}

/* Glass KPI cards */
div[data-testid="stMetric"] {
    background: linear-gradient(
        135deg,
        rgba(255,255,255,0.72),
        rgba(255,255,255,0.32)
    );
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border: 1px solid rgba(255,255,255,0.8);
    border-radius: 17px;
    padding: 18px;
    box-shadow: 0 8px 25px rgba(145,95,137,0.09);
}

div[data-testid="stMetricLabel"] {
    color: #98758E;
}

div[data-testid="stMetricValue"] {
    color: #68465F;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-weight: 800;
}

/* Glass panels */
[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255,255,255,0.48);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255,255,255,0.78);
    border-radius: 18px;
    box-shadow: 0 8px 24px rgba(145,95,137,0.06);
}

/* Insight panels */
.insight-box {
    background: linear-gradient(
        120deg,
        rgba(231,168,201,0.28),
        rgba(215,168,228,0.25)
    );
    border: 1px solid rgba(255,255,255,0.8);
    border-left: 4px solid #D58BBE;
    border-radius: 13px;
    padding: 15px;
    color: #68465F;
    line-height: 1.7;
    margin-bottom: 12px;
}

/* Tables */
[data-testid="stDataFrame"] {
    background: rgba(255,255,255,0.65);
    border: 1px solid rgba(255,255,255,0.9);
    border-radius: 13px;
}

/* Expander */
[data-testid="stExpander"] {
    background: rgba(255,255,255,0.45);
    border: 1px solid rgba(255,255,255,0.8);
    border-radius: 14px;
}

/* Footer */
.footer {
    color: #98758E;
    text-align: center;
    font-size: 11px;
    padding: 25px;
}

/* Full-width content: use all available space when sidebar is collapsed */
[data-testid="stMainBlockContainer"],
.main .block-container,
section.main > div.block-container {
    width: 100% !important;
    max-width: none !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
    padding-left: clamp(1rem, 2vw, 2rem) !important;
    padding-right: clamp(1rem, 2vw, 2rem) !important;
    box-sizing: border-box !important;
}


/* Responsive chart rendering */
[data-testid="stImage"],
[data-testid="stImage"] img,
[data-testid="stPyplot"] img {
    max-width: 100% !important;
    height: auto !important;
}

@media (max-width: 900px) {
    [data-testid="stMainBlockContainer"] {
        padding-left: 0.85rem !important;
        padding-right: 0.85rem !important;
    }
}

/* Sidebar brand */
.sidebar-brand {
    padding: 12px 10px 20px;
    margin-bottom: 12px;
    border-bottom: 1px solid rgba(255,255,255,0.55);
    font-family: 'Plus Jakarta Sans', sans-serif;
    line-height: 1.12;
}
.sidebar-brand .brand-line {
    color: #68465F !important;
    font-size: 21px;
    font-weight: 800;
    letter-spacing: -0.7px;
}
.sidebar-brand .brand-accent {
    color: #A94F83 !important;
    text-shadow: 0 1px 0 rgba(255,255,255,0.55);
}
.sidebar-brand .brand-caption {
    color: #79566F !important;
    font-family: 'DM Sans', sans-serif;
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 1.1px;
    margin-top: 8px;
}

/* Expanded sidebar: icon and label aligned in one row */
.sidebar-nav-label {
    color: #79566F !important;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.4px;
    padding: 7px 10px 10px;
}
.sidebar-menu {
    display: flex;
    flex-direction: column;
    gap: 7px;
    padding: 0 4px 14px;
}
.sidebar-menu a {
    display: flex;
    align-items: center;
    gap: 13px;
    min-height: 43px;
    padding: 7px 11px;
    border-radius: 13px;
    color: #68465F !important;
    text-decoration: none !important;
    background: rgba(255,255,255,0.20);
    border: 1px solid rgba(255,255,255,0.30);
    transition: all 160ms ease;
}
.sidebar-menu a:hover {
    color: #68465F !important;
    background: rgba(255,255,255,0.62);
    transform: translateX(3px);
    box-shadow: 0 5px 14px rgba(129,87,128,0.10);
}
.sidebar-menu .menu-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    flex: 0 0 27px;
    width: 27px;
    height: 27px;
    border-radius: 9px;
    background: rgba(255,255,255,0.60);
    color: #925D83 !important;
    font-size: 17px;
    font-weight: 700;
}
.sidebar-menu .menu-text {
    color: #68465F !important;
    font-size: 11px;
    font-weight: 600;
    line-height: 1.3;
}

/* Collapsed-sidebar floating quick navigation */
.floating-quick-nav {
    display: none;
    position: fixed;
    left: 13px;
    top: 50%;
    transform: translateY(-50%);
    z-index: 999999;
    flex-direction: column;
    gap: 11px;
    padding: 12px 9px;
    border-radius: 20px;
    background: rgba(255,255,255,0.46);
    border: 1px solid rgba(255,255,255,0.78);
    box-shadow: 0 8px 28px rgba(111,75,111,0.13);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
}
.floating-quick-nav a {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 39px;
    height: 39px;
    border-radius: 13px;
    color: #79566F !important;
    background: rgba(255,255,255,0.66);
    border: 1px solid rgba(255,255,255,0.8);
    text-decoration: none !important;
    font-size: 19px;
    font-weight: 700;
    transition: all 160ms ease;
}
.floating-quick-nav a:hover {
    color: #FFFFFF !important;
    background: linear-gradient(135deg, #DFA5C9, #BDA5E3);
    transform: scale(1.07);
}
.floating-quick-nav a::after {
    content: attr(title);
    position: absolute;
    left: 49px;
    top: 50%;
    transform: translate(5px, -50%);
    white-space: nowrap;
    padding: 8px 11px;
    border-radius: 9px;
    color: #FFFFFF;
    background: rgba(104,70,95,0.95);
    font-family: 'DM Sans', sans-serif;
    font-size: 11px;
    font-weight: 600;
    opacity: 0;
    visibility: hidden;
    pointer-events: none;
    transition: all 150ms ease;
}
.floating-quick-nav a:hover::after {
    opacity: 1;
    visibility: visible;
    transform: translate(0, -50%);
}

/* Streamlit renders this control when the native sidebar is collapsed. */
.floating-quick-nav {
    display: none;
}
body:has([data-testid="stSidebarCollapsedControl"]) .floating-quick-nav {
    display: flex;
}
/* Keep the floating rail above charts and app content. */
.floating-quick-nav {
    position: fixed !important;
    left: 14px !important;
    top: 50% !important;
    transform: translateY(-50%) !important;
    z-index: 1000000 !important;
}

/* Small screens: keep content readable and nav compact */
@media (max-width: 700px) {
    [data-testid="stMainBlockContainer"],
    .main .block-container,
    section.main > div.block-container {
        padding-left: 0.8rem !important;
        padding-right: 0.8rem !important;
    }
    .floating-quick-nav {
        left: 5px;
        padding: 8px 6px;
    }
    .floating-quick-nav a {
        width: 34px;
        height: 34px;
    }
}



/* ============================================================
   SOFT LIFT HOVER INTERACTIONS
   ============================================================ */

div[data-testid="stMetric"],
[data-testid="stVerticalBlockBorderWrapper"],
[data-testid="stDataFrame"],
[data-testid="stExpander"],
[data-testid="stPlotlyChart"],
[data-testid="stPyplot"],
[data-testid="stImage"] {
    transition:
        transform 220ms cubic-bezier(0.2, 0.75, 0.25, 1),
        box-shadow 220ms ease,
        border-color 220ms ease,
        filter 220ms ease;
    transform-origin: center center;
}

[data-testid="stVerticalBlockBorderWrapper"]:hover,
[data-testid="stDataFrame"]:hover,
[data-testid="stExpander"]:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 32px rgba(145, 95, 137, 0.15);
    border-color: rgba(213, 139, 190, 0.58);
    z-index: 2;
}

[data-testid="stPlotlyChart"]:hover,
[data-testid="stPyplot"]:hover,
[data-testid="stImage"]:hover {
    transform: translateY(-3px);
    filter: drop-shadow(0 9px 13px rgba(145, 95, 137, 0.13));
}

iframe[title="streamlit.components.v1.html"] {
    transition: transform 220ms ease, filter 220ms ease;
    transform-origin: center center;
}

iframe[title="streamlit.components.v1.html"]:hover {
    transform: translateY(-6px) scale(1.015);
    filter: drop-shadow(0 12px 15px rgba(145, 95, 137, 0.20));
}

.question-heading {
    transition: transform 220ms ease, box-shadow 220ms ease, filter 220ms ease;
    transform-origin: center center;
}

.question-heading:hover {
    transform: translateY(-4px);
    box-shadow: 0 14px 28px rgba(145, 95, 137, 0.19);
    filter: saturate(1.06);
}

.insight-box {
    transition: transform 200ms ease, box-shadow 200ms ease;
}

.insight-box:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 22px rgba(145, 95, 137, 0.13);
}

.sidebar-menu a,
.sidebar-icon-nav a {
    transition: transform 180ms ease, box-shadow 180ms ease, background 180ms ease;
}

.sidebar-menu a:hover,
.sidebar-icon-nav a:hover {
    transform: translateY(-3px) scale(1.025);
    box-shadow: 0 10px 20px rgba(129, 87, 128, 0.18);
}

.period-banner {
    transition: transform 220ms ease, box-shadow 220ms ease;
}

.period-banner:hover {
    transform: translateY(-3px);
    box-shadow: 0 14px 30px rgba(145, 95, 137, 0.16);
}

@media (prefers-reduced-motion: reduce) {
    *,
    *::before,
    *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        scroll-behavior: auto !important;
        transition-duration: 0.01ms !important;
    }
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# 2. DATA LOADING
# ============================================================



@st.cache_data
def load_data():

    orders_df = pd.read_csv(DATA_DIR / "orders_dataset.csv")
    reviews = pd.read_csv(DATA_DIR / "order_reviews_dataset.csv")
    items = pd.read_csv(DATA_DIR / "order_items_dataset.csv")
    products = pd.read_csv(DATA_DIR / "products_dataset.csv")
    translation = pd.read_csv(
        DATA_DIR / "product_category_name_translation.csv"
    )

    # Convert date columns
    order_date_columns = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]

    review_date_columns = [
        "review_creation_date",
        "review_answer_timestamp"
    ]

    for column in order_date_columns:
        orders_df[column] = pd.to_datetime(
            orders_df[column], errors="coerce"
        )

    for column in review_date_columns:
        reviews[column] = pd.to_datetime(
            reviews[column], errors="coerce"
        )

    # Aggregate reviews at order level
    review_agg = (
        reviews
        .groupby("order_id")
        .agg(
            avg_review_score=("review_score", "mean"),
            total_reviews=("review_score", "count")
        )
        .reset_index()
    )

    # Prepare delivery analysis
    q1 = orders_df.merge(
        review_agg,
        on="order_id",
        how="inner"
    )

    q1 = q1[
        (q1["order_status"] == "delivered") &
        (q1["order_delivered_customer_date"].notna()) &
        (q1["order_estimated_delivery_date"].notna())
    ].copy()

    q1["delay_days"] = (
        q1["order_delivered_customer_date"] -
        q1["order_estimated_delivery_date"]
    ).dt.total_seconds() / 86400

    q1["delivery_status"] = np.where(
        q1["delay_days"] <= 0,
        "On Time",
        "Late"
    )

    # Prepare category analysis
    q2_orders = orders_df.merge(
        review_agg,
        on="order_id",
        how="inner"
    )

    q2_orders = q2_orders[
        (q2_orders["order_purchase_timestamp"].notna())
    ].copy()

    q2_orders["low_satisfaction"] = (
        q2_orders["avg_review_score"] <= 2
    )

    q2 = (
        q2_orders[["order_id", "low_satisfaction"]]
        .merge(items[["order_id", "product_id"]], on="order_id", how="inner")
        .merge(products[["product_id", "product_category_name"]],
               on="product_id", how="left")
        .merge(translation, on="product_category_name", how="left")
    )

    q2 = q2.dropna(subset=["product_category_name"]).copy()

    q2["category_name"] = (
    q2["product_category_name_english"]
    .fillna(q2["product_category_name"])
    .str.replace("_", " ", regex=False)
    .str.title()
)

    # One order can be associated with multiple categories.
    # Count each order only once within each category.
    q2 = q2.drop_duplicates(
        subset=["order_id", "category_name"]
    )

    return orders_df, reviews, items, products, translation, q1, q2


try:
    (
        orders_df,
        reviews_df,
        items_df,
        products_df,
        translation_df,
        q1_df,
        q2_df
    ) = load_data()

except FileNotFoundError as error:
    st.error(f"Dataset tidak ditemukan: {error}")
    st.info(
        "Pastikan lima file CSV berada di dalam folder "
        "'data' pada direktori project."
    )
    st.stop()


# ============================================================
# 3. SIDEBAR & DATE FILTER
# ============================================================


st.sidebar.markdown(
    """
    <div class="sidebar-brand">
        <div class="brand-line">E-Commerce</div>
        <div class="brand-line brand-accent">Intelligence</div>
        <div class="brand-caption">CUSTOMER ANALYTICS</div>
    </div>

    <div class="sidebar-nav-label">QUICK NAVIGATION</div>

    <nav class="sidebar-menu">
        <a href="#executive-overview" title="Executive Overview">
            <span class="menu-icon">⌂</span>
            <span class="menu-text">Executive Overview</span>
        </a>
        <a href="#delivery-performance" title="Q1 · Delivery Performance">
            <span class="menu-icon">↗</span>
            <span class="menu-text">Q1 · Delivery Performance</span>
        </a>
        <a href="#category-satisfaction" title="Q2 · Product Category Satisfaction">
            <span class="menu-icon">▦</span>
            <span class="menu-text">Q2 · Product Category Satisfaction</span>
        </a>
        <a href="#category-priority" title="Category Evaluation Priority">
            <span class="menu-icon">◉</span>
            <span class="menu-text">Category Evaluation Priority</span>
        </a>
        <a href="#data-methodology" title="Data Methodology">
            <span class="menu-icon">ⓘ</span>
            <span class="menu-text">Data Methodology</span>
        </a>
    </nav>
    """,
    unsafe_allow_html=True
)

# Floating navigation is shown only when the native sidebar is collapsed.
st.markdown(
    """
    <nav class="floating-quick-nav" aria-label="Quick navigation">
        <a href="#executive-overview" title="Executive Overview" aria-label="Executive Overview">⌂</a>
        <a href="#delivery-performance" title="Q1 · Delivery Performance" aria-label="Q1 Delivery Performance">↗</a>
        <a href="#category-satisfaction" title="Q2 · Product Category Satisfaction" aria-label="Q2 Product Category Satisfaction">▦</a>
        <a href="#category-priority" title="Category Evaluation Priority" aria-label="Category Evaluation Priority">◉</a>
        <a href="#data-methodology" title="Data Methodology" aria-label="Data Methodology">ⓘ</a>
    </nav>
    """,
    unsafe_allow_html=True
)

st.sidebar.divider()

st.sidebar.markdown("### Filter Periode")

min_date = orders_df["order_purchase_timestamp"].min().date()
max_date = orders_df["order_purchase_timestamp"].max().date()

selected_dates = st.sidebar.date_input(
    "Purchase Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if not isinstance(selected_dates, (tuple, list)) or len(selected_dates) != 2:
    st.warning("Silakan pilih tanggal mulai dan tanggal akhir.")
    st.stop()

start_date, end_date = selected_dates

if start_date > end_date:
    st.error("Tanggal mulai tidak boleh melebihi tanggal akhir.")
    st.stop()

st.sidebar.divider()

st.sidebar.markdown("### Analysis Information")
st.sidebar.caption(
    "Dataset: E-Commerce Public Dataset"
)
st.sidebar.caption(
    "Focus: Customer Satisfaction"
)
st.sidebar.caption(
    "Target User: Management"
)
st.sidebar.caption(
    "Period: September 2016 – October 2018"
)

st.sidebar.divider()

st.sidebar.caption(
    "Review score 1–2 dikategorikan sebagai tingkat "
    "kepuasan rendah berdasarkan rata-rata skor per pesanan."
)


# ============================================================
# 4. FILTER DATA
# ============================================================

start_timestamp = pd.Timestamp(start_date)
end_timestamp = (
    pd.Timestamp(end_date) + pd.Timedelta(days=1)
)

filtered_orders = orders_df[
    (orders_df["order_purchase_timestamp"] >= start_timestamp) &
    (orders_df["order_purchase_timestamp"] < end_timestamp)
].copy()

filtered_reviews = reviews_df[
    reviews_df["order_id"].isin(filtered_orders["order_id"])
].copy()

filtered_review_agg = (
    filtered_reviews
    .groupby("order_id")
    .agg(
        avg_review_score=("review_score", "mean"),
        total_reviews=("review_score", "count")
    )
    .reset_index()
)

filtered_q1 = q1_df[
    (q1_df["order_purchase_timestamp"] >= start_timestamp) &
    (q1_df["order_purchase_timestamp"] < end_timestamp)
].copy()

filtered_q2_orders = filtered_orders.merge(
    filtered_review_agg,
    on="order_id",
    how="inner"
)

filtered_q2_orders["low_satisfaction"] = (
    filtered_q2_orders["avg_review_score"] <= 2
)

filtered_q2 = (
    filtered_q2_orders[["order_id", "low_satisfaction"]]
    .merge(items_df[["order_id", "product_id"]], on="order_id", how="inner")
    .merge(products_df[["product_id", "product_category_name"]],
           on="product_id", how="left")
    .merge(translation_df, on="product_category_name", how="left")
)

filtered_q2 = filtered_q2.dropna(
    subset=["product_category_name"]
).copy()

filtered_q2["category_name"] = (
    filtered_q2["product_category_name_english"]
    .fillna(filtered_q2["product_category_name"])
    .str.replace("_", " ", regex=False)
    .str.title()
)

filtered_q2 = filtered_q2.drop_duplicates(
    subset=["order_id", "category_name"]
)


# ============================================================
# 5. EXECUTIVE OVERVIEW
# ============================================================

st.markdown('<span id="executive-overview" class="section-anchor"></span>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="hero-header">
        <div class="main-title">E-Commerce Customer Satisfaction</div>
        <div class="subtitle">
            EXECUTIVE ANALYTICS | DELIVERY PERFORMANCE &amp; PRODUCT CATEGORY
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Animated active analysis period
st.markdown(
    f"""
    <div class="period-banner">
        <div class="period-label">ACTIVE ANALYSIS PERIOD</div>
        <div class="period-value">
            {start_date.strftime('%d %B %Y')}
            &nbsp;—&nbsp;
            {end_date.strftime('%d %B %Y')}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


total_orders = len(filtered_orders)
total_reviews = len(filtered_reviews)

avg_score = filtered_review_agg["avg_review_score"].mean()

on_time_orders = len(
    filtered_q1[filtered_q1["delivery_status"] == "On Time"]
)

late_orders = len(
    filtered_q1[filtered_q1["delivery_status"] == "Late"]
)

eligible_delivery_orders = len(filtered_q1)

on_time_rate = (
    on_time_orders / eligible_delivery_orders * 100
    if eligible_delivery_orders > 0 else 0
)

negative_orders = (
    filtered_q2_orders["low_satisfaction"].sum()
)

negative_rate = (
    negative_orders / len(filtered_q2_orders) * 100
    if len(filtered_q2_orders) > 0 else 0
)

st.markdown("### Executive Overview")
st.caption(
    f"Business performance from {start_date:%d %b %Y} "
    f"to {end_date:%d %b %Y}"
)



# ============================================================
# ============================================================
# GRADIENT KPI CARDS
# ============================================================

kpi_cards = [
    {
        "title": "TOTAL ORDERS",
        "value": f"{total_orders:,}",
        "description": "Total transactions",
        "icon": "🛍️",
        "color1": "#E9A9C8",
        "color2": "#C99BE0"
    },
    {
        "title": "AVERAGE REVIEW",
        "value": f"{avg_score:.2f} / 5" if pd.notna(avg_score) else "N/A",
        "description": "Customer satisfaction",
        "icon": "★",
        "color1": "#EBA5BD",
        "color2": "#D68DBD"
    },
    {
        "title": "ON-TIME DELIVERY",
        "value": f"{on_time_rate:.2f}%",
        "description": "Delivery punctuality",
        "icon": "🚚",
        "color1": "#D5A4DF",
        "color2": "#B6A5E5"
    },
    {
        "title": "LOW SATISFACTION",
        "value": f"{negative_orders:,}",
        "description": f"{negative_rate:.2f}% of reviewed orders",
        "icon": "⚠️",
        "color1": "#E6A0C4",
        "color2": "#C49DDB"
    }
]

kpi_columns = st.columns(4)

for col, card in zip(kpi_columns, kpi_cards):
    with col:
        card_html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
    * {{
        box-sizing: border-box;
    }}

    html, body {{
        margin: 0;
        padding: 0;
        background: transparent;
        font-family: 'DM Sans', Arial, sans-serif;
    }}

    .kpi-card {{
        width: 100%;
        height: 138px;
        transition: transform 220ms ease, box-shadow 220ms ease;
        transform-origin: center center;
        padding: 17px;
        border-radius: 17px;
        background: linear-gradient(
            135deg,
            {card['color1']},
            {card['color2']}
        );
        border: 1px solid rgba(255,255,255,0.7);
        box-shadow: 0 8px 22px rgba(145,95,137,0.12);
        overflow: hidden;
    }}

    .kpi-card:hover {{
        transform: translateY(-6px) scale(1.015);
        box-shadow: 0 15px 28px rgba(145,95,137,0.22);
    }}

    .kpi-header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: white;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 0.4px;
    }}

    .kpi-icon {{
        font-size: 19px;
    }}

    .kpi-value {{
        margin-top: 20px;
        color: white;
        font-family: 'Plus Jakarta Sans', Arial, sans-serif;
        font-size: 24px;
        font-weight: 800;
        white-space: nowrap;
    }}

    .kpi-description {{
        margin-top: 5px;
        color: white;
        opacity: 0.92;
        font-size: 10px;
    }}
</style>
</head>
<body>
    <div class="kpi-card">
        <div class="kpi-header">
            <span>{card['title']}</span>
            <span class="kpi-icon">{card['icon']}</span>
        </div>
        <div class="kpi-value">{card['value']}</div>
        <div class="kpi-description">{card['description']}</div>
    </div>
</body>
</html>
"""
        components.html(
            card_html,
            height=150,
            scrolling=False
        )


# 6. DELIVERY PERFORMANCE ANALYSIS
# Matplotlib charts use use_container_width=True so they scale with their
# Streamlit columns and available width after the sidebar is collapsed.
# ============================================================

st.markdown(
    """
    <span id="delivery-performance" class="section-anchor"></span>
    <div class="question-heading">
        <div class="question-number">Q1</div>
        <div>
            <div class="question-title">Delivery Performance</div>
            <div class="question-description">
                Evaluating the relationship between delivery punctuality and customer satisfaction.
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

if not filtered_q1.empty:

    delivery_summary = (
        filtered_q1
        .groupby("delivery_status")
        .agg(
            total_orders=("order_id", "count"),
            avg_review_score=("avg_review_score", "mean")
        )
        .reindex(["On Time", "Late"])
        .reset_index()
    )

    delivery_summary["avg_review_score"] = (
        delivery_summary["avg_review_score"].round(2)
    )

    left, right = st.columns([1.5, 1])

    with left:
        st.markdown("#### Average Review by Delivery Status")

        fig, ax = plt.subplots(figsize=(8, 4.5))

        sns.barplot(
            data=delivery_summary,
            x="delivery_status",
            y="avg_review_score",
            hue="delivery_status",
            legend=False,
            ax=ax
        )

        ax.set_ylim(0, 5)
        ax.set_xlabel("")
        ax.set_ylabel("Average Review Score")
        ax.set_title("Delivery Punctuality vs Customer Satisfaction")

        for container in ax.containers:
            ax.bar_label(container, fmt="%.2f", padding=4)

        sns.despine()
        fig.tight_layout()

        st.pyplot(fig, use_container_width=True)
        plt.close(fig)

    with right:
        st.markdown("#### Delivery Summary")

        st.dataframe(
            delivery_summary.rename(columns={
                "delivery_status": "Delivery Status",
                "total_orders": "Total Orders",
                "avg_review_score": "Average Score"
            }),
            use_container_width=True,
            hide_index=True
        )

        if len(delivery_summary) == 2:
            on_time_score = delivery_summary.loc[
                delivery_summary["delivery_status"] == "On Time",
                "avg_review_score"
            ].iloc[0]

            late_score = delivery_summary.loc[
                delivery_summary["delivery_status"] == "Late",
                "avg_review_score"
            ].iloc[0]

            score_gap = on_time_score - late_score

            st.markdown(
                f"""
                <div class="insight-box">
                <b>Key Insight</b><br>
                Pesanan tepat waktu memiliki rata-rata review
                <b>{on_time_score:.2f}</b>, sedangkan pesanan terlambat
                memperoleh skor <b>{late_score:.2f}</b>.
                Terdapat selisih sebesar <b>{score_gap:.2f} poin</b>.
                </div>
                """,
                unsafe_allow_html=True
            )

    # Delivery delay categories
    st.markdown("#### Customer Satisfaction by Delay Duration")

    delay_conditions = [
        filtered_q1["delay_days"] <= 0,
        (filtered_q1["delay_days"] > 0) &
        (filtered_q1["delay_days"] <= 3),
        (filtered_q1["delay_days"] > 3) &
        (filtered_q1["delay_days"] <= 7),
        filtered_q1["delay_days"] > 7
    ]

    delay_labels = [
        "On Time / Early",
        "Late 1–3 Days",
        "Late 4–7 Days",
        "Late >7 Days"
    ]

    filtered_q1["delay_category"] = np.select(
        delay_conditions,
        delay_labels,
        default="Unknown"
    )

    delay_summary = (
        filtered_q1
        .groupby("delay_category")
        .agg(
            total_orders=("order_id", "count"),
            avg_review_score=("avg_review_score", "mean")
        )
        .reindex(delay_labels)
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(10, 4.5))

    sns.barplot(
        data=delay_summary,
        x="delay_category",
        y="avg_review_score",
        hue="delay_category",
        legend=False,
        ax=ax
    )

    ax.set_ylim(0, 5)
    ax.set_xlabel("")
    ax.set_ylabel("Average Review Score")
    ax.set_title("Customer Satisfaction by Delivery Delay")

    for container in ax.containers:
        ax.bar_label(container, fmt="%.2f", padding=3)

    sns.despine()
    fig.tight_layout()

    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

    st.dataframe(
        delay_summary.rename(columns={
            "delay_category": "Delay Category",
            "total_orders": "Total Orders",
            "avg_review_score": "Average Review Score"
        }).round(2),
        use_container_width=True,
        hide_index=True
    )

else:
    st.info(
        "Tidak ada pesanan yang memenuhi kriteria analisis "
        "pengiriman pada periode ini."
    )

st.divider()


# ============================================================
# 7. PRODUCT CATEGORY SATISFACTION
# ============================================================

st.markdown(
    """
    <span id="category-satisfaction" class="section-anchor"></span>
    <div class="question-heading">
        <div class="question-number">Q2</div>
        <div>
            <div class="question-title">Product Category Satisfaction</div>
            <div class="question-description">
                Identifying product categories associated with the highest proportion of low-satisfaction orders.
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

if not filtered_q2.empty:

    category_summary = (
        filtered_q2
        .groupby("category_name")
        .agg(
            total_orders=("order_id", "nunique"),
            negative_orders=("low_satisfaction", "sum")
        )
        .reset_index()
    )

    category_summary["negative_rate"] = (
        category_summary["negative_orders"] /
        category_summary["total_orders"] * 100
    )

    # Minimum 30 orders for a more stable comparison
    category_filtered = category_summary[
        category_summary["total_orders"] >= 30
    ].copy()

    top_categories = (
        category_filtered
        .sort_values("negative_rate", ascending=False)
        .head(10)
    )

    
    # Top 10 Categories by Negative Order Rate
    st.markdown("#### Top 10 Categories by Negative Order Rate")

    fig, ax = plt.subplots(figsize=(11, 5.5))

    sns.barplot(
        data=top_categories,
        x="negative_rate",
        y="category_name",
        order=top_categories["category_name"],
        hue="category_name",
        legend=False,
        ax=ax
    )

    ax.set_xlabel("Negative Order Rate (%)")
    ax.set_ylabel("")
    ax.set_title(
        "Categories with Lowest Customer Satisfaction",
        fontweight="bold",
        pad=12
    )

    for container in ax.containers:
        ax.bar_label(
            container,
            fmt="%.2f%%",
            padding=4
        )

    sns.despine()
    fig.tight_layout()

    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

    # Category Performance Table
    st.markdown("#### Category Performance")
    st.caption("Detailed performance of the top 10 categories.")

    category_table = (
        category_filtered
        .sort_values("negative_rate", ascending=False)
        .head(10)
        .rename(columns={
            "category_name": "Product Category",
            "total_orders": "Total Orders",
            "negative_orders": "Negative Orders",
            "negative_rate": "Negative Rate (%)"
        })
        .round(2)
    )

    st.dataframe(
        category_table,
        use_container_width=True,
        hide_index=True,
        height=390,
        column_config={
            "Product Category": st.column_config.TextColumn(
                "Product Category",
                width="medium"
            ),
            "Total Orders": st.column_config.NumberColumn(
                "Total Orders",
                format="%d"
            ),
            "Negative Orders": st.column_config.NumberColumn(
                "Negative Orders",
                format="%d"
            ),
            "Negative Rate (%)": st.column_config.NumberColumn(
                "Negative Rate",
                format="%.2f%%"
            )
        }
    )

    
    # Category priority based on negative volume
    st.markdown('<span id="category-priority" class="section-anchor"></span>', unsafe_allow_html=True)
    st.markdown("#### Category Evaluation Priority")

    priority_categories = (
        category_filtered
        .sort_values("negative_orders", ascending=False)
        .head(10)
        .copy()
    )

    # Calculate average reference lines
    avg_orders = category_filtered["total_orders"].mean()
    avg_negative_rate = category_filtered["negative_rate"].mean()

    fig, ax = plt.subplots(figsize=(11, 6))

    # Bubble scatter plot
    bubble_sizes = (
        priority_categories["negative_orders"] /
        priority_categories["negative_orders"].max() * 900
    )

    ax.scatter(
        priority_categories["total_orders"],
        priority_categories["negative_rate"],
        s=bubble_sizes,
        alpha=0.75,
        color="#D78EAE",
        edgecolors="#B76E91",
        linewidths=1.2
    )

    # Reference lines
    ax.axvline(
        avg_orders,
        color="#EAB6CC",
        linestyle="--",
        linewidth=1.2,
        alpha=0.9,
        label="Average Order Volume"
    )

    ax.axhline(
        avg_negative_rate,
        color="#B76E91",
        linestyle="--",
        linewidth=1.2,
        alpha=0.9,
        label="Average Negative Rate"
    )

    # Category labels
    for _, row in priority_categories.iterrows():
        ax.annotate(
            row["category_name"],
            (
                row["total_orders"],
                row["negative_rate"]
            ),
            fontsize=8,
            xytext=(7, 7),
            textcoords="offset points",
            bbox=dict(
                boxstyle="round,pad=0.25",
                fc="white",
                ec="none",
                alpha=0.8
            )
        )

    ax.set_xlabel("Total Orders")
    ax.set_ylabel("Negative Order Rate (%)")
    ax.set_title(
        "Category Priority: Order Volume vs Negative Rate",
        fontweight="bold",
        pad=15
    )

    ax.legend(
        loc="best",
        fontsize=8,
        frameon=False
    )

    ax.grid(alpha=0.2)
    sns.despine()

    fig.tight_layout()
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)


# ============================================================
# 8. DATA NOTES & FOOTER
# ============================================================

st.markdown('<span id="data-methodology" class="section-anchor"></span>', unsafe_allow_html=True)

with st.expander("Data Methodology & Interpretation"):

    st.markdown("""
    **Delivery Performance**
    - Analisis hanya mencakup pesanan berstatus delivered yang memiliki
      tanggal pengiriman aktual dan estimasi.
    - Pengiriman tepat waktu ditentukan ketika tanggal aktual tidak
      melewati tanggal estimasi.
    - Review pada beberapa baris dalam satu pesanan diagregasi
      menggunakan rata-rata review score.

    **Product Category Satisfaction**
    - Tingkat kepuasan rendah ditentukan berdasarkan rata-rata
      review score per pesanan <= 2.
    - Review merupakan ulasan pada tingkat pesanan, bukan
      penilaian spesifik setiap produk.
    - Satu pesanan dapat terhubung dengan beberapa kategori produk.
    - Setiap kombinasi pesanan dan kategori dihitung satu kali.
    - Kategori dengan kurang dari 30 pesanan tidak ditampilkan
      dalam peringkat Top 10.

    **Interpretation**
    Hasil analisis menunjukkan hubungan atau asosiasi, bukan
    hubungan sebab-akibat.
    """)

st.markdown(
    """
    <div class="footer">
    E-Commerce Customer Satisfaction Dashboard |
    Data Analysis Project |
    E-Commerce Public Dataset
    </div>
    """,
    unsafe_allow_html=True
)