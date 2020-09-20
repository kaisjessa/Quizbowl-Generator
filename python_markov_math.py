#https://towardsdatascience.com/simulating-text-with-markov-chains-in-python-1a27e6d13fc6
import numpy as np
text1 = open('quizbowl_math_tossups2.txt', encoding='utf8').read()
text2 = open('quizbowl_math_answers2.txt', encoding='utf8').read()

corpus = text1.split(" ")
corpus2 = []
for word in corpus:
	if '&' not in word:
		corpus2.append(word)
corpus=corpus2
#print(sorted(list(set(corpus))))
def make_pairs(corpus):
	for i in range(len(corpus)-1):
		yield (corpus[i], corpus[i+1])
		
pairs = make_pairs(corpus)

tu_dict = {}
for word_1, word_2 in pairs:
	if word_1 in tu_dict.keys():
		tu_dict[word_1].append(word_2)
	else:
		tu_dict[word_1] = [word_2]

corpus = text2.split(" ")
corpus2 = []
for word in corpus:
	if '&' not in word:
		corpus2.append(word)
corpus=corpus2
#print(sorted(list(set(corpus))))
def make_pairs(corpus):
	for i in range(len(corpus)-1):
		yield (corpus[i], corpus[i+1])
		
pairs = make_pairs(corpus)

an_dict = {}
for word_1, word_2 in pairs:
	if word_1 in an_dict.keys():
		an_dict[word_1].append(word_2)
	else:
		an_dict[word_1] = [word_2]

#first_word = np.random.choice(corpus)
# Generate tossup, ftp, answer
first_word = "TOSSUP:"
chain = [first_word]
n_words = 1000
after_this = ""
for i in range(n_words):
	if(chain[-1].lower() == "this" and after_this == ""):
		after_this = np.random.choice(tu_dict[chain[-1]])
		chain.append(after_this)
		#print("AFTER_THIS: " + after_this)
	elif(chain[-1].lower() == "this" and after_this != ""):
		chain.append(after_this)
	else:
		chain.append(np.random.choice(tu_dict[chain[-1]]))
tu = ' '.join(chain)
chain = ["For", "10", "points,"]
n_words = 100
for i in range(n_words):
	if(chain[-1].lower() == "this" and after_this == ""):
		after_this = np.random.choice(ftp_dict[chain[-1]])
		chain.append(after_this)
		#print("AFTER_THIS: " + after_this)
	elif(chain[-1].lower() == "this" and after_this != ""):
		chain.append(after_this)
	else:
		chain.append(np.random.choice(tu_dict[chain[-1]]))

ftp = ' '.join(chain)
first_word = "ANSWER:"
chain = [first_word]
n_words = 100
for i in range(n_words):
	chain.append(np.random.choice(an_dict[chain[-1]]))
an = ' '.join(chain[1:])
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
tu2 = ' '.join(tu2.split()) # format whitespace


ftp_list = ftp[len("For 10 points, "):].split('.')
ftp_list2 = []
for t in ftp_list:
	if("TOSSUP:" not in t and "ANSWER:" not in t and "For 10 points" not in t and '[' not in t and ']' not in t and len(t)>50):
		ftp_list2.append(t)
if(len(ftp_list2)==0):
	ftp_list2 = ['']
ftp2 = "For 10 points, " + ftp_list2[0] + '.'
ftp2 = ' '.join(ftp2.split()) # format whitespace

def fix_brackets(s):
	count = 0
	st = ""
	for c in s:
		if c == '[' and count == 0:
			count += 1
		elif c == '[' and count > 0:
			return([count, st])
		st += c
	return([count, st])

# an_list = an[len("ANSWER: "):].split('.')
# an_list2 = []
# for t in an_list:
# 	if("TOSSUP:" not in t and "ANSWER:" not in t and "For 10 points" not in t and len(t)>50):
# 		an_list2.append(t)
# if(len(an_list2)==0):
# 	an_list2 = ['']
# an2 = "\nANSWER: " + an_list2[0] + '.'
# if('[' in an2 and ']' not in an2):
# 	an2 += ']'

an2 = an[:an.find("ANSWER:")-2]
l = fix_brackets(an2)
an2 = l[1].replace('(','').replace(')','')
co = l[0]
if(co > 0 and ']' not in an2):
	if(an2[-1] == ' '):
		an2 = an2[:-1]
	an2 += ']'
if(']' in an2 and co == 0):
	an2 = an2.replace(']','')
an2 = "ANSWER: " + an2
if(']' in an2):
	an2 = an2[:an2.find(']')+1]
an2 = ' '.join(an2.split()) # format whitespace
# Output
print(tu2, ftp2)
print(an2)