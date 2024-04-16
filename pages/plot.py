import streamlit as st
import pandas as pd
import plotly.express as px


@st.cache_data
def load_data():
    df = pd.read_csv('WomensClothingE-CommerceReviews.csv')
    return df


df = load_data()


st.sidebar.title('Explore Dataset')
option = st.sidebar.selectbox(
    'Select an option', ['Show Dataset', 'Statistics', 'Reviews', '3D Plot'])


if option == 'Show Dataset':
    st.subheader('Raw Data')
    st.write(df)

elif option == 'Statistics':
    st.subheader('Data Statistics')
    st.write(df.describe())
    st.write(df.describe(include='object'))
    st.write(df.describe(include='all'))


elif option == 'Reviews':
    st.subheader('Reviews Analysis')

    min_rating = st.slider('Minimum Rating', 1, 5, 1)
    filtered_df = df[df['Rating'] >= min_rating]

    st.write(filtered_df[['Age', 'Title', 'ReviewText', 'Rating']])

elif option == '3D Plot':
    st.subheader('3D Plot: Age, Rating, and Positive Feedback Count')

    filtered_data = df[['Age', 'Rating', 'Positive_Feedback_Count']]

    fig = px.scatter_3d(filtered_data, x='Age', y='Rating', z='Positive_Feedback_Count',
                        title='Relationship between Age, Rating, and Positive Feedback Count',
                        size_max=1)

    fig2 = px.bar(filtered_data, x='Age', y='Rating',
                  title='Relationship between Age, Rating, and Positive Feedback Count')

    st.plotly_chart(fig)
    st.plotly_chart(fig2)
