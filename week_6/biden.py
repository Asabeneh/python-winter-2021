import re

with open('./files/biden_speech.txt', encoding='utf-8') as f:
    cleaned_text = re.sub(r'[^A-Za-z ]', ' ', f.read())
    words = cleaned_text.split(' ')
    real_words = [word  for word in words if word !='']
    print(len(real_words))


# Lexical variety/density
# What were the 10 month frequent words used in this inaguration speech ?
  