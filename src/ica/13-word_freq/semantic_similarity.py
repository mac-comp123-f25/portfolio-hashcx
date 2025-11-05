from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

doc1 = "Mars is the fourth planet in our solar system."
doc2 = "Saturn is a yellow planet, the sixth from the Sun."
doc3 = "Mars is the second-smallest planet after Mercury."

documents = [doc1, doc2, doc3]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# Calculate similarity between doc1 and doc3
similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[2:3])[0][0]
print(f"Cosine similarity between doc1 and doc3: {similarity_score:.2f}")

# Calculate similarity between doc1 and doc2
similarity_score_diff = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
print(f"Cosine similarity between doc1 and doc2: {similarity_score_diff:.2f}")
