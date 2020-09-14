import markovify

# Get raw text as string.
with open("quizbowl.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text, state_size=3, well_formed = True)

# Print five randomly-generated sentences
for i in range(10):
    print(text_model.make_sentence())

#Print three randomly-generated sentences of no more than 280 characters
# for i in range(10):
#     print(text_model.make_short_sentence(5000))