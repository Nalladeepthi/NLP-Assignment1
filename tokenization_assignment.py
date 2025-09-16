# ----------------------------
# Q2. Tokenization Assignment
# ----------------------------

# Install spaCy and English model if not already installed:
# pip install spacy
# python -m spacy download en_core_web_sm

import spacy

# ---------- 1. INPUT PARAGRAPH ----------
paragraph = ("Natural language processing is rapidly evolving. "
             "It's changing how humans interact with machines. "
             "Applications such as chatbots, translation, and sentiment analysis are growing daily.")

print("Original Paragraph:\n", paragraph, "\n")

# ---------- 1a. Naïve space-based tokenization ----------
naive_tokens = paragraph.split()
print("Naïve Space-Based Tokens:\n", naive_tokens, "\n")

# ---------- 1b. Manual correction ----------
# Remove trailing punctuation, handle contractions like "It's"
# and ensure words like "chatbots," -> "chatbots"
manual_tokens = []
for token in naive_tokens:
    # strip common punctuation at start/end
    corrected = token.strip(".,!?;:'\"")
    manual_tokens.append(corrected)

# handle contraction "It's" -> "It", "'s"
manual_corrected = []
for tok in manual_tokens:
    if tok.lower() == "it's":
        manual_corrected.extend(["It", "'s"])
    else:
        manual_corrected.append(tok)

print("Manually Corrected Tokens:\n", manual_corrected, "\n")

# ---------- 2. Compare with spaCy Tokenizer ----------
nlp = spacy.load("en_core_web_sm")
spacy_doc = nlp(paragraph)
spacy_tokens = [token.text for token in spacy_doc]
print("spaCy Tokens:\n", spacy_tokens, "\n")

# ---------- Differences ----------
naive_set = set(manual_corrected)
spacy_set = set(spacy_tokens)
diff_spacy_extra = spacy_set - naive_set
diff_manual_extra = naive_set - spacy_set

print("Tokens found by spaCy but not in manual:", diff_spacy_extra)
print("Tokens found in manual but not by spaCy:", diff_manual_extra, "\n")

# ---------- 3. Multiword Expressions ----------
MWEs = [
    "natural language processing",
    "machine learning",
    "sentiment analysis"
]
print("Multiword Expressions (MWEs):")
for mwe in MWEs:
    print("-", mwe, ": should be treated as a single token because it expresses one fixed concept.\n")

# ---------- 4. Reflection Template ----------
reflection = """
Reflection:
Tokenization was challenging when handling punctuation and contractions (e.g., "It's").
English contractions and possessives require splitting into multiple tokens.
Compared to English, some languages (like Chinese or Hindi) may not have spaces at all,
making tokenization even harder.
Punctuation, complex morphology, and MWEs all add difficulty, because a simple
space-based split cannot capture semantic units.
"""

print(reflection)
