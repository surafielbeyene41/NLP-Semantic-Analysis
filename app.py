import nltk
from nltk.wsd import lesk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import argparse

# Ensure required NLTK data is downloaded
try:
    nltk.data.find('corpora/wordnet')
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('taggers/averaged_perceptron_tagger')
except LookupError:
    nltk.download('wordnet')
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')

def is_ambiguous(word):
    """Check if a word has multiple senses in WordNet."""
    synsets = wn.synsets(word)
    return len(synsets) > 1

def get_word_senses(word):
    """Retrieve all WordNet senses for a word with their definitions."""
    senses = []
    for synset in wn.synsets(word):
        senses.append({
            'name': synset.name(),
            'definition': synset.definition(),
            'examples': synset.examples()
        })
    return senses

def disambiguate_sentence(sentence, target_word=None):
    """Disambiguate words in a sentence using the Lesk algorithm."""
    # Tokenize and POS tag the sentence
    tokens = word_tokenize(sentence)
    tagged = pos_tag(tokens)
    
    # If a target word is specified, focus on it; otherwise, check all words
    words_to_process = [target_word] if target_word else tokens
    
    results = []
    for word in words_to_process:
        # Skip if word is not in the sentence or not ambiguous
        if word not in tokens or not is_ambiguous(word):
            continue
        
        # Apply Lesk algorithm to disambiguate
        synset = lesk(sentence, word)
        if synset:
            results.append({
                'word': word,
                'sense': synset.name(),
                'definition': synset.definition(),
                'examples': synset.examples()
            })
    
    return results

def main():
    """Main function to handle CLI input and output."""
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Word Sense Disambiguation using Lesk algorithm")
    parser.add_argument("sentence", help="Input sentence for WSD")
    parser.add_argument("--word", help="Specific word to disambiguate (optional)", default=None)
    args = parser.parse_args()

    # Perform disambiguation
    results = disambiguate_sentence(args.sentence, args.word)

    # Display results
    if not results:
        print("No ambiguous words found or no valid senses identified.")
        return

    print("\nWord Sense Disambiguation Results:")
    print("-" * 40)
    for result in results:
        print(f"Word: {result['word']}")
        print(f"Sense: {result['sense']}")
        print(f"Definition: {result['definition']}")
        if result['examples']:
            print("Examples:")
            for ex in result['examples']:
                print(f"  - {ex}")
        print("-" * 40)

if __name__ == "__main__":
    main()