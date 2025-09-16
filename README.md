# Tokenization Task - README

## Overview
This project demonstrates tokenization of a paragraph in English using three approaches:
1. **Naïve Tokenization** - simple space-based split.
2. **Manual Tokenization** - regex-based correction for punctuation, clitics, and suffixes.
3. **Rule-Based Tokenization** - a simple automated method that imitates an NLP tool.

It also compares the results, identifies multiword expressions (MWEs), and provides a short reflection.

---

## Files
- `tokenization_task_no_spacy.py` : Python script that runs without requiring any external libraries.

---

## Requirements
- Python 3.x
- No external libraries needed (uses only built-in `re` for regex).

---

## How to Run
1. Open a terminal (or VS Code terminal).
2. Navigate to the folder where the file is saved.
3. Run the script:
   ```bash
   python tokenization_task_no_spacy.py
   ```

---

## Expected Output
The script will print:
- Naïve tokens (split on spaces).
- Manually corrected tokens.
- Rule-based tokenizer tokens.
- Differences between manual and rule-based tokens.
- Examples of Multiword Expressions (MWEs).
- A short reflection on tokenization challenges.

---

## Notes
- You can replace the sample paragraph inside the script with your own text.
- The script is fully portable and does not require installing spaCy or other NLP libraries.
