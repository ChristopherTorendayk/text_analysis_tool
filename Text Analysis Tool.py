import tkinter as tk
import spacy
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load the pre-trained word vectors and English language model
nlp = spacy.load("en_core_web_md")

# Threshold for similarity score to consider a suggestion
similarity_score_threshold = 0.6

# Function to extract noun phrases from the text
def extract_noun_phrases(text):
    doc = nlp(text)
    noun_phrases = [chunk.text for chunk in doc.noun_chunks]
    return noun_phrases

# Function to analyze text
def analyze_text():
    input_text = input_text_area.get("1.0", "end-1c")

    input_noun_phrases = extract_noun_phrases(input_text)

    suggestions = []

    for noun_phrase in input_noun_phrases:
        phrase_suggestions = []

        for phrase in standardized_phrases:
            similarity_score = nlp(noun_phrase).similarity(nlp(phrase))

            if similarity_score > similarity_score_threshold:
                phrase_suggestions.append({
                    "recommended_replacement": phrase,
                    "similarity_score": similarity_score
                })

        phrase_suggestions.sort(key=lambda x: x["similarity_score"], reverse=True)

        if phrase_suggestions:
            suggestions.append({
                "original_noun_phrase": noun_phrase,
                "suggestions": phrase_suggestions
            })

    
    if suggestions:
        result_text.config(text="Original Text:")
        suggestion_text.config(text="Suggestions for Replacements:")
        suggestion_list.delete(0, tk.END)
        for suggestion in suggestions:
            original_noun_phrase = suggestion["original_noun_phrase"]
            top_suggestion = suggestion["suggestions"][0]
            suggestion_list.insert(tk.END, f"Replace '{original_noun_phrase}' with '{top_suggestion['recommended_replacement']}' (Similarity Score: {top_suggestion['similarity_score']:.2f})")
    else:
        result_text.config(text="Original Text:")
        suggestion_text.config(text="No suitable suggestions found.")


root = tk.Tk()
root.title("Text Analysis Tool")


frame = tk.Frame(root)
frame.pack(padx=20, pady=20)


input_label = tk.Label(frame, text="Enter your text:")
input_label.pack()

input_text_area = tk.Text(frame, height=6, width=50)
input_text_area.pack()


analyze_button = tk.Button(frame, text="Analyze", command=analyze_text)
analyze_button.pack()


result_text = tk.Label(frame, text="Original Text:")
result_text.pack()

suggestion_text = tk.Label(frame, text="")
suggestion_text.pack()


suggestion_list = tk.Listbox(frame, height=6, width=50)
suggestion_list.pack()

# Standardized Phrases
standardized_phrases = [
    "Optimal performance",
    "Utilize resources",
    "Enhance productivity",
    "Conduct an analysis",
    "Maintain a high standard",
    "Implement best practices",
    "Ensure compliance",
    "Streamline operations",
    "Foster innovation",
    "Drive growth",
    "Leverage synergies",
    "Demonstrate leadership",
    "Exercise due diligence",
    "Maximize stakeholder value",
    "Prioritize tasks",
    "Facilitate collaboration",
    "Monitor performance metrics",
    "Execute strategies",
    "Gauge effectiveness",
    "Champion change"
]


root.mainloop()
