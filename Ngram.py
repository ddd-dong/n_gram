from collections import Counter,namedtuple
import dill
import random

class Ngram():
    def __init__(self,train_data:list=[],N:int=2) -> None:
        self.train_data=train_data
        self.N=N
        self.ngram_table=dict()
        self.Word = namedtuple('Word',['word','probability'])

    def generate(self):
        total_nextwords=list()
        total_prewords=list()
        for _document in self.train_data:
            for i in range(len(_document)-self.N+2):
                total_prewords.append(tuple(_document[i:i+self.N-1]))
            for i in range(len(_document)-self.N+1):
                total_nextwords.append(tuple(_document[i:i+self.N]))
        
        count_prewords = Counter(total_prewords)
        count_nextwords = Counter(total_nextwords)
        for _key in count_nextwords:
            text = ''.join(_key[:self.N-1])
            if text not in self.ngram_table:
                self.ngram_table[text]=set()
            nextword_probability = count_nextwords[_key]/count_prewords[_key[:self.N-1]]
            self.ngram_table[text].add(self.Word(_key[-1],f'{nextword_probability:.3g}'))
        for _word,_ in self.ngram_table.items():
            self.ngram_table[_word]=sorted(self.ngram_table[_word],key = lambda w:w.probability,reverse=True)

    def save(self,name:str='ngrammodel',location:str=''):
        _name=name+'.pkl'
        with open(location+"/"+_name,'wb') as f:
            dill.dump({"ngram_table":self.ngram_table,"N":self.N,"train_data":self.train_data},f)

    def load(self,name:str='ngrammodel',location:str=''):
        _name=name+'.pkl'
        with open(location+"/"+_name, 'rb') as f:
            _data = dill.load(f)
            self.ngram_table = _data["ngram_table"]
            self.N = _data["N"]
            self.train_data = _data["train_data"]

    def predict_detail(self,word:str,number:int=5):
        return self.ngram_table.get(word)[:number]

    def predict(self,word):
        _prediction = self.ngram_table.get(word)
        if _prediction:
            return self.ngram_table[word][0].word
        else:
            return random.choice(random.choice(self.train_data))
