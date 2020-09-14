#https://towardsdatascience.com/simulating-text-with-markov-chains-in-python-1a27e6d13fc6
import numpy as np
text = open('quizbowl_no_accents.txt', encoding='utf8').read()

corpus = text.split(" ")
for word in corpus:
	if word.startswith('&'):
		corpus.remove(word)
#print(sorted(list(set(corpus))))

def make_pairs(corpus):
    for i in range(len(corpus)-1):
        yield (corpus[i], corpus[i+1])
        
pairs = make_pairs(corpus)

word_dict = {}
for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

#first_word = np.random.choice(corpus)
first_word = "TOSSUP:"
chain = [first_word]
n_words = 200

for i in range(n_words):
    chain.append(np.random.choice(word_dict[chain[-1]]))

tu = ' '.join(chain)

chain = ["For", "10", "points,"]
n_words = 20

for i in range(n_words):
    chain.append(np.random.choice(word_dict[chain[-1]]))

ftp = ' '.join(chain)

first_word = "ANSWER:"
chain = [first_word]
n_words = 20

for i in range(n_words):
    chain.append(np.random.choice(word_dict[chain[-1]]))

an = ' '.join(chain)
tu = tu[:min(len(tu)-1, tu.rfind('.'), tu[1:].find('TOSSUP:'), tu.find('ANSWER:'), tu.find('For 10 points,'))]
ftp = ftp[:min(ftp.rfind('.'), ftp.find('TOSSUP:'), ftp.find('ANSWER:'))]
an = an[:min(an.rfind('.'), an.find('TOSSUP:'), an[1:].find('ANSWER:'))]

print(tu)
print(ftp)
print(an)