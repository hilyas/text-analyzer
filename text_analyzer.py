from collections import Counter
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class TextAnalyzer:
    def __init__(self, content):
        self.content = content

    def analyze_text(self):
        words = self.get_words()
        letters = self.get_letters()
        sentences = self.get_sentences()
        sentiment = self.get_sentiment()
        
        total_words = len(words)
        avg_word_length = sum(len(word) for word in words) / total_words
        word_frequency = Counter(words)
        letter_frequency = Counter(letters)
        total_sentences = len(sentences)

        return (
            total_words,
            word_frequency,
            avg_word_length,
            letter_frequency,
            total_sentences,
            sentiment
        )

    def get_words(self):
        tokens = nltk.word_tokenize(self.content)
        words = [word.lower() for word in tokens if re.match(r"\w+", word)]
        return words

    def get_letters(self):
        letters = [letter.lower() for letter in self.content if letter.isalpha()]
        return letters

    def get_sentences(self):
        sentences = nltk.sent_tokenize(self.content)
        return sentences

    def get_pos_tags(self):
        tokens = nltk.word_tokenize(self.content)
        pos_tags = nltk.pos_tag(tokens)
        return pos_tags

    def get_named_entities(self):
        tokens = nltk.word_tokenize(self.content)
        pos_tags = nltk.pos_tag(tokens)
        named_entities = nltk.ne_chunk(pos_tags)
        return named_entities
    
    def get_sentiment(self):
        analyzer = SentimentIntensityAnalyzer()
        sentiment = analyzer.polarity_scores(self.content)
        return sentiment