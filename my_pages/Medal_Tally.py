import streamlit as st
import helper

def run_medal_tally(df):
    # Page heading
    st.markdown("## 🏅 Medal Tally")

    # Filters
    col1, col2 = st.columns(2)

    years = helper.year_list(df)
    countries = helper.country_list(df)

    with col1:
        selected_year = st.selectbox("Select Year", years)

    with col2:
        selected_country = st.selectbox("Select Country", countries)

    # Fetch medal tally
    medal_df = helper.fetch_medal_tally(df, selected_year, selected_country)

    # Subheading
    st.markdown("### 🏆 Overall Medal Tally")

    # Display table
    if medal_df.empty:
        st.warning("No data available for selected filters.")
    else:
        st.dataframe(
            medal_df,
            use_container_width=True
        )
