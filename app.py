import pickle                               #importing all the required libraries
import pandas as pd
import streamlit as st
import requests
import time

def Posters_Movie(movie_id):              # helper function to fetch the posters for movies
    link = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data_source = requests.get(link)
    data_source = data_source.json()
    MoviePosters = data_source['poster_path']
    TotalPaths = "https://image.tmdb.org/t/p/w500/" + MoviePosters
    return TotalPaths

def recommend_movies(movie):         #function to recommend all the movies#
    index = movies[movies['title'] == movie].index[0]
    distances_movie = sorted(list(enumerate(similarity_basis[index])), reverse=True, key=lambda x: x[1]) #calculating distance
    movie_name_recommendations = []                                                                     # between movies#
    movie_posters_recommendations = []
    for i in distances_movie[1:6]:
        # fetching the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        movie_posters_recommendations.append(Posters_Movie(movie_id))
        movie_name_recommendations.append(movies.iloc[i[0]].title)

    return movie_name_recommendations, movie_posters_recommendations


st.header('MOVIE PREDICTOR AND RECOMMENDER')     # to give it a title
movies_data= pickle.load(open('movies_data.pkl', 'rb'))   #opening the movies_data pickle file  in binary mode here
movies = pd.DataFrame(movies_data)   #creating dataframe and passing movies_data
similarity_basis = pickle.load(open('movies_similarities.pkl', 'rb')) #opening the movies_similarities pickle file  in binary
                                                                      #mode here

new_movies = movies['title'].values
movie_selections = st.selectbox(    #adding a select box to select different movies
    "Watch Your Favourite Movie",
     new_movies
)

if st.button('Recommend Me'):  #creating button to recommend movies
    movie_name_recommendations, movie_posters_recommendations = recommend_movies(movie_selections)
    column1, column2, column3, column4, column5 = st.columns(5)    # creating 5 different movie's columns to recommend
    with column1:
        st.text(movie_name_recommendations[0])                       # showing first movie name and image
        st.image(movie_posters_recommendations[0])
    with column2:                                                    # showing  second movie name and image
        st.text(movie_name_recommendations[1])
        st.image(movie_posters_recommendations[1])

    with column3:                                                     # showing third movie name and image
        st.text(movie_name_recommendations[2])
        st.image(movie_posters_recommendations[2])
    with column4:                                                     # showing fourth movie name and image
        st.text(movie_name_recommendations[3])
        st.image(movie_posters_recommendations[3])
    with column5:                                                     # showing fifth movie name and image
        st.text(movie_name_recommendations[4])
        st.image(movie_posters_recommendations[4])

