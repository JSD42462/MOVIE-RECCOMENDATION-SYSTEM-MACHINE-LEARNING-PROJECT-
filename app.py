import streamlit as st

st.title("Movie Recommendation System")

import pickle
import requests 

movies = pickle.load(open('movies_list.pkl', 'rb'))

title = st.selectbox("Select Movie", movies)

 
def get_recommendations(title):
    # Load the recommendation model
    cosine_sim = pickle.load(open('similarity.pkl', 'rb'))
    
    
    idx = movies.index[movies== title].tolist()[0]
    # Get the pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))
    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get the indices of the top 5 most similar movies
    movie_indices = [i[0] for i in sim_scores[1:6]]
    
    # Return the top 10 most similar movies
    return movies.iloc[movie_indices]
# Show recommendation button
if st.button("Show Recommendations"):
    # Get recommendations for the selected movie
    recommended_movies = get_recommendations(title)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    cols = [col1, col2, col3, col4, col5]
    for i, movie in enumerate(recommended_movies):
      cols[i].text(movie)
      

