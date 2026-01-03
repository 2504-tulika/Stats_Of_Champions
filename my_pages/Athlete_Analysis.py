import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def run_athlete_analysis(df):
    st.markdown("## 🤸 Athlete Analysis")

    # -------- Sport Selector --------
    sport = st.selectbox(
        "Select Sport",
        sorted(df['Sport'].dropna().unique())
    )

    sport_df = df[df['Sport'] == sport]

    # -------- Athlete Selector (filtered by sport) --------
    athlete = st.selectbox(
        "Select Athlete",
        sorted(sport_df['Name'].dropna().unique())
    )

    athlete_df = sport_df[sport_df['Name'] == athlete]

    st.markdown("---")

    # Tabs
    tab1, tab2 = st.tabs(["📊 Age Distribution", "⚖️ Height vs Weight"])

    # ---------------- Age Distribution ----------------
    with tab1:
        st.markdown(f"### 📊 Age Distribution – {athlete}")

        fig, ax = plt.subplots(figsize=(8, 4))
        sns.histplot(
            athlete_df['Age'].dropna(),
            kde=True,
            bins=10,
            ax=ax
        )

        ax.set_xlabel("Age")
        ax.set_ylabel("Appearances")
        ax.grid(alpha=0.3)

        st.pyplot(fig)

    # ---------------- Height vs Weight ----------------
    with tab2:
        st.markdown(f"### ⚖️ Height vs Weight – {athlete}")

        fig, ax = plt.subplots(figsize=(8, 5))
        sns.scatterplot(
            x=athlete_df['Weight'],
            y=athlete_df['Height'],
            hue=athlete_df['Sex'],
            s=80,
            ax=ax
        )

        ax.set_xlabel("Weight (kg)")
        ax.set_ylabel("Height (cm)")
        ax.grid(alpha=0.3)

        st.pyplot(fig)
