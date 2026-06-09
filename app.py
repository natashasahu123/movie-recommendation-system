import streamlit as st
import pickle
import joblib
st.title("Movie Recommendation System")
with open ("movies.pickle",'rb')as m:
    movies=pickle.load(m)
movie_name=movies['title'].values
similarities=joblib.load("similarities.joblib")
name_movie=st.selectbox("Enter Movie name:",movie_name)
def recommend(name_movie):
    movie_index=movies[movies['title']==name_movie].index[0]
    recommendations=similarities[movie_index]
    movie_list=sorted(enumerate(recommendations),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies
if st.button("Recommend"):
    r=recommend(name_movie)
    st.write("Recommended Movies are :")
    for i in r:
        st.write(i)