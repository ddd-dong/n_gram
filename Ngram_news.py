import json
import re
import os
from Ngram import Ngram

path = os.path.dirname(os.path.abspath(__file__))
DATA_sorce = path+'/WebNews.json'
update_data='''
先斷詞，對於中文語意理解
'''
text_filter = re.compile(r"[^\u4e00-\u9fa5]")
with open(DATA_sorce,encoding='utf8') as file:
    text_data_unprocess=json.load(file) 
    text_data=[]
    for i in text_data_unprocess:
        text_data.append(re.sub(text_filter,"",i['detailcontent'])) 
update_data = [re.sub(text_filter,"",update_data)]

# trigram_model=Ngram(text_data,3)
# trigram_model.generate()
# trigram_model.save("news",path)

trigram_model = Ngram()
trigram_model.load("news",path)
trigram_model.update(update_data)
print(trigram_model.predict_detail("中文"))

# word = "早安"
# print(word,end='')
# for i in range(1000):
#     _w = trigram_model.predict(word)
#     word = word[:-1]+ _w
#     print(_w,end="")


