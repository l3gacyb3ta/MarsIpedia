import threading
import json
import spacy
import pickle
import random

nlp = spacy.load("en_core_web_sm")

print('Data loading')

# '''
with open('wiki.json') as wiki:
    data = json.loads(wiki.read())

print('Data loaded')

random.shuffle(data)


def chunks(lst: list, n: int):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


cut = list(chunks(data, len(data) // 4))

firstq = cut[0]
secondq = cut[1]
thirdq = cut[2]
fourthq = cut[3]


def compute(half: list, which_half: str):

    keywords = {}
    '''Computes the data from the data.'''
    count = 0
    for article in half:

        print(article['title'])

        # calculate percent
        percent = str(round((half.index(article) / len(half))*100, 2))
        #         ^str ^round      ^get percent  ^divide    ^readability

        print(percent, "%")

        doc = nlp(article['text'])

        for keyword in doc.ents[:len(doc.ents)//2]:
            # stttrrr
            keyword = str(keyword).lower()
            if not keyword in keywords.keys():
                keywords[keyword] = [article['title']]

            else:
                keywords[keyword].append(article['title'])

        if count == 10:
            with open('data/' + which_half + ".pic", 'wb') as pic:
                pickle.dump(keywords, pic)
                print("-------backed up")
            count = 0

        count = count + 1
# '''


# ---------------------------- COMPUTE --------------------------------
first = threading.Thread(target=compute, args=(firstq,  'first'))
second = threading.Thread(target=compute, args=(secondq, 'second'))
third = threading.Thread(target=compute, args=(thirdq,  'third'))
fourth = threading.Thread(target=compute, args=(fourthq, 'fourth'))

first.start()
second.start()
third.start()
fourth.start()
