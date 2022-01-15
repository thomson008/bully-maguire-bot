import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

from googletrans import Translator

sia = SentimentIntensityAnalyzer()
translator = Translator()

def is_negative(message):
    translation = translator.translate(message)
    print(translation)
    if translation.src != 'en':
        message = translation.text
        
    print(f'Analysis for "{message}": {sia.polarity_scores(message)}')
    return translation.src, sia.polarity_scores(message)['compound'] < 0