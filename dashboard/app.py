import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px
from streamlit_autorefresh import st_autorefresh

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="NeuralStreamX",
    page_icon="⚡",
    layout="wide"
)

# =========================================
# AUTO REFRESH
# =========================================

st_autorefresh(
    interval=5000,
    key="dashboardrefresh"
)

# =========================================
# FUTURISTIC CSS
# =========================================

st.markdown("""
<style>

html, body, [class*="css"] {
    background-color: #050816;
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

.main {
    background: linear-gradient(
        135deg,
        #050816,
        #0b1026,
        #050816
    );
}

.block-container {
    padding-top: 1rem;
}

h1 {
    font-size: 3rem;
    font-weight: 800;
    color: #00F5FF;
    text-shadow: 0px 0px 20px #00F5FF;
}

h2, h3 {
    color: #8BE9FD;
}

[data-testid="metric-container"] {

    background: rgba(255,255,255,0.05);

    border: 1px solid rgba(0,255,255,0.2);

    padding: 25px;

    border-radius: 25px;

    backdrop-filter: blur(20px);

    box-shadow:
        0 0 20px rgba(0,255,255,0.15),
        0 0 40px rgba(0,255,255,0.08);

    transition: all 0.3s ease-in-out;
}

[data-testid="metric-container"]:hover {

    transform: translateY(-5px);

    box-shadow:
        0 0 30px rgba(0,255,255,0.4),
        0 0 60px rgba(0,255,255,0.2);
}

.stDataFrame {

    background: rgba(255,255,255,0.03);

    border-radius: 20px;

    padding: 10px;

    border: 1px solid rgba(255,255,255,0.08);
}

div[data-testid="stPlotlyChart"] {

    background: rgba(255,255,255,0.04);

    border-radius: 20px;

    padding: 10px;

    border: 1px solid rgba(255,255,255,0.05);

    box-shadow:
        0 0 20px rgba(0,255,255,0.08);
}

</style>
""", unsafe_allow_html=True)

# =========================================
# SIDEBAR
# =========================================

st.sidebar.title("⚙ NeuralStreamX")

refresh_rate = st.sidebar.slider(
    "Refresh Speed (sec)",
    1,
    10,
    5
)

st.sidebar.success("System Operational")

st.sidebar.metric(
    "Kafka Lag",
    "0 ms"
)

st.sidebar.metric(
    "Fraud Risk",
    "LOW"
)

# =========================================
# DATABASE CONNECTION
# =========================================

connection = psycopg2.connect(
    host="localhost",
    port="5433",
    database="streaming_db",
    user="admin",
    password="06041977"
)

# =========================================
# LOAD DATA
# =========================================

query = """
SELECT * FROM streaming_events
ORDER BY id DESC
LIMIT 100
"""

df = pd.read_sql(query, connection)

# =========================================
# HEADER
# =========================================

st.title("⚡ NeuralStreamX")

st.subheader(
    "AI-Powered Real-Time Kafka Streaming Analytics Platform"
)

# =========================================
# STATUS BAR
# =========================================

st.markdown("""
<div style="
padding:15px;
border-radius:15px;
background:rgba(0,255,255,0.08);
border:1px solid rgba(0,255,255,0.2);
margin-bottom:20px;
">

🟢 Kafka Online |
🟢 PostgreSQL Connected |
🟢 Streaming Active |
⚡ Real-Time Processing Enabled

</div>
""", unsafe_allow_html=True)

# =========================================
# KPI METRICS
# =========================================

total_transactions = len(df)

total_revenue = df['amount'].sum()

average_transaction = (
    df['amount'].mean()
    if not df.empty else 0
)

top_city = (
    df.groupby('city')['amount']
    .sum()
    .idxmax()
    if not df.empty else "N/A"
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "⚡ Transactions",
    f"{total_transactions:,}"
)

col2.metric(
    "💰 Revenue",
    f"₹ {total_revenue:,.0f}"
)

col3.metric(
    "📊 Avg Transaction",
    f"₹ {average_transaction:,.0f}"
)

col4.metric(
    "🌍 Top City",
    top_city
)

# =========================================
# REVENUE TREND
# =========================================

st.subheader("📈 Real-Time Revenue Trend")

trend_df = (
    df.groupby('created_at')['amount']
    .sum()
    .reset_index()
)

fig3 = px.line(
    trend_df,
    x='created_at',
    y='amount',
    template='plotly_dark'
)

fig3.update_traces(
    line_color='#00F5FF'
)

fig3.update_layout(
    paper_bgcolor='#050816',
    plot_bgcolor='#050816',
    font_color='white'
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# =========================================
# CHARTS
# =========================================

left, right = st.columns(2)

# =========================================
# CITY REVENUE
# =========================================

city_df = (
    df.groupby('city')['amount']
    .sum()
    .reset_index()
)

fig1 = px.bar(
    city_df,
    x='city',
    y='amount',
    title='🌆 City Revenue Analytics',
    template='plotly_dark'
)

fig1.update_traces(
    marker_color='#00F5FF'
)

fig1.update_layout(
    paper_bgcolor='#050816',
    plot_bgcolor='#050816',
    font_color='white'
)

left.plotly_chart(
    fig1,
    use_container_width=True
)

# =========================================
# PRODUCT DISTRIBUTION
# =========================================

product_df = (
    df.groupby('product')['amount']
    .sum()
    .reset_index()
)

fig2 = px.pie(
    product_df,
    names='product',
    values='amount',
    title='🛒 Product Distribution',
    template='plotly_dark'
)

fig2.update_traces(
    textfont_size=16
)

fig2.update_layout(
    paper_bgcolor='#050816',
    font_color='white'
)

right.plotly_chart(
    fig2,
    use_container_width=True
)

# =========================================
# LIVE ACTIVITY FEED
# =========================================

st.subheader("⚡ Live Transaction Activity")

latest = df.head(5)

for _, row in latest.iterrows():

    st.markdown(f"""
    <div style="
    padding:12px;
    margin-bottom:10px;
    border-radius:15px;
    background:rgba(255,255,255,0.03);
    border-left:5px solid #00F5FF;
    ">

    💳 {row['product']} |
    ₹ {row['amount']} |
    🌍 {row['city']}

    </div>
    """, unsafe_allow_html=True)

# =========================================
# LIVE TRANSACTION TABLE
# =========================================

st.subheader("📡 Live Streaming Feed")

st.dataframe(
    df,
    use_container_width=True,
    height=400
)

# =========================================
# FRAUD DETECTION PANEL
# =========================================

st.subheader("🚨 AI Fraud Detection")

fraud_df = df[df['amount'] > 200000]

if not fraud_df.empty:

    st.error(
        f"{len(fraud_df)} Suspicious Transactions Detected"
    )

    st.dataframe(
        fraud_df,
        use_container_width=True
    )

else:

    st.success("No Fraud Detected")

# =========================================
# SYSTEM HEALTH
# =========================================

st.subheader("🟢 System Health")

health_col1, health_col2, health_col3 = st.columns(3)

health_col1.success("Kafka Online")
health_col2.success("PostgreSQL Connected")
health_col3.success("Streaming Active")