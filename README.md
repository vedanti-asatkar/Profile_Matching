# Intelligent Hybrid Recommendation System

An AI-powered professional networking and collaboration matching system that combines semantic profile understanding, MBTI compatibility logic, and weighted scoring to recommend high-potential connections.

## GitHub Repository Description

Intelligent Hybrid Recommendation System for professional networking and collaboration matching using NLP-based semantic similarity, MBTI compatibility, and weighted Compatibility Score ranking.

## Overview

This project is a Streamlit-based AI/ML application designed to match users with relevant professional collaborators based on profile similarity and compatibility signals. The system is built for major project demonstration, portfolio presentation, and beginner-friendly understanding.

It keeps the recommendation workflow practical and explainable:

- semantic similarity captures closeness between profile descriptions
- MBTI compatibility contributes a personality-based alignment signal
- weighted scoring combines these signals into a final Compatibility Score
- top matches are presented for each `user_id`
- feedback is stored for lightweight interaction tracking

## Problem Statement

Finding suitable professional collaborators or networking connections can be difficult when user profiles contain a mix of structured and unstructured information. This project addresses that challenge by combining NLP-based understanding with compatibility logic to generate relevant recommendations in a transparent way.

## Key Features

- Streamlit interface with a clean product-demo layout
- selected user profile summary
- best match highlight card
- personalized top matches table
- analytics chart for Compatibility Score comparison
- sidebar-based user selection and feedback capture
- CSV-based feedback storage for simple deployment
- beginner-readable Python code suitable for viva explanation

## Tech Stack

- Python
- Streamlit
- Pandas
- Altair
- Sentence Transformers
- Scikit-learn
- CSV-based data storage

## Architecture

```text
User Profile Dataset
        |
        v
Text Preprocessing + Profile Representation
        |
        v
Sentence Transformer Embeddings
        |
        v
Cosine Similarity Computation
        |
        +-------------------+
        |                   |
        v                   v
 MBTI Compatibility    Weighted Scoring Logic
        |                   |
        +---------+---------+
                  |
                  v
        Final Compatibility Score
                  |
                  v
      Top Match Ranking per user_id
                  |
                  v
      Streamlit Dashboard + Feedback Log
```

## Methodology

The recommendation system follows a hybrid methodology:

1. user profiles are collected from the dataset
2. textual profile fields are transformed into semantic representations
3. cosine similarity is used to measure closeness between users
4. MBTI compatibility logic adds a personality compatibility component
5. both signals are merged using weighted scoring
6. the final Compatibility Score is used to rank top recommendations
7. recommendations are shown in the Streamlit dashboard for each selected user

## NLP Layer

The NLP layer is responsible for understanding the meaning of user profiles beyond keyword matching.

- profile text such as professional summary and about me is converted into embeddings
- Sentence Transformer models capture contextual similarity
- cosine similarity identifies semantically related profiles
- this helps the system recommend users with aligned interests, skills, and goals

## Compatibility Score Formula

The project keeps the recommendation logic hybrid and explainable.

```text
Compatibility Score = (w1 × Semantic Similarity) + (w2 × MBTI Compatibility)
```

Where:

- `Semantic Similarity` is obtained from sentence embeddings and cosine similarity
- `MBTI Compatibility` is computed from the predefined personality compatibility logic
- `w1` and `w2` are configurable weights used in the project

Note: the UI enhancement in this version does not change the core recommendation logic.

## Project Files

```text
Profile_Matching/
|-- app.py
|-- major_project_dataset.csv
|-- all_top_matches.xls
|-- live_feedback.csv
|-- requirements.txt
|-- README.md
```

## Suggested Better Folder Structure

For better maintainability, the project can evolve into the following structure:

```text
Profile_Matching/
|-- app.py
|-- README.md
|-- requirements.txt
|-- data/
|   |-- major_project_dataset.csv
|   |-- all_top_matches.xls
|   |-- live_feedback.csv
|   |-- feedback.xls
|-- src/
|   |-- data_loader.py
|   |-- recommender.py
|   |-- compatibility.py
|   |-- feedback_manager.py
|   |-- ui_components.py
|-- assets/
|   |-- screenshots/
|-- notebooks/
|-- tests/
```

This structure separates data, logic, UI, and documentation while still remaining easy to explain during a viva.

## Installation

1. Clone the repository:

```bash
git clone <your-repository-url>
cd Profile_Matching
```

2. Create a virtual environment:

```bash
python -m venv .venv
```

3. Activate the environment:

```bash
.venv\Scripts\activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

## How to Run

Start the Streamlit application:

```bash
streamlit run app.py
```

After launching, open the local Streamlit URL shown in the terminal.

## Streamlit Community Cloud Deployment

1. Push the project to GitHub.
2. Ensure `app.py`, `requirements.txt`, and data files are present in the repository.
3. Log in to Streamlit Community Cloud.
4. Click `New app`.
5. Select the GitHub repository and branch.
6. Set the main file path to `app.py`.
7. Deploy the app.

## Screenshots

Add screenshots here after deployment:

- `assets/screenshots/home-dashboard.png`
- `assets/screenshots/profile-section.png`
- `assets/screenshots/top-matches-table.png`
- `assets/screenshots/analytics-chart.png`

## Future Scope

- real-time recommendation regeneration instead of static precomputed matches
- authentication for user-specific login
- advanced feedback learning for adaptive ranking
- richer analytics dashboard with filter controls
- model comparison between multiple embedding techniques
- deployment with database-backed storage

## Why This Project Is Viva-Friendly

- the recommendation pipeline is easy to explain step by step
- the UI clearly shows input, output, and analytics
- the code remains simple and readable
- the hybrid approach demonstrates both NLP and rule-based reasoning

## License

This project can be used for academic demonstration, portfolio presentation, and learning purposes.
