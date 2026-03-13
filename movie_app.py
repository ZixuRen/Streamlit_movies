import streamlit as st
import pandas as pd

# Load the cleaned dataset
df = pd.read_csv('movies_clean.csv')

# App title
st.title("🎬 Movie Genre Explorer")

# Get all unique individual genres
all_genres = sorted(set(
    genre
    for genres in df['genres'].dropna()
    for genre in genres.split('|')
))

# Select box - one genre at a time
selected_genre = st.selectbox("Select a Genre:", all_genres)

# Filter movies that contain the selected genre
filtered_df = df[df['genres'].str.contains(selected_genre, na=False)]
filtered_df = filtered_df[['Title', 'Year', 'genres']].reset_index(drop=True)

# Display results
st.write(f"### Movies in genre: {selected_genre}")
st.write(f"Total: {len(filtered_df)} movies")
st.dataframe(filtered_df)
