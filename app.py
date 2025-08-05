import streamlit as st
import pandas as pd
import preprocessor

st.markdown("""
    <div style='display: flex; align-items: center; gap: 15px; margin-bottom: 20px;'>
        <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Olympic_rings_without_rims.svg/320px-Olympic_rings_without_rims.svg.png' width='50'>
        <h1 style='color: #002868;'>Stats of Champions</h1>
    </div>
""", unsafe_allow_html=True)

# ---------------- Custom Olympic Styling ----------------
st.set_page_config(page_title="Olympic Data Explorer", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
        color: #1C1C1C;
    }

    /* Header Text */
    .main h1, .main h2, .main h3 {
        color: #002868;
        font-weight: 700;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #F0F0F0;
        border-right: 2px solid #D0D0D0;
    }

    /* Button Styling */
    .stButton > button {
        background-color: #0081C9;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5rem 1rem;
    }

    .stButton > button:hover {
        background-color: #005B9A;
    }

    /* Tabs */
    [data-baseweb="tab"] {
        font-size: 16px;
        font-weight: 600;
        color: #002868;
    }

    /* Radio Buttons in Sidebar */
    .stRadio label {
        font-size: 16px;
        font-weight: 500;
    }

    /* Table & Charts Container */
    .stDataFrame {
        background-color: #FFFFFF;
        border-radius: 8px;
        padding: 0.5rem;
    }

    </style>
""", unsafe_allow_html=True)


# Load data
df = pd.read_csv('./olympic-history/athlete_events.csv')
region_df = pd.read_csv('./olympic-history/noc_regions.csv')

# Preprocess
df = preprocessor.preprocess(df, region_df)

# Sidebar
st.sidebar.image('./images/olympics 1.png', width=250)
st.sidebar.title("🏆 Olympics Data Insights")

user_menu = st.sidebar.radio(
    "Navigate",
    options=[
        "🏅 Medal Tally",
        "📊 Overall Analysis",
        "🌍 Country Analysis",
        "🤸‍♀️ Athlete Analysis"
    ]
)

# Page navigation logic
if user_menu == "🏅 Medal Tally":
    from my_pages.Medal_Tally import run_medal_tally
    run_medal_tally(df)

elif user_menu == "📊 Overall Analysis":
    from my_pages.Overall_Analysis import run_overall_analysis
    run_overall_analysis(df)

elif user_menu == "🌍 Country Analysis":
    from my_pages.Country_Analysis import run_country_analysis
    run_country_analysis(df)

elif user_menu == "🤸‍♀️ Athlete Analysis":
    from my_pages.Athlete_Analysis import run_athlete_analysis
    run_athlete_analysis(df)
