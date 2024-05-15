import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from collections import Counter
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('omw-1.4')

with open('text.txt', 'r') as txt:
    text = txt.read()

print(text.split())

template = "[a-я-Z0-9]{1,}"
tokens = re.findall(template, text)
print(tokens)

print(len(text.split()))
dic = Counter(text.split())
print(sum(dic.values()))

test_text = text
for i in text:
    if not i.isalpha() and i != ' в':
        test_text = test_text.replace(i, '')
print(text)
print(test_text)

tokens = word_tokenize(text)
stop_words = set(stopwords.words('russian'))
filtered_tokens = [word for word in tokens if word not in stop_words]


stemmer = SnowballStemmer("russian")
tokens = word_tokenize(text)
stemmed_words = [stemmer.stem(word) for word in tokens]

# stemmer = SnowballStemmer("russian")
# tokens = word_tokenize(text)
# lemmatized_words = [stemmer.stem(word) for word in tokens]
# print(lemmatized_words)


lemmatizer = WordNetLemmatizer('russian')
tokens = word_tokenize(text)
lemmatized_words = [lemmatizer.lemmatize(word) for word in tokens]
print(lemmatized_words)

with open('analiz.txt', 'w') as file:
    file.write(f'{text}'+ '\n')
    file.write(f'{text.split()}' + '\n')
    file.write(f'{tokens}'+ '\n')
    file.write(f'{word_tokenize(str(text))}' + '\n')
    file.write(f'{filtered_tokens}' + '\n')
    file.write(f'{stemmed_words}' + '\n')
    file.write(f'{lemmatized_words}' + '\n')
