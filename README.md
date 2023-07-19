# N_Gram

## index


````
│   README.md               說明書
│   Ngram.py                Ngram object    
│   Ngram_news.py           demo python script
|   WebNews.json            demo data(from:https://data.gov.tw/dataset/25891) 
````

## requirment
Python
```
Python 3.10.8
```

pip
```
dill                         0.3.6
```

## usage
creat a N_Gram object
```
testmodel = Ngram(train_data,N)
```

load model
```
testmodel = Ngram()
testmodel.load(file_name,path)
```

## method
```
Name: generate
function: generate n_gram table
input: -
output: -
```
```
Name: update
function: update n_gram table
input: update data
output: -
```
```
Name: save
function: save n_gram table
input: file name, save path
output: -
```
```
Name: load
function: load n_gram table
input: file name, save path
output: -
```
```
Name: predict_detail
function: use n_gram table to predict next word, return posible words and their posibility
input: word,n(how many posible words return)
output: a list of posible words and their posibility, if word not in n_gram table will return None
```
```
Name: predict
function: use n_gram table to predict next word
input: word
output: posible next word, if word not in n_gram table will return a random word
```