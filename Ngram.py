from collections import Counter,namedtuple
import dill
import random

class Ngram():
    def __init__(self,train_data:list=[],N:int=2) -> None:
        self.train_data=train_data
        self.N=N 
        self.ngram_table=dict()
        self.Word = namedtuple('Word',['word','probability'])
        self.count_prewords=dict() #分母
        self.count_nextwords=dict()#分子

    def _count_word(self,_data:list):
        total_nextwords=list()
        total_prewords=list()
        for _document in _data:
            for i in range(len(_document)-self.N+2):
                total_prewords.append(tuple(_document[i:i+self.N-1]))
            for i in range(len(_document)-self.N+1):
                total_nextwords.append(tuple(_document[i:i+self.N]))
        return {"total_nextwords":total_nextwords,"total_prewords":total_prewords}

    def _update_ngram_table(self):
        for _key in self.count_nextwords:
            text = ''.join(_key[:self.N-1])
            if text not in self.ngram_table:
                self.ngram_table[text]=set()
            nextword_probability = self.count_nextwords[_key]/self.count_prewords[_key[:self.N-1]]
            self.ngram_table[text]=set(self.ngram_table[text])
            self.ngram_table[text].add(self.Word(_key[-1],f'{nextword_probability:.3g}'))
        
    def _sorted_ngram_table(self):
        for _word,_ in self.ngram_table.items():
            self.ngram_table[_word]=sorted(self.ngram_table[_word],key = lambda w:w.probability,reverse=True)

    def generate(self):
        _word_counter = self._count_word(self.train_data)
        total_nextwords=_word_counter["total_nextwords"]
        total_prewords=_word_counter["total_prewords"]
        self.count_prewords = Counter(total_prewords)
        self.count_nextwords = Counter(total_nextwords)
        self.ngram_table=dict()
        self._update_ngram_table()
        self._sorted_ngram_table()

    def update(self,update_data:list):
        self.train_data.extend(update_data)
        _word_counter = self._count_word(update_data)
        total_nextwords=_word_counter["total_nextwords"]
        total_prewords=_word_counter["total_prewords"]
        self.count_prewords = Counter(self.count_prewords) + Counter(total_prewords)
        self.count_nextwords = Counter(self.count_nextwords)+Counter(total_nextwords)
        self.ngram_table=dict()
        self._update_ngram_table()
        self._sorted_ngram_table()
            

    def save(self,name:str='ngrammodel',location:str=''):
        _name=name+'.pkl'
        with open(location+"/"+_name,'wb') as f:
            dill.dump({
                "ngram_table":self.ngram_table,
                "N":self.N,
                "train_data":self.train_data,
                "count_prewords":self.count_prewords,
                "count_nextwords":self.count_nextwords
                },f)

    def load(self,name:str='ngrammodel',location:str=''):
        _name=name+'.pkl'
        with open(location+"/"+_name, 'rb') as f:
            _data = dill.load(f)
            self.ngram_table = _data["ngram_table"]
            self.N = _data["N"]
            self.train_data = _data["train_data"]
            self.count_prewords=_data["count_prewords"]
            self.count_nextwords=_data["count_nextwords"]

    def predict_detail(self,word:str,number:int=5)->list:
        return self.ngram_table.get(word)[:number]

    def predict(self,word)->str:
        _prediction = self.ngram_table.get(word)
        if _prediction:
            return self.ngram_table[word][0].word
        else:
            return random.choice(random.choice(self.train_data))
