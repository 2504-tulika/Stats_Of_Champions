import streamlit as st
import helper
import matplotlib.pyplot as plt

def run_country_analysis(df):
    st.markdown("## 🌍 Country-wise Analysis")

    # Country selector
    country = st.selectbox("Select Country", helper.country_list(df))
    country_df = df[df['Region'] == country]

    medals = country_df[country_df['Medal'] != 'No Medal']

    st.markdown("---")

    # Layout: Trend | Top Athletes
    col1, col2 = st.columns([2, 1])

    # 📈 Medal Trend
    with col1:
        st.markdown(f"### 📈 {country} – Medal Trend Over Years")

        trend = medals.groupby('Year')['Medal'].count()

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(trend.index, trend.values, marker='o')
        ax.set_xlabel("Year")
        ax.set_ylabel("Number of Medals")
        ax.grid(alpha=0.3)

        st.pyplot(fig)

    # 🏅 Top Athletes
    with col2:
        st.markdown("### 🏅 Top Athletes")

        top_athletes = (
            medals['Name']
            .value_counts()
            .head(10)
            .reset_index()
        )
        top_athletes.columns = ["Athlete Name", "Medals Won"]

        st.dataframe(
            top_athletes,
            use_container_width=True
        )
