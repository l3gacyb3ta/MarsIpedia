import json, spacy, pickle

nlp = spacy.load("en_core_web_sm")

print('Data loading')

#'''
with open('wiki.json') as wiki:
  data = json.loads(wiki.read())

print('Data loaded')

# print(data)

keywords = {}

count = 0

for article in data:

  print(article['title'])

  # calculate percent
  percent = str(round((data.index(article) / len(data))*100, 2))
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
    with open("progress.pic", 'wb') as pic:
      pickle.dump(keywords, pic)
      print("-------backed up")
    count = 0
  
  count = count + 1
#'''

with open('progress.pic', 'rb') as f:
  keywords = pickle.load(f)

#print(keywords)

stop = nlp.Defaults.stop_words

while True:
  query = input("> ")

  if " " in query:
    results = []
    querys = query.split(' ')

    for q in querys:
      if q in stop:
        pass

      try:
        results.append(keywords[q])

      except:
        pass
    
    if len(results) == 0:
      continue

    result = set(results[0])
    for s in results[1:]:
        result.intersection_update(s)
    
    for i in result:
      print(i)
    
    continue


  try:
    for key in keywords[query]:
      print(key)

  except:
    print("not found")