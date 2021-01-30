with open('quizbowl_art2.txt', encoding='utf_8') as f1:
	with open('quizbowl_art.txt', 'w', encoding='utf_8') as f2:
		count = 0
		for line in f1:
			if("ANSWER:" in line):
				line = line.replace("ANSWER: ", "")
				line = line + "&"
				line = line[:line.index("&")]
				line = line + '['
				line = line[:line.index('[')]
				line = line + '('
				line = line[:line.index('(')]
				line = line + '\n'
				line = line[:line.index('\n')]
				if(len(line) > 0 and line[-1] == ' '):
					line = line[:-1]
				if(len(line) > 1 and len(line) < 35):
					count += 1
					f2.write(line.replace(': ', '').replace('.', '') + ', ')

print(count)