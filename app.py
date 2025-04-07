import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import plotly.graph_objects as go
import seaborn as sns

# Set page configuration
st.set_page_config(
    page_title="Artificial Intelligence in Healthcare",
    page_icon="🏥",
    layout="wide"
)

# App title and introduction
st.title("Artificial Intelligence in Healthcare")
st.markdown("""
This dashboard presents comprehensive analytics on healthcare industry trends and
Impact of AI on trsnforming the healthcare landscape.
""")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select a Page",
    ["Overview", "Industry Trends", "AI Healthcare Market", "Impact of AI", "AI Use Cases"]
)

# Function to load data
@st.cache_data
def load_industry_data():
    # Placeholder for real data - replace with actual data loading
    # Example data structure for healthcare industry trends
    data = pd.read_csv("data/trends.csv")
    return pd.DataFrame(data)

@st.cache_data
def load_ai_impact_data():
    return pd.read_csv("data/ai_healthcare_investment.csv")


# Load the data
industry_data = load_industry_data()
ai_impact_data = load_ai_impact_data()

# Overview Page
if page == "Overview":
    st.header("Market Research Overview")
    
    # Key metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Healthcare Spending 2024", "$11T", "+7%")
    with col2:
        st.metric("Telehealth Adoption", "72%", "-6%")
    with col3:
        st.metric("AI in Healthcare Growth", "45%", "+15%")
    
    st.subheader("Project Scope")
    st.markdown("""
    This healthcare market research project analyzes:
    - **Industry Trends**: Emerging technologies, spending patterns, and market dynamics
    - **AI Healthcare Market**: Insights on growth, investment, and future forecasts of AI in healthcare
    - **Impact of AI**: AI Capabilities, Adoptation analysis
    - **AI Use Cases**: Adoption of AI in various healthcare applications
    
    Use the navigation panel on the left to explore specific areas of analysis.
    """)

    # CAGR Analysis
    st.subheader("📈 CAGR (Compound Annual Growth Rate) from 2018 to 2025")

    # Manually define CAGR values
    cagr_data = pd.DataFrame({
        "Trend": [
            "AI/ML in Healthcare",
            "Medical Robotics",
            "Blockchain in Healthcare",
            "Cybersecurity in Healthcare",
            "Health Apps (mHealth)",
            "Telemedicine",
            "Wearable Devices"
        ],
        "CAGR (%)": [50.2, 20.8, 22.7, 18.5, 38.26, 29.0, 20.0]
    })

    # Plot CAGR
    fig_cagr = px.bar(
        cagr_data,
        x="Trend",
        y="CAGR (%)",
        color="Trend",
        title="CAGR (2018–2025) by Technology Segment"
    )
    fig_cagr.update_layout(xaxis_title="Trend", yaxis_title="CAGR (%)")

    st.plotly_chart(fig_cagr, use_container_width=True)

    st.markdown("""
                - **Rapid Growth**: The AI in healthcare market is experiencing a high CAGR — estimated to reach ~60% by 2030. This reflects rapid adoption of AI technologies for diagnostics, personalized medicine, robotic surgery, and patient care.
                - **Market Value Surge**: Due to this strong CAGR, the global AI in healthcare market is projected to grow from ~$25 billion in 2023 to over $215 billion by 2030, showcasing its transformative potential in revolutionizing healthcare delivery.
                """)
    

# Industry Trends Page
elif page == "Industry Trends":
    st.title("📈 Healthcare Market Research: Industry Trends")
    st.markdown("Analyze healthcare technology trends from 2018 to 2025.")

    st.markdown("""
            Healthcare Industry Technological Trends:
            - **AI/ML**
            - **Medical Robotics**
            - **Blockchain**
            - **Cybersecurity**
            - **Health apps**
            - **Telemedicine and virtual care**
            - **Wearable devices**
                """)

    # Load data
    years = [int(col) for col in industry_data.columns if col != "Trend"]

    # Line Chart
    st.subheader("Trend Growth Over Time")
    df_melted = industry_data.melt(id_vars="Trend", var_name="Year", value_name="Market Size (USD Billion)")
    df_melted["Year"] = df_melted["Year"].astype(int)
    fig = px.line(df_melted, x="Year", y="Market Size (USD Billion)", color="Trend", markers=True)
    st.plotly_chart(fig, use_container_width=True)

    # Select Year for Comparison
    year = st.selectbox("Select a Year to Compare Trends", years)
    st.subheader(f"Market Size Comparison for {year}")
    year_data = industry_data[["Trend", str(year)]].rename(columns={str(year): "Market Size (USD Billion)"})
    fig2 = px.bar(year_data, x="Trend", y="Market Size (USD Billion)", color="Trend")
    st.plotly_chart(fig2, use_container_width=True)

    

