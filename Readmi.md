# 🧠 Contextual Word Sense Disambiguator (CLI Tool)

This Python-based command-line tool performs **Word Sense Disambiguation (WSD)** using **NLTK's Lesk algorithm**. Given a sentence, it identifies ambiguous (polysemous) words like *bank*, *bat*, *crane*, etc., and returns the most contextually appropriate **WordNet sense**, including its **definition** and **examples**.

---

## 📌 Features

- ✅ Accepts any sentence as input.
- ✅ Optionally specify a target word.
- ✅ Identifies ambiguous words with multiple senses.
- ✅ Outputs the best sense using WordNet:
  - Sense name
  - Definition
  - Example usages

---

## 🚀 Requirements

- Python 3.6+
- [NLTK](https://www.nltk.org/)

### Install Dependencies
```bash
pip install nltk


------------------------------
input -> python app.py "She sat by the bank and watched the river flow." --word bank
output -> Word Sense Disambiguation Results:
----------------------------------------
Word: bank
Sense: bank.n.01
Definition: sloping land (especially the slope beside a body of water)
Examples:
  - they pulled the canoe up on the bank
----------------------------------------

example

python app.py "The crane flew over the lake."

"She sat by the bank and watched the river flow." → bank → land beside a river

"He works at the bank downtown." → bank → financial institution

"The crane stood tall on the construction site." → crane → machine for lifting

"The crane flew over the lake." → crane → bird

