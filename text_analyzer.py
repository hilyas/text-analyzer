from collections import Counter
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from abc import ABC, abstractmethod

class TextExtractor:
    def __init__(self, content: str):
        self.content = content

    def get_words(self) -> list:
        tokens = nltk.word_tokenize(self.content)
        words = [word.lower() for word in tokens if re.match(r"\w+", word)]
        return words

    def get_letters(self) -> list:
        return [letter.lower() for letter in self.content if letter.isalpha()]

    def get_sentences(self) -> list:
        return nltk.sent_tokenize(self.content)

class TextAnalyzer(ABC):
    def __init__(self, content: str):
        self.content = content
        self.extractor = TextExtractor(content)

    @abstractmethod
    def analyze_text(self):
        pass

class TextStatistics(TextAnalyzer):
    def analyze_text(self):
        words = self.extractor.get_words()
        letters = self.extractor.get_letters()
        sentences = self.extractor.get_sentences()
        
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
            total_sentences
        )

class TextNLP(TextAnalyzer):
    def get_pos_tags(self) -> list:
        tokens = nltk.word_tokenize(self.content)
        return nltk.pos_tag(tokens)

    def get_named_entities(self):
        tokens = nltk.word_tokenize(self.content)
        pos_tags = self.get_pos_tags()
        return nltk.ne_chunk(pos_tags)
    
    def get_sentiment(self) -> dict:
        analyzer = SentimentIntensityAnalyzer()
        return analyzer.polarity_scores(self.content)

    def analyze_text(self):
        return {
            'sentiment': self.get_sentiment(),
            'pos_tags': self.get_pos_tags(),
            'named_entities': self.get_named_entities()
        }
