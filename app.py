import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# -----------------------------
# Page Settings
# -----------------------------

st.set_page_config(
    page_title="Book Recommendation System",
    page_icon="📚",
    layout="centered"
)


# -----------------------------
# Custom Design
# -----------------------------

st.markdown("""
<style>

.stApp {
    background-color: #f5f7fb;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #243b6b;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #6b7280;
    margin-bottom: 30px;
}

.book-card {
    padding: 15px;
    margin: 10px 0;
    border-radius: 10px;
    background-color: white;
    border: 1px solid #dfe4ee;
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# Title
# -----------------------------

st.markdown(
    '<div class="title">📚 Book Recommendation System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Discover your next favorite book using AI-powered recommendations.</div>',
    unsafe_allow_html=True
)


# -----------------------------
# Load Dataset
# -----------------------------

books = pd.read_csv("dataset/books.csv")


# -----------------------------
# Combine Book Information
# -----------------------------

books["combined_features"] = (
    books["Title"] + " " +
    books["Author"] + " " +
    books["Genre"] + " " +
    books["Description"]
)


# -----------------------------
# TF-IDF
# -----------------------------

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(
    books["combined_features"]
)


# -----------------------------
# Cosine Similarity
# -----------------------------

similarity = cosine_similarity(tfidf_matrix)


# -----------------------------
# User Input
# -----------------------------

book_name = st.text_input(
    "📖 Enter a book name",
    placeholder="Example: hobbit"
)


# -----------------------------
# Recommendation Button
# -----------------------------

if st.button("🔍 Recommend Books"):

    if book_name.strip() == "":
        st.warning("Please enter a book name.")

    else:

        search = book_name.strip().lower()

        matches = books[
            books["Title"]
            .str.lower()
            .str.contains(search, na=False)
        ]

        if matches.empty:

            st.error("Book not found. Try another title.")

        else:

            book_index = matches.index[0]

            selected_book = books.loc[
                book_index, "Title"
            ]

            st.success(
                f"Selected Book: {selected_book}"
            )

            similarity_scores = list(
                enumerate(similarity[book_index])
            )

            similarity_scores = sorted(
                similarity_scores,
                key=lambda x: x[1],
                reverse=True
            )

            st.subheader("📖 Recommended Books")

            for i, score in similarity_scores[1:6]:
                title = books.iloc[i]["Title"]
                author = books.iloc[i]["Author"]
                genre = books.iloc[i]["Genre"]
                description = books.iloc[i]["Description"]

                st.markdown(
                    f"""
                    <div class="book-card">
                        <h3>📘 {title}</h3>
                        <p><b>Author:</b> {author}</p>
                        <p><b>Genre:</b> {genre}</p>
                        <p><b>About:</b> {description}</p>
                        <p>✨ Recommended for you</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )