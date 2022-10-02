import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

# Defining the stop words and punctuation to be excluded from word scoring
STOPWORDS = list(STOP_WORDS)
PUNCTUATION = punctuation + '\n'

SUMMARIZATION_RATIO = 0.3


def _calc_word_count(doc):
    word_count = {}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
                if word.text.lower() not in word_count.keys():
                    word_count[word.text.lower()] = 1
                else:
                    word_count[word.text.lower()] += 1
    
    return word_count

def calc_word_freq(doc):
     
    word_frequencies = _calc_word_count(doc)
    max_frequency = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word]/max_frequency

def calc_sent_score(doc, sentence_tokens):

    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]


def Summarize(text):

    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)

    tokens = [ token.text for token in doc]

    word_frequencies = calc_word_freq(doc)

    sentence_tokens = [sent for sent in doc.sents]

    sentence_scores = calc_sents_score(doc, sentence_tokens)


    select_length = int(len(sentence_tokens) * SUMMARIZATION_RATIO)
    summary = nlargest(select_length, sentence_scores, key = sentence_scores.get)

    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)

    return summary

    

    

    


    
    

