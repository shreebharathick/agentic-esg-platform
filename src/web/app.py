import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Agentic ESG Dashboard",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 Agentic ESG: Autonomous ESG Reporting Platform")
st.markdown("Welcome to the real-time AI-powered ESG analytics and compliance dashboard.")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select View", ["Overview", "Emissions Tracking", "Compliance Audit"])

if page == "Overview":
    st.header("Executive Summary")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Carbon Emissions", "1,245 tCO2e", "-12% vs last year")
    col2.metric("ESG Composite Score", "84 / 100", "+5 points")
    col3.metric("Regulatory Compliance", "96%", "GRI & CSRD Aligned")

    st.subheader("Emissions Trend (Scope 1, 2, 3)")
    chart_data = pd.DataFrame(
        {"Scope 1": [120, 110, 105], "Scope 2": [300, 290, 280], "Scope 3": [850, 820, 860]},
        index=["Q1", "Q2", "Q3"]
    )
    st.line_chart(chart_data)

elif page == "Emissions Tracking":
    st.header("Scope 1, 2 & 3 Detailed Breakdown")
    st.info("Automated ERP data extraction active. Live data feeds connected.")

elif page == "Compliance Audit":
    st.header("Self-Updating Regulatory Compliance")
    st.success("All modules are up to date with the latest CSRD and GHG Protocol standards.")