elif page == "AI Healthcare Market":
    st.subheader("AI Investment in Medical & Healthcare (2017-2023)")

    st.markdown("""
    This dashboard shows the annual private investment in artificial intelligence within the medical and healthcare sector.
    Data includes companies that received more than $1.5 million in investment.
    All values are in **constant 2021 US dollars**, adjusted for inflation.
    """)

    # Line chart
    fig = px.line(
        ai_impact_data,
        x="Year",
        y=["World", "United States", "European Union & UK", "China"],
        markers=True,
        title="Annual Private AI Investment in Healthcare by Region",
        labels={"value": "Investment (USD Billion)", "variable": "Region"},
    )
    fig.update_layout(legend_title_text='Region')
    st.plotly_chart(fig)

    # Data table toggle
    if st.checkbox("Show raw data"):
        st.subheader("Raw Investment Data")
        st.dataframe(ai_impact_data)

    # Investment summary
    st.subheader("Investment Highlights")
    st.markdown(f"- **Peak global investment:** ${ai_impact_data['World'].max():.1f} billion in {ai_impact_data.loc[ai_impact_data['World'].idxmax(), 'Year']}")
    st.markdown(f"- **Peak US investment:** ${ai_impact_data['United States'].max():.1f} billion in {ai_impact_data.loc[ai_impact_data['United States'].idxmax(), 'Year']}")
    st.markdown(f"- **Peak EU+UK investment:** ${ai_impact_data['European Union & UK'].max():.1f} billion")
    st.markdown(f"- **Peak China investment:** ${ai_impact_data['China'].max():.1f} billion")
    st.subheader("AI Capabilities in Medical Specialties")

        # Add a new section for AI Healthcare Market Forecast
    st.subheader("AI Healthcare Market Revenue Forecast (2023 vs. 2030)")

    # Market data
    market_data = {
        "Country": [
            "USA", "Canada", "Germany", "France", "Italy", "Spain", "Russia", "UK",
            "Japan", "China", "India", "Australia", "South Korea", "Singapore",
            "Mexico", "Argentina", "Brazil", "South Africa", "Saudi Arabia", "UAE"
        ],
        "Revenue 2023 (USD Billion)": [
            11.8194, 1.1338, 0.6871, 0.7142, 0.0965, 0.1629, 0.2015, 1.3262,
            0.9173, 1.5855, 0.7588, 0.1976, 0.3528, 0.0781, 0.0562, 0.0355,
            0.0841, 0.0153, 0.0228, 0.0172
        ],
        "Forecast 2030 (USD Billion)": [
            102.1537, 10.7673, 6.6181, 7.0779, 0.7393, 1.5143, 1.8475, 12.4938,
            10.8909, 18.8836, 8.728, 2.1573, 3.8091, 0.8813, 0.5938, 0.3048,
            0.7894, 0.1163, 0.1913, 0.1379
        ],
        "Growth Rate (2024-2030)": [
            "36.1%", "37.9%", "38.2%", "38.8%", "33.8%", "37.5%", "37.2%", "37.8%",
            "42.4%", "42.5%", "41.8%", "40.7%", "40.5%", "41.4%", "40.0%", "36.0%",
            "37.7%", "33.6%", "35.5%", "34.6%"
        ]
    }

    market_df = pd.DataFrame(market_data)

    # Bar chart for 2023 vs 2030 revenue
    fig3 = px.bar(
        market_df,
        x="Country",
        y=["Revenue 2023 (USD Billion)", "Forecast 2030 (USD Billion)"],
        barmode="group",
        title="AI Healthcare Revenue Forecast by Country",
        labels={"value": "USD Billion", "variable": "Year"},
    )
    st.plotly_chart(fig3)

    # Optional: Show raw forecast data
    if st.checkbox("Show Forecast Table"):
        st.dataframe(market_df)

    # Highlight key growth markets
    st.subheader("Top Growth Markets (2024–2030)")
    top_growth = market_df.copy()
    top_growth["Growth %"] = top_growth["Growth Rate (2024-2030)"].str.rstrip('%').astype(float)
    top_growth = top_growth.sort_values("Growth %", ascending=False).head(5)

    st.markdown("Here are the top 5 countries by projected growth rate:")
    st.table(top_growth[["Country", "Growth Rate (2024-2030)"]])


    

    # Data
    years = list(range(2016, 2031))
    market_size = [
        100, 300, 700, 1500, 3000, 6000, 12000, 25000,
        45000, 70000, 100000, 130000, 165000, 190000, 215000
    ]

    shared_2025 = market_size[9]
    # Current (add 2025 to make smooth connection)
    current_years = years[:9] + [2025]
    current_market = market_size[:9] + [shared_2025]

    # Projected (start from 2025 too)
    projected_years = [2025] + years[10:]
    projected_market = [shared_2025] + market_size[10:]

    # Plot
    fig = go.Figure()

    # Current
    fig.add_trace(go.Scatter(
        x=current_years,
        y=current_market,
        fill='tozeroy',
        mode='lines+markers',
        name='Current',
        line=dict(color='green')
    ))

    # Projected
    fig.add_trace(go.Scatter(
        x=projected_years,
        y=projected_market,
        fill='tozeroy',
        mode='lines+markers',
        name='Projected',
        line=dict(color='orange', dash='dash')
    ))

    fig.update_layout(
        title="Global AI Healthcare Market Size (2016–2030)",
        xaxis=dict(title="Year", tickmode='linear', dtick=1),
        yaxis_title="Market Size (USD Millions)",
        legend_title="Data Type"
    )

    # Display in Streamlit
    st.subheader("Global AI Healthcare Market Growth")
    st.plotly_chart(fig, use_container_width=True, key="ai_market_split_chart")




