from collections import Counter
import matplotlib.pyplot as plt
from nltk.draw import dispersion_plot
from nltk import word_tokenize, Text
import pymorphy3

with open("text.txt", encoding="utf-8") as p:
    text = p.read()


def grapher(text: str):
    text = text.split()
    word_count = Counter(text)
    word_count = word_count.most_common(10)
    plt.plot([word for word, count in word_count], [count for word, count in word_count])
    plt.show()


def disp(text: str):
    text = text.split()
    words = []
    for i in range(len(text)):
        if text[i] not in words:
            words.append(text[i])
        if len(words) == 10:
            break
    dispersion_plot(text, words)
    plt.show()


def gram(text: str):
    text = text.split()
    morph = pymorphy3.MorphAnalyzer()
    gram_info = [morph.parse(word)[0].tag.POS for word in text]
    with open("gram_text.txt", "w", encoding="utf-8") as clean:
        for i in range(len(gram_info)):
            if gram_info[i] is None:
                continue
            clean.write(gram_info[i])
            clean.write(" ")
    for i in gram_info:
        if i is None:
            gram_info.remove(i)
    return gram_info


def gram_graf(text: str):
    new_text = gram(text)
    word_count = Counter(new_text)
    word_count = word_count.most_common(5)
    print(dict(word_count))
    plt.plot([word for word, count in word_count], [count for word, count in word_count])
    plt.show()


def optional(text: str):
    tokens = word_tokenize(text)
    text_obj = Text(tokens)
    sim_word = text_obj.similar("война")
    com_word = text_obj.common_contexts(['холод', 'осень'], 2)
    coll_word = text_obj.collocations()
    return sim_word, com_word, coll_word


while True:
    x = input("введите номер программы: ")
    if x == "1":
        disp(text)
    elif x == "2":
        grapher(text)
    elif x == "3":
        gram_graf(text)
    elif x == "4":
        optional(text)
    else:
        break
