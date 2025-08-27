import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag





class TextProcessing:
    def __init__(self, original_text):
        self.nltk_downloads()
        self.clean_text = original_text

    def nltk_downloads(self):
        nltk.download('stopwords')
        nltk.download('punkt_tab')
        nltk.download('wordnet')
        nltk.download('omw-1.4')
        nltk.download('averaged_perceptron_tagger_eng')

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

    def lemmatization(self):
        lemmatizer = WordNetLemmatizer()
        tokens = word_tokenize(self.clean_text)
        tagged_tokens = pos_tag(tokens)

        lemmatized_sentence = []

        for word, tag in tagged_tokens:
            if word.lower() == 'are' or word.lower() in ['is', 'am']:
                lemmatized_sentence.append(word)
            else:
                lemmatized_sentence.append(lemmatizer.lemmatize(word, self.get_wordnet_pos(tag)))
        self.clean_text = ' '.join(lemmatized_sentence)

    def get_wordnet_pos(self, tag):
        if tag.startswith('J'):
            return 'a'
        elif tag.startswith('V'):
            return 'v'
        elif tag.startswith('N'):
            return 'n'
        elif tag.startswith('R'):
            return 'r'
        else:
            return 'n'





p = TextProcessing('if, i wont Want I wanted    running   hey/.')

p.removes_punctuation_marks()
print(p.clean_text)
p.removes_special_characters()
print(p.clean_text)
p.removing_unnecessary_whitespace_characters()
print(p.clean_text)
p.remove_stopwords()
print(p.clean_text)
p.change_to_lower()
print(p.clean_text)
p.lemmatization()
print(p.clean_text)






