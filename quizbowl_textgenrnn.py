from textgenrnn import textgenrnn

textgen = textgenrnn()
#textgen.train_from_file('quizbowl.txt', num_epochs=1)
textgen.generate()