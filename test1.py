import streamlit as st  # Streamlit library for creating web apps
import pandas as pd  # Library for data manipulation
import re  # Library for regular expressions
from sklearn.feature_extraction.text import TfidfVectorizer  # For converting text to TF-IDF vectors
from sklearn.metrics.pairwise import cosine_similarity  # For calculating similarity between vectors

# Text normalization function
# Mətnin normalizasiyası funksiyası
def normalize_colors(text):
    color_map = {
        'black': ['black', 'черный', 'qara', 'negro', 'noir'],
        'white': ['white', 'белый', 'ağ', 'blanco', 'blanc'],
        'grey': ['grey', 'серый', 'gri', 'gris', 'boz'],
        'blue': ['blue', 'синий', 'mavi', 'azul'],
        'natural': ['natural', 'натуральный', 'doğal', 'dogal', 'natural'],
        'titanium': ['titanium', 'титан', 'titan', 'titanio'],
        'pink': ['pink', 'розовый', 'pembe', 'rosa', 'çehrayi'],
        'green': ['green', 'зеленый', 'yeşil', 'verde', 'yaşıl', 'yasil'],
        'graphite': ['graphite', 'графит', 'grafit', 'grafito'],
        'gray': ['gray', 'серый', 'gri', 'gris', 'boz'],
        'dark purple': ['dark purple', 'тёмно-пурпурный', 'koyu mor', 'morado oscuro', 'pourpre foncé', 'tund benovseyi']
    }

    text = text.lower()  # Convert text to lowercase
    for standard_color, variations in color_map.items():
        for variant in variations:
            if ' ' in variant:  # Check if the variant contains spaces
                for word in variant.split():
                    text = re.sub(r'\b' + re.escape(word) + r'\b', standard_color, text)  # Replace with standard color
            else:
                text = re.sub(r'\b' + re.escape(variant) + r'\b', standard_color, text)  # Replace with standard color
    return text

# Normalize the text
# Mətnin normalizasiyasını həyata keçirir
def normalize_text(text):
    text = text.lower()  # Convert text to lowercase
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    text = normalize_colors(text)  # Normalize colors
    return text

# Load data from CSV
# CSV faylından məlumatları yükləyirik
data = pd.read_csv('IrshadDATA.csv')
combined_df = pd.DataFrame(data)
combined_df['Normalized Name'] = combined_df['Product Name'].apply(normalize_text)  # Apply normalization

# TF-IDF vectorizer
# TF-IDF vektorizatoru
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(combined_df['Normalized Name'])  # Transform text data into TF-IDF vectors

# Search function
# Axtarış funksiyası
def search(query, vectorizer, X):
    query = normalize_text(query)  # Normalize the search query
    query_vector = vectorizer.transform([query])  # Convert the query into a TF-IDF vector
    similarities = cosine_similarity(query_vector, X)  # Calculate similarity between the query and the data
    return similarities

# Streamlit app
# Streamlit tətbiqi
st.title('Product Search Engine')  # Set the title of the app

query = st.text_input('Search for a product:')  # Input field for search query

if query:
    similarities = search(query, vectorizer, X)  # Perform the search
    if similarities.size > 0:  # Check if there are any results
        scores = similarities[0]  # Get similarity scores
        results_df = pd.DataFrame({
            'Index': range(len(scores)),
            'Score': scores
        })

        # Sort by score and get top results
        # Nəticələri ballara görə sıralayırıq və ən yaxşılarını əldə edirik
        top_results_df = results_df.sort_values(by='Score', ascending=False).head(5)
        st.write("**Top Similarity Scores:**")
        st.write(top_results_df)  # Display top similarity scores

        # Get top products based on indices
        # İndekslərə əsaslanaraq ən yaxşı məhsulları əldə edirik
        top_indices = top_results_df['Index'].values
        top_products = combined_df.iloc[top_indices]

        st.write('**Search Results:**')
        st.write(top_products[['Product Name']])  # Display top products
    else:
        st.write("No results found.")  # Inform the user if no results are found
