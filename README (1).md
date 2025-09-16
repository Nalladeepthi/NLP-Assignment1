## Q2: Tokenization Task Using spaCy  

**Name:** Deepthi Nalla  
**ID:** 700779838  

### 📌 Overview
This project demonstrates **tokenization** of a paragraph using three different approaches:  
1. **Naïve Space-Based Tokenization**  
2. **Manual Tokenization using Regular Expressions**  
3. **spaCy Tokenization**

The goal is to compare these methods, highlight their differences, and understand the challenges of tokenization.

---

### 🛠 Requirements
- Python 3.8 or higher  
- Install spaCy and its English model:

```bash
pip install spacy
python -m spacy download en_core_web_sm
```

---

### 💻 Code

```python
import spacy
import re

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Paragraph to tokenize
paragraph = """The weather is changing quickly. However, people are still going outside without umbrellas.
It’s surprising, given the dark clouds. Some decided to take raincoats, while others ignored the forecast."""

# 1️⃣ Naïve Space-Based Tokenization
# Splits the paragraph based on spaces only.
naive_tokens = paragraph.split()
print("Naïve Tokens:\n", naive_tokens)

# 2️⃣ Manual Tokenization (using Regular Expressions)
# Handles punctuation and contractions more carefully.
manual_tokens = re.findall(r"\w+|’\w+|[.,!?;]", paragraph)
print("\nManually Corrected Tokens:\n", manual_tokens)

# 3️⃣ spaCy Tokenization
# Uses spaCy’s powerful language model for accurate tokenization.
doc = nlp(paragraph)
spacy_tokens = [token.text for token in doc]
print("\nspaCy Tokens:\n", spacy_tokens)

# 🔍 Comparing Manual vs spaCy Tokens
# Shows differences between manually created tokens and spaCy tokens.
differences = [(m, s) for m, s in zip(manual_tokens, spacy_tokens) if m != s]
print("\nDifferences between Manual and spaCy Tokens:\n", differences)

# 🏷 Multiword Expressions (MWEs)
MWEs = [
    "New York City",     # place name
    "kick the bucket",   # idiom
    "high school"        # common phrase
]
print("\nMultiword Expressions (MWEs):\n", MWEs)
print("Explanation: These should be treated as single tokens because they represent a single concept or entity.")

# 📝 Reflection
reflection = """ 
Reflection:
The hardest part of tokenization is separating punctuation from words and handling contractions like 'It’s' properly.
Compared to English, languages with rich morphology or complex suffixes can be even harder to tokenize.
Punctuation, morphology, and multiword expressions make tokenization more difficult because they can change word boundaries.
Treating MWEs as single tokens is important to preserve meaning and context.
Using spaCy makes tokenization easier and more accurate for professional NLP tasks.
"""
print("\n" + reflection)
```

---

### ⚡ Execution
Run the script:

```bash
python tokenization_task.py
```

It will display:
- Tokens from **space-based**, **manual**, and **spaCy** tokenization.
- Differences between manual and spaCy tokens.
- Examples of **multiword expressions**.

---

### 🧐 Key Learnings
- **Space-based tokenization** is simple but fails with punctuation and contractions.  
- **Regular expressions** improve token handling but require manual adjustments.  
- **spaCy** provides the most accurate tokenization for NLP tasks.  
- Handling **multiword expressions** is essential to maintain the semantic meaning of text.
