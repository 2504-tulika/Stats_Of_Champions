import streamlit as st
import matplotlib.pyplot as plt

def run_overall_analysis(df):
    st.title("📊 Overall Olympic Analysis")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Editions", df['Edition'].nunique())
    col2.metric("Cities", df['City'].nunique())
    col3.metric("Sports", df['Sport'].nunique())
    col4.metric("Athletes", df['Name'].nunique())

    st.subheader("Events Over Time")
    events = df.groupby('Year')['Event'].nunique()

    fig, ax = plt.subplots()
    events.plot(ax=ax)
    ax.set_ylabel("No. of Events")
    st.pyplot(fig)

    st.subheader("Participating Nations Over Time")
    nations = df.groupby('Year')['Region'].nunique()

    fig, ax = plt.subplots()
    nations.plot(ax=ax, color='green')
    ax.set_ylabel("No. of Countries")
    st.pyplot(fig)
