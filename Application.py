import streamlit as st
import pickle
import pandas as pd

movies_list = pickle.load(open("Movies.pkl", "rb"))

similarity = pickle.load(open("Similarity.pkl", "rb"))

def recommender(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list2 = sorted(list(enumerate(distances)), reverse = True ,key = lambda x: x[1])[1:6]
    to_show = []
    for movies in movies_list2:
        to_show.append(movies_list.iloc[movies[0]].title)
    return to_show

movie_names = movies_list['title'].values

st.title("Movie Recommender System")

select_movie = st.selectbox('Which movie have you seen?', movie_names)

if st.button('To Watch Recommendations'):
    recommendations = recommender(select_movie)
    for movie in recommendations:
        st.write(movie)
