import unicodedata

def strip_accents(text):

    try:
        text = unicode(text, 'utf-8')
    except NameError: # unicode is a default on python 3 
        pass

    text = unicodedata.normalize('NFD', text)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")
    text = text.replace('\n', ' ').replace('\r', '')
    return str(text)

with open('quizbowl_math2.txt', encoding='utf_8') as f1:
	with open('quizbowl_math3.txt', 'w', encoding='utf_8') as f2:
		for line in f1:
			f2.write(strip_accents(line))