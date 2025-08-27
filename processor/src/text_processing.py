import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer





class TextProcessing:
    def __init__(self, original_text):
        self.nltk_downloads()
        self.clean_text = original_text

    def nltk_downloads(self):
        nltk.download('stopwords')
        nltk.download('punkt_tab')


    def removes_punctuation_marks(self):
        self.clean_text = re.sub(r'[^\w\s]', '', self.clean_text)

    def removes_special_characters(self):
        self.clean_text = re.sub(r'[^\w\s]', '', self.clean_text)

    def removing_unnecessary_whitespace_characters(self):
        self.clean_text = re.sub(r'\s+', ' ', self.clean_text).strip()

    def remove_stopwords(self):
        words = word_tokenize(self.clean_text)
        filtered_words = [word for word in words if word.lower() not in stopwords.words('english')]
        self.clean_text = ' '.join(filtered_words)

    def change_to_lower(self):
        self.clean_text = self.clean_text.lower()


p = TextProcessing('if, i wont       hey/.')

p.removes_punctuation_marks()
print(p.clean_text)
p.removes_special_characters()
print(p.clean_text)
p.removing_unnecessary_whitespace_characters()
print(p.clean_text)
p.remove_stopwords()
print(p.clean_text)






