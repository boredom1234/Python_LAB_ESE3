import streamlit as st
import pandas as pd
import numpy as np
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


@st.cache_data
def load_data():
    data = pd.read_csv(
        ".\WomensClothingE-CommerceReviews.csv", encoding="utf-8")
    return data


def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    tokens = word_tokenize(text.lower())
    filtered_tokens = [
        token for token in tokens if token not in string.punctuation and token not in stop_words]
    lemmatized_tokens = [lemmatizer.lemmatize(
        token) for token in filtered_tokens]

    return ' '.join(lemmatized_tokens)

# Cosine
def calculate_similarity(data):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(data)
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return cosine_sim


def main():
    st.title("Text Similarity Analysis")

    data_load_state = st.text("Loading data...")
    data = load_data()
    data_load_state.text("Data loaded successfully!")

    division_names = data['Division_Name'].unique()
    division = st.sidebar.selectbox("Select a Division", division_names)

    filtered_data = data[data['Division_Name'] == division]
    reviews = filtered_data['ReviewText'].astype(str)

    preprocessed_reviews = reviews.apply(preprocess_text)

    similarity_matrix = calculate_similarity(preprocessed_reviews)

    st.subheader("Cosine Similarity Matrix")
    st.write(pd.DataFrame(similarity_matrix,
             columns=filtered_data.index, index=filtered_data.index))

    threshold = st.slider("Select similarity threshold", 0.0, 1.0, 0.7, 0.05)
    st.subheader("Similar Reviews")
    for i in range(len(similarity_matrix)):
        for j in range(i+1, len(similarity_matrix[i])):
            if similarity_matrix[i][j] > threshold:
                st.write(
                    f"Review {filtered_data.index[i]} and Review {filtered_data.index[j]} have a similarity score of {similarity_matrix[i][j]:.2f}")
                st.write(
                    f"Review {filtered_data.index[i]}: {filtered_data.iloc[i]['ReviewText']}")
                st.write(
                    f"Review {filtered_data.index[j]}: {filtered_data.iloc[j]['ReviewText']}")
                st.write("="*50)


if __name__ == "__main__":
    main()
