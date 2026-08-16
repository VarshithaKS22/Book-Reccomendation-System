import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the book dataset
books = pd.read_csv("dataset/books.csv")

# Combine book information
books["combined_features"] = (
    books["Title"] + " " +
    books["Author"] + " " +
    books["Genre"] + " " +
    books["Description"]
)

# Convert text into numbers
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(books["combined_features"])

# Calculate similarity between books
similarity = cosine_similarity(tfidf_matrix)


# Recommendation function
def recommend_books(book_title):

    # Remove extra spaces and make search case-insensitive
    search = book_title.strip().lower()

    # Find matching books
    matches = books[
        books["Title"].str.lower().str.contains(search, na=False)
    ]

    if matches.empty:
        print("Book not found.")
        return

    # Select the first matching book
    book_index = matches.index[0]

    print(f"\nSelected Book: {books.loc[book_index, 'Title']}")

    # Calculate similarity scores
    similarity_scores = list(enumerate(similarity[book_index]))

    # Sort from most similar to least similar
    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    print("\nRecommended Books:")

    for i, score in similarity_scores[1:6]:
        print(books.iloc[i]["Title"])


# Get input from user
book_name = input("Enter a book name: ")

# Run recommendation system
recommend_books(book_name)