import json
import re
import os
from Ngram import Ngram

path = os.path.dirname(os.path.abspath(__file__))
DATA_sorce = path+'/WebNews.json'

with open(DATA_sorce,encoding='utf8') as file:
    text_data_unprocess=json.load(file) 
    text_data=[]
    for i in text_data_unprocess:
        text_filter = re.compile(r"[^\u4e00-\u9fa5]")
        text_data.append(re.sub(text_filter,"",i['detailcontent'])) 


# trigram_model=Ngram(text_data,3)
# trigram_model.generate()
# trigram_model.save("news",path)

trigram_model = Ngram()
trigram_model.load("news",path)


word = "早安"
print(word,end='')
for i in range(100):
    _w = trigram_model.predict(word)
    word = word[:-1]+ _w
    print(_w,end="")


