import threading, uuid, json, spacy, pickle, random

nlp = spacy.load("en_core_web_sm")

print('Data loading')

code = """

import threading, uuid, json, spacy, pickle, random

with open('wiki.json') as wiki:
    data = json.loads(wiki.read())

print('Data loaded')

random.shuffle(data)


def chunks(lst: list, n: int):
    '''Yield successive n-sized chunks from lst.'''
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


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


"""

threads = 5

uuids = []

code = code + "cut = list(chunks(data, len(data) // " + str(threads) + "))\n"

for i in range(0, threads):
    uid = "a" + str(uuid.uuid4())[:8]

    uuids.append(uid)
    code = code + "list" + uid + " = cut[" + str(uuids.index(uid)) + "]\n"

code = code + "\n"

for uid in uuids:
    code = code + uid + " = threading.Thread(target=compute, args=(list" + uid + ",  '" + uid + "'))\n"

code = code + "\n"

for uid in uuids:
    code = code + uid + ".start()\n"

code = code + "\n"

if input("run> ") == "y":
    print(code)

with open('output.py', 'w') as f:
  f.write(code)

'''
# ---------------------------- COMPUTE --------------------------------
first = threading.Thread(target=compute, args=(firstq,  'first'))
second = threading.Thread(target=compute, args=(secondq, 'second'))
third = threading.Thread(target=compute, args=(thirdq,  'third'))
fourth = threading.Thread(target=compute, args=(fourthq, 'fourth'))

first.start()
second.start()
third.start()
fourth.start()
'''
