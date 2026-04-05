import streamlit as st
import pandas as pd
import os

df = pd.read_csv("major_project_dataset.csv")
matches = pd.read_csv("all_top_matches.xls")
feedback = pd.read_csv("feedback.xls")

if not os.path.exists("live_feedback.csv"):
    pd.DataFrame(columns=["user_id", "action"]).to_csv(
        "live_feedback.csv",
        index=False
    )

st.set_page_config(
    page_title="Intelligent Hybrid Recommendation System",
    layout="wide"
)

st.title("Intelligent Hybrid Recommendation System")
st.write(
    "A profile-based matching platform using NLP, MBTI, "
    "and adaptive machine learning."
)

user_id = st.selectbox("Select Your User ID", df["user_id"])

if st.button("Show Recommendations"):
    filtered_matches = matches[matches["user_id"] == user_id]

    st.subheader(f"Top Matches for {user_id}")

    if filtered_matches.empty:
        st.warning("No recommendations found for this user.")
    else:
        st.dataframe(filtered_matches, use_container_width=True)

        st.subheader("Compatibility Scores")

        for _, row in filtered_matches.iterrows():
            st.metric(
                label=row["Recommended User"],
                value=f"{row['Compatibility Score']}%"
            )

            profile = df[df["name"] == row["Recommended User"]]

            if not profile.empty:
                profile = profile.iloc[0]

                st.write(f"Name: {profile['name']}")
                st.write(f"Career Goal: {profile['career goals']}")
                st.write(f"MBTI: {profile['mbti']}")
                st.write(f"Location: {profile['location']}")
                st.write("---")

st.subheader("Recommendation Feedback")

user_feedback = st.radio(
    "Do you like these recommendations?",
    ["Accept", "Reject"]
)

if st.button("Submit Feedback"):
    action_value = 1 if user_feedback == "Accept" else 0

    new_feedback = pd.DataFrame({
        "user_id": [user_id],
        "action": [action_value]
    })

    new_feedback.to_csv(
        "live_feedback.csv",
        mode="a",
        header=False,
        index=False
    )

    st.success("Feedback saved successfully.")

st.subheader("Recommendation Analytics")

filtered_matches = matches[matches["user_id"] == user_id]

if not filtered_matches.empty:
    chart_data = filtered_matches.set_index("Recommended User")[
        "Compatibility Score"
    ]
    st.bar_chart(chart_data)