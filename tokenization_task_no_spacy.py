# Q2: Tokenization Task

# Step 1: Paragraph
paragraph = """The weather is changing quickly. However, people are still going outside without umbrellas. 
It’s surprising, given the dark clouds."""

# ---- Naïve Space-Based Tokenization ----
naive_tokens = paragraph.split()
print("Naïve Tokens:\n", naive_tokens)

# ---- Manual Correction (handling punctuation, suffixes, clitics) ----
import re
manual_tokens = re.findall(r"\w+|’\w+|[.,!?;]", paragraph)
print("\nManually Corrected Tokens:\n", manual_tokens)

# ---- Simple Rule-Based Tokenizer (as Tool Replacement) ----
# A very basic imitation of NLP tool tokenization (split on spaces + separate punctuation)
rule_based_tokens = re.findall(r"[A-Za-z]+|’s|[.,!?;]", paragraph)
print("\nRule-Based Tokenizer Tokens:\n", rule_based_tokens)

# ---- Compare manual vs rule-based ----
max_len = max(len(manual_tokens), len(rule_based_tokens))
diffs = []
for i in range(max_len):
    m = manual_tokens[i] if i < len(manual_tokens) else None
    r = rule_based_tokens[i] if i < len(rule_based_tokens) else None
    if m != r:
        diffs.append((m, r))

print("\nDifferences between Manual and Rule-Based:\n", diffs)

# ---- Step 3: Multiword Expressions ----
MWEs = [
    "New York City",       # place name
    "kick the bucket",     # idiom
    "high school"          # fixed phrase
]
print("\nMultiword Expressions (MWEs):\n", MWEs)

# ---- Step 4: Reflection ----
reflection = """
Reflection:
The hardest part of tokenization is handling punctuation and contractions.
In English, words like “It’s” need splitting into ‘It’ and ‘’s’, which is tricky.
Compared to English, languages with rich morphology (like agglutinative ones) 
are even harder to tokenize because suffixes carry meaning. 
Punctuation, morphology, and MWEs definitely increase the difficulty, 
since MWEs should be treated as single tokens though they contain spaces.
"""
print("\n" + reflection)
