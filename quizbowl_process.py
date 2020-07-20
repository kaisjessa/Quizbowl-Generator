with open('quizbowl_raw.txt', encoding='utf_8') as f1:
	with open('quizbowl.txt', 'w', encoding='utf_8') as f2:
		for line in f1:
			if("TOSSUP:" in line or "ANSWER:" in line):
				f2.write(line)
				f2.write('\n')