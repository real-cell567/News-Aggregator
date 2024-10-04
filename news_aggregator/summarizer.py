import spacy

nlp = spacy.load('en_core_web_sm')

def summarize_text(text):
    if not text:
        return "No summary available."
    doc = nlp(text)
    sentences = [sent for sent in doc.sents]
    return " ".join(str(sent) for sent in sentences[:3])  # Returns the first 3 sentences
