import re

print(dir(re))
# re.match() => only look for a patter at the beginning of the string 
# re.search -> this look for through out the string and stops when the patter is found
# re.sub -> substitute a patter with any thing
# re.split
# re.findall

txt = 'i Love to teach python and javaScript. if you do not love this what else can you love. '

match = re.match(r'I love', txt, re.I)
print(match.span())

start_index = match.span()[0]
end_index = match.span()[1]
print(start_index, end_index)
start, end = match.span()
print(start, end)
print(txt[start:end])

match = re.search(r'love', txt, re.I)
print(match)

matches =re.findall('love', txt,re.I )
print(matches)

test = re.sub(r'love', 'hate', txt, flags = re.I)
print(test)
print(re.split(r'love', txt, flags=re.I)) 

regex= r'[Aa]pple|[Bb]anana'

txt = 'Apple and banana are fruits. An old cliche says an apple a day keey the  doctor way has been replaced by a banana a day keeps the doctor far far away. '

print(re.findall(regex, txt))

