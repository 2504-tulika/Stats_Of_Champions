import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def run_athlete_analysis(df):
    st.markdown("## 🤸 Athlete Analysis")
    st.caption(
        "Explore athlete participation, physical attributes, and performance trends across sports."
    )

    # ------------------ FILTERS ------------------
    col1, col2 = st.columns(2)

    with col1:
        sport = st.selectbox(
            "Select Sport",
            sorted(df['Sport'].dropna().unique())
        )

    sport_df = df[df['Sport'] == sport]

    with col2:
        athlete = st.selectbox(
            "Select Athlete",
            sorted(sport_df['Name'].dropna().unique())
        )

    athlete_df = sport_df[sport_df['Name'] == athlete]

    st.markdown("---")

    # ------------------ SPORT LEVEL INSIGHTS ------------------
    st.markdown(f"### 🏅 {sport} – Sport Overview")

    k1, k2, k3 = st.columns(3)
    k1.metric("Athletes", sport_df['Name'].nunique())
    k2.metric("Countries", sport_df['Region'].nunique())
    k3.metric("Events", sport_df['Event'].nunique())

    col_left, col_right = st.columns(2)

    # Age distribution
    with col_left:
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.histplot(sport_df['Age'].dropna(), bins=20, kde=True, ax=ax)
        ax.set_title("Age Distribution")
        ax.set_xlabel("Age")
        ax.grid(alpha=0.3)
        st.pyplot(fig)

    # Gender distribution
    with col_right:
        gender_counts = sport_df['Sex'].value_counts()

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.pie(
            gender_counts,
            labels=gender_counts.index,
            autopct='%1.1f%%',
            startangle=90
        )
        ax.set_title("Gender Distribution")
        st.pyplot(fig)

    st.markdown("---")

    # ------------------ ATHLETE LEVEL INSIGHTS ------------------
    st.markdown(f"### 🧑‍🤝‍🧑 Athlete Profile – {athlete}")

    a1, a2, a3 = st.columns(3)
    a1.metric("Olympic Appearances", athlete_df['Year'].nunique())
    a2.metric("Events Played", athlete_df['Event'].nunique())
    a3.metric("Medals Won", athlete_df[athlete_df['Medal'] != 'No Medal'].shape[0])

    # Career timeline
    st.subheader("📆 Career Timeline")

    career = athlete_df.groupby('Year').agg({
    'Event': 'nunique',
    'Medal': lambda x: (x != 'No Medal').sum()
    }).reset_index()

    fig, ax = plt.subplots(figsize=(9, 4))

# Base line: participation
    ax.plot(
        career['Year'],
    career['Event'],
    marker='o',
    linewidth=2,
    label="Events Participated"
    )

# Highlight medal-winning years
    medal_years = career[career['Medal'] > 0]
    ax.scatter(
    medal_years['Year'],
    medal_years['Event'],
    s=120,
    color='gold',
    edgecolor='black',
    label="Medal-winning Year",
    zorder=3
)

# Fill area for career span
    ax.fill_between(
    career['Year'],
    career['Event'],
    alpha=0.2
)

    ax.set_xlabel("Olympic Year")
    ax.set_ylabel("Events")
    ax.set_title("Athlete Career Progression")
    ax.legend()
    ax.grid(alpha=0.3)

    st.pyplot(fig)

    st.caption(
    "Gold markers indicate years in which the athlete won at least one medal."
)


    # Physical profile
    st.subheader("⚖️ Physical Profile Comparison")

    fig, ax = plt.subplots(figsize=(7, 6))

# Sport-level density
    sns.kdeplot(
    x=sport_df['Weight'],
    y=sport_df['Height'],
    cmap="Blues",
    fill=True,
    thresh=0.05,
    alpha=0.4,
    ax=ax
)

# Sport average
    ax.scatter(
    sport_df['Weight'].mean(),
    sport_df['Height'].mean(),
    color='black',
    s=80,
    marker='X',
    label="Sport Average"
)

# Athlete highlight
    ax.scatter(
    athlete_df['Weight'],
    athlete_df['Height'],
    color='red',
    s=150,
    edgecolor='black',
    label=athlete
)

    ax.set_xlabel("Weight (kg)")
    ax.set_ylabel("Height (cm)")
    ax.set_title("Athlete vs Sport Physical Distribution")
    ax.legend()
    ax.grid(alpha=0.3)

    st.pyplot(fig)

    st.caption(
    "The highlighted point shows how the athlete’s physical attributes compare to others in the same sport."
)

