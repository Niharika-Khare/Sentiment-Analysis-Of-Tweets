from porter_stemmer import PorterStemmer

def tokenize(str):
    return str.split(" ")

def stemming(list_of_tokens):
    ps = PorterStemmer()
    # for word in list_of_tokens:
    #     print word,
    #     print ps.stem(word)
    return [ ps.stem(word) for word in list_of_tokens ] 


sample_tweet = '''
@sonamakapoor  its because of people like you who dont use public transport or less fuel consumption vehicles You Know that your luxury car gives 3 or 4 km per litre mileage and  10 20 ACs in your house are equally responsible for global warming First control your pollution
'''

# ps = PorterStemmer()
# print ps.stem("running")

tokens = tokenize(sample_tweet)
print tokens

stemmed = stemming(tokens)
print stemmed