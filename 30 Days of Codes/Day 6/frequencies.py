import pprint as pp

text = "I am shimul Mahmud. I am from Bangladesh"

freq = {}

for i in text:
    freq.setdefault(i,0)
    freq[i] = freq[i]+1

pp.pprint(freq)