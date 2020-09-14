#https://towardsdatascience.com/simulating-text-with-markov-chains-in-python-1a27e6d13fc6
import numpy as np
text = open('quizbowl_no_accents.txt', encoding='utf8').read()

corpus = text.split(" ")
for word in corpus:
	if '&' in word:
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
# Generate tossup, ftp, answer
first_word = "TOSSUP:"
chain = [first_word]
n_words = 1000
for i in range(n_words):
    chain.append(np.random.choice(word_dict[chain[-1]]))
tu = ' '.join(chain)
chain = ["For", "10", "points,"]
n_words = 100
for i in range(n_words):
    chain.append(np.random.choice(word_dict[chain[-1]]))

ftp = ' '.join(chain)
first_word = "ANSWER:"
chain = [first_word]
n_words = 100
for i in range(n_words):
    chain.append(np.random.choice(word_dict[chain[-1]]))
an = ' '.join(chain)
# tu = tu[:min(len(tu)-1, tu.rfind('.'), tu[1:].find('TOSSUP:'), tu.find('ANSWER:'), tu.find('For 10 points,'))]
# ftp = ftp[:min(ftp.rfind('.'), ftp.find('TOSSUP:'), ftp.find('ANSWER:'))]
# an = an[:min(an.rfind('.'), an.find('TOSSUP:'), an[1:].find('ANSWER:'))]

# Format tossup, ftp, answer
tu_list = tu[len("TOSSUP: "):].split('.')
tu_list2 = []
for t in tu_list:
	if("TOSSUP:" not in t and "ANSWER:" not in t and "For 10 points" not in t and '[' not in t and ']' not in t and len(t)>50):
		tu_list2.append(t)
tu_list2 = tu_list2[:min(len(tu_list2)-1, 4)]
tu2 = "TOSSUP: " + '.'.join(tu_list2) + '.'


ftp_list = ftp[len("For 10 points, "):].split('.')
ftp_list2 = []
for t in ftp_list:
	if("TOSSUP:" not in t and "ANSWER:" not in t and "For 10 points" not in t and '[' not in t and ']' not in t and len(t)>50):
		ftp_list2.append(t)
ftp_list2 = ftp_list2[:min(len(ftp_list2)-1, 1)]
ftp2 = "For 10 points, " + '.'.join(ftp_list2) + '.'


an_list = an[len("ANSWER: "):].split('.')
an_list2 = []
for t in an_list:
	if("TOSSUP:" not in t and "ANSWER:" not in t and "For 10 points" not in t and len(t)>50):
		an_list2.append(t)
if(len(an_list2)==0):
	an_list2 = ['']
an2 = "\nANSWER: " + an_list2[0] + '.'
if('[' in an2 and ']' not in an2):
	an2 += ']'

# Output
print(tu2, ftp2)
print(an2)