import streamlit as st
from st_pages import Page, show_pages
st.set_page_config(page_icon="🚀", layout='wide')

show_pages(
    [
        Page("app.py", "Home", "🏠"),
        Page("plot.py", "3D Plots", "📊"),
        Page("image.py", "Image Processing", "🖼️"),
        Page("text.py", "Text Similarity", "📖"),
    ]
)

def main():
    st.header("Rajdeep Banik - 2347141")
    st.subheader("ESE_3 LAB EXAM PYTHON")
    st.subheader("Date: ```16th April 2024```")

if __name__ == "__main__":
    main()
