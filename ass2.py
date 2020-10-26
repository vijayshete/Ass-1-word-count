import os
tex=open('text.txt','r')

line=0
word=0
char=0
v=0
vowels="AaEeIiOoUu"
for w in tex:
    li=w.strip("\n")
    vowels_c=[vowe for vowe in li if vowe in vowels ]
    v=v+len(vowels_c)
    line+=1
    wor=w.split()
    word+=len(wor)
    ch=len(w)


print(f"no of line in file: {line}")
print(f"no of  words in file: {word}")
print(f"no of character in file: {ch}")
print(f"no of vowels in file: {v}")
