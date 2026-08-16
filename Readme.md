# 📚 Book Recommendation System

A beginner-friendly **AI/ML mini project** that recommends books similar to a user's selected book. The system uses **TF-IDF** and **Cosine Similarity** to analyze book information and generate the top 5 recommendations.

## 🚀 Features

* 🔎 Search using a full or partial book title
* 🔤 Case-insensitive search
* 🤖 Content-based book recommendations
* ⭐ Displays the top 5 similar books
* ✍️ Shows author information
* 🏷️ Shows book genre
* 📝 Displays book descriptions
* 🌐 Interactive web interface using Streamlit

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* TF-IDF Vectorization
* Cosine Similarity
* Streamlit

## 📂 Project Structure

```text
Book Recommendation System/
│
├── main.py
├── app.py
├── README.md
│
└── dataset/
    └── books.csv
```

## ⚙️ How It Works

### 1. Load the Dataset

The system loads book information from `books.csv` using Pandas.

### 2. Combine Book Information

The following information is combined for each book:

* Title
* Author
* Genre
* Description

### 3. Convert Text into Numerical Features

TF-IDF (Term Frequency-Inverse Document Frequency) converts the combined text information into numerical vectors.

### 4. Calculate Similarity

Cosine Similarity is used to compare the book vectors and determine how similar the books are.

### 5. Generate Recommendations

When the user enters a book title, the system finds the matching book and displays the **top 5 most similar books**.

## ▶️ How to Run the Project

### Step 1 — Install Dependencies

Open the terminal in the project folder and run:

```bash
python -m pip install pandas scikit-learn streamlit
```

### Step 2 — Run the Streamlit Application

```bash
python -m streamlit run app.py
```

### Step 3 — Open the Application

Streamlit will provide a local URL such as:

```text
http://localhost:8501
```

Open the URL in your web browser.

## 🔍 Example

Enter:

```text
hobbit
```

The system recognizes the matching book and displays five recommended books along with their:

* Title
* Author
* Genre
* Description

## 🎯 Project Objective

The objective of this project is to understand the basics of **Natural Language Processing (NLP)** and **content-based recommendation systems** by building a practical book recommendation application using Python and machine-learning techniques.

## 📌 Future Improvements

* Add more books to the dataset
* Support multiple languages
* Add book cover images
* Add ratings and popularity information
* Improve the user interface
* Deploy the application online

## 👩‍💻 Author

**Varshitha K S**

BCA Student
PES Institute of Advanced Management Studies (PESIAMS)

---

⭐ If you found this project useful, consider giving it a star on GitHub.
