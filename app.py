import streamlit as st
import pickle
import numpy as np
import pandas as pd


df = pd.DataFrame(pickle.load(open('dataset.pkl','rb')))
similarity = pd.DataFrame(pickle.load(open('similarity.pkl','rb')))

def recommend(value):
    names_list = []
    image_list =[]
    links_list =[]
    index = df[df['Title']== value].index[0]
    distance = similarity[index]
    games = sorted(list(enumerate(distance)),key = lambda x:x[1],reverse=True)[1:11]
    for i in games:
        names_list.append((df.iloc[i[0]][0]))
        image_list.append((df.iloc[i[0]][5]))
        links_list.append((df.iloc[i[0]][6]))
    return names_list,image_list,links_list


st.title(":red[Game Recommender]")

st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://wallpapercave.com/wp/wp10326658.jpg');
        background-repeat: no-repeat;
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

selected_anime_name = st.selectbox('Select Game You Like',(df['Title'].values))

if st.button('Recommend'):
    name,poster,link = recommend(selected_anime_name)

    for i in range(len(name)):
        data = (f'{name[i]}')
        caption = f'<h2>{data}</h2>'
        st.markdown(f'<a href = "{link[i]}" target ="_blank">Click Here To Explore More </a>',unsafe_allow_html=True)
        st.image(poster[i])

    
  
