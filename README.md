# Text Analysis Tool

## Overview

The Text Analysis Tool is a Python application that analyzes input text and suggests improvements based on the similarity to a list of standardized phrases. These standardized phrases represent the ideal way certain concepts should be articulated. The tool provides recommendations to align the input text closer to these standards.

## Features

- **Input Text Analysis:** Users can input text through a user-friendly graphical interface

- **Standardized Phrases:** The tool comes pre-loaded with a list of standardized phrases, which can be customized for various domains (e.g., business jargon, scientific terminology).

- **Semantic Similarity:** The tool uses a pre-trained language model and techniques like cosine similarity with word embeddings to find phrases in the input text that are semantically similar to the standardized phrases.

- **Suggestions:** It provides a list of suggestions to replace phrases in the input text with their more "standard" versions. Each suggestion displays the original phrase, the recommended replacement, and the similarity score.


## Technologies Used

- Python
- Tkinter (for the GUI)
- spaCy (for natural language processing)
- NumPy (for numerical computations)
- scikit-learn (for cosine similarity calculations)

## How it Works

1. The user inputs text through the GUI.

2. The tool extracts noun phrases from the input text.

3. It calculates cosine similarity between each noun phrase in the input text and a list of standardized phrases.

4. Suggestions are provided for replacing noun phrases with similar standardized phrases.

5. Suggestions are displayed in the GUI or printed to the console.

## Design Decisions

- We chose spaCy for natural language processing due to its accuracy and efficiency.

- A graphical user interface (GUI) was implemented using Tkinter to enhance user experience.

- A similarity threshold is used to control the strictness of suggestions.

