import networkx as nx
import urllib.parse
import random
from networkx.algorithms import community
import matplotlib.pyplot as plt
import os
import glob
from sklearn.feature_extraction.text import TfidfVectorizer

# Function to load the graph from the links.tsv file
def load_wikispeedia_graph(filepath):
    G = nx.DiGraph()
    with open(filepath, 'r') as f:
        for line in f:
            # Skip comment lines and empty lines
            if line.startswith('#') or not line.strip():
                continue
            # Split the line into source and target
            parts = line.strip().split('\t')
            if len(parts) != 2:
                continue  # Skip lines that do not have exactly two parts
            source, target = parts
            # Decode the URL-encoded names
            source = urllib.parse.unquote(source)
            target = urllib.parse.unquote(target)
            # Add edge to the graph
            G.add_edge(source, target)
    return G

# Function to load the navigation paths from the dataset
def load_navigation_paths(filepath):
    paths = []
    with open(filepath, 'r') as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            parts = line.strip().split('\t')
            if len(parts) != 5:
                continue
            path = [urllib.parse.unquote(node) for node in parts[3].split(';')]
            paths.append(path)
    return paths

# # Function to read the text content of all pages
# def load_wikispeedia_data(data_directory):
#     page_texts = {}
#     for filepath in glob.glob(os.path.join(data_directory, "*.txt")):
#         with open(filepath, 'r', encoding='utf-8') as file:
#             content = file.read()
#             page_name = os.path.basename(filepath).replace(".txt", "")
#             page_texts[page_name] = content
#     return page_texts

def load_wikispeedia_data(data_directory):
    page_texts = {}
    for filepath in glob.glob(os.path.join(data_directory, "*.txt")):
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            page_name = os.path.basename(filepath).replace(".txt", "")
            decoded_page_name = urllib.parse.unquote(page_name)  # Decode percent-encoded characters
            page_texts[decoded_page_name] = content
    return page_texts


# Function to vectorize the textual content
def vectorize_texts(page_texts):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(page_texts.values())
    return tfidf_matrix, vectorizer