elif page == "Impact of AI":

    stats_data = {
        "Task": [
            "Provide documentation",
            "Provide emphatic care to patients",
            "Formulate personalized medication and/or treatment plans",
            "Evaluate referral type",
            "Establish prognoses",
            "Detect criminal behavior",
            "Detect self-harmful behavior",
            "Reach diagnoses",
            "Perform physical examination",
            "Interview patients",
            "Average for each task"
        ],
        "Psychiatry": [49, 9, 30, 33, 67, 35, 44, 72, 16, 51, 41],
        "Pathology": [73, 13, 60, 73, 87, 40, 53, 73, 33, 80, 59],
        "Radiology": [35, 6, 65, 53, 71, 35, 35, 65, 29, 29, 42],
        "Surgical Specialities": [38, 8, 46, 51, 64, 36, 23, 64, 31, 59, 42],
        "Average": [49, 9, 50, 53, 72, 37, 39, 69, 27, 54, 46]
    }

    stats_df = pd.DataFrame(stats_data)
    fig2 = px.imshow(
        stats_df.set_index("Task").T,
        text_auto=True,
        labels=dict(color="% Capability"),
        aspect="auto",
        title="AI Capability (%) Across Medical Tasks and Specialties"
    )
    st.plotly_chart(fig2)
    # Optional: Show raw task data
    if st.checkbox("Show AI Task Data"):
        st.dataframe(stats_df)
    
    # Summary of AI capability data
    st.subheader("Key Insights from AI Task Capabilities")
    st.markdown("""
    - **Pathology** leads in AI capability across almost all medical tasks, with the highest average score (59%).
    - **Radiology** and **Surgical Specialties** have similar average scores (42%), while **Psychiatry** shows lower capability in tasks involving physical interaction.
    - Highest capability across all specialties is in **establishing prognoses (72%)** and **reaching diagnoses (69%)**.
    - Tasks requiring human empathy or interaction, like **providing emphatic care**, show the lowest AI capability (average 9%).
    - Overall, AI shows strongest potential in analytical and documentation tasks across specialties.
    """)

    # Data
    data = {
        "Use Case": [
            "Clinical decision support tools",
            "Predictive analytics and risk stratification",
            "Clinical workflow optimization and automation",
            "Treatment and therapy recommendations for providers",
            "Diagnosis and treatment recommendations",
            "Clinical documentation and dictation"
        ],
        "Share of Respondents (%)": [29, 25, 23, 19, 16, 15]
    }

    df = pd.DataFrame(data)

    # Sort values for better visual order
    df = df.sort_values(by="Share of Respondents (%)", ascending=True)

    # Plot
    fig = px.bar(
        df,
        x="Share of Respondents (%)",
        y="Use Case",
        orientation="h",
        title="AI Use Cases in Healthcare (by Share of Respondents)",
        color_discrete_sequence=["#1f77b4"]  # Solid blue
    )

    # Aesthetic improvements
    fig.update_layout(
        xaxis_title="Percentage of Respondents",
        yaxis_title="AI Use Case",
        plot_bgcolor="white",
        font=dict(size=14),
        title_font=dict(size=20),
        margin=dict(l=100, r=40, t=60, b=40)
    )

    # Display
    st.title("AI Use Case Adoption in Healthcare")
    st.plotly_chart(fig, use_container_width=True)


elif page == "AI Use Cases":
    import streamlit as st
    from PIL import Image

    st.subheader("GPT-2 Medi: AI-Powered Healthcare Assistant")
    st.markdown("""
    GPT-2 Medi is an AI-powered healthcare assistant designed for doctors to get information on any disease instantly.
    """)

    st.subheader("How it Works")
    # Load image
    image = Image.open("Images\\Gpt2-Medi.png")
    image2 = Image.open("Images\\Output.png")

    # Display image
    col1, col2, col3 = st.columns([1, 2, 1])  # 2 is the center column
    with col2:
        st.image(image, use_container_width=True, caption="Centered Image")
    
    st.subheader("Sample Output")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(image2, use_container_width=True, caption="Centered Image")
    