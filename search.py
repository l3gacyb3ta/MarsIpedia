import json, spacy, pickle

nlp = spacy.load("en_core_web_sm")


with open('data/first.pic', 'rb') as f:
  first = pickle.load(f)

with open('data/second.pic', 'rb') as f2:
  second = pickle.load(f2)

with open('data/third.pic', 'rb') as f3:
  third = pickle.load(f3)

with open('data/fourth.pic', 'rb') as f4:
  fourth = pickle.load(f4)

# with open('data/second.pic', 'rb') as f2:
#   second = pickle.load(f2)

keywords = {**first, **second, **third, **fourth}

stop = nlp.Defaults.stop_words

while True:
  query = input("> ").lower()

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