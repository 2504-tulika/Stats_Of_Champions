import streamlit as st
import matplotlib.pyplot as plt

def run_overall_analysis(df):
    st.markdown("## 📊 Overall Olympic Analysis")

    # -------------------- KPI METRICS --------------------
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("🏟️ Editions", df['Edition'].nunique())
    col2.metric("🌍 Cities", df['City'].nunique())
    col3.metric("🏅 Sports", df['Sport'].nunique())
    col4.metric("🤸 Athletes", df['Name'].nunique())

    st.markdown("### 📈 Olympic Growth Over Time")

    col_left, col_right = st.columns(2)

    # -------------------- EVENTS OVER TIME --------------------
    with col_left:
        st.subheader("🎯 Events Expansion")

        events = df.groupby('Year')['Event'].nunique()

        fig, ax = plt.subplots(figsize=(7, 4))
        events.plot(ax=ax)

        ax.set_title("Number of Olympic Events Over the Years")
        ax.set_xlabel("Year")
        ax.set_ylabel("Events")
        ax.grid(alpha=0.3)

        st.pyplot(fig)

        st.caption(
            "Insight: The number of Olympic events has steadily increased, reflecting the inclusion of new sports and categories."
        )

    # -------------------- NATIONS OVER TIME --------------------
    with col_right:
        st.subheader("🌐 Global Participation")

        nations = df.groupby('Year')['Region'].nunique()

        fig, ax = plt.subplots(figsize=(7, 4))
        nations.plot(ax=ax)

        ax.set_title("Participating Nations Over Time")
        ax.set_xlabel("Year")
        ax.set_ylabel("Countries")
        ax.grid(alpha=0.3)

        st.pyplot(fig)

        st.caption(
            "Insight: Growing country participation highlights the increasing global reach of the Olympic Games."
        )

    

    