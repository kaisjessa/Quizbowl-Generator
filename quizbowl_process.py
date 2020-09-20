with open('quizbowl_music.txt', encoding='utf_8') as f1:
	with open('quizbowl_music_tossups.txt', 'w', encoding='utf_8') as f2:
		for line in f1:
			if("TOSSUP:" in line):
				f2.write(line + '\n')