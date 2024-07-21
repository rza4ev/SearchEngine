This project involves developing a search engine for products using a Streamlit web application. The primary goal is to provide an intuitive and efficient search experience for users looking for specific products on an e-commerce website.

Key Features:

Text Normalization:

The search engine employs a text normalization process to standardize product names by normalizing variations in color names and other textual discrepancies. This involves converting product names to a standard format using a predefined color map that accounts for different languages and synonyms.
TF-IDF Vectorization:

The application utilizes TF-IDF (Term Frequency-Inverse Document Frequency) vectorization to convert product names into numerical vectors. This method helps in quantifying the relevance of each product to the search query.
Similarity Calculation:

The search functionality is powered by cosine similarity, which measures the similarity between the search query and product names. The most relevant products are identified based on their similarity scores.
Streamlit Interface:

The project features a user-friendly interface built with Streamlit, allowing users to input search queries and view the results in a clear and organized format. The interface displays both the similarity scores and the top matching products.
Data Handling:

Product data is loaded from a CSV file, which is processed and used for searching. The application can handle a variety of products, with results being dynamically updated based on user input.
Technical Details:

Libraries and Tools:

Streamlit for the web interface.
Pandas for data manipulation.
Scikit-learn for TF-IDF vectorization and similarity calculations.
Regular expressions for text processing.
Data Source:

Product data is read from an IrshadDATA.csv file containing product names and other relevant information.
Usage:

Run the Streamlit application to launch the search engine interface.
Enter a product name or keyword into the search field.
View the search results, including similarity scores and the top matching products.
This project is designed to enhance the product search experience by leveraging advanced text processing techniques and a straightforward web interface.
