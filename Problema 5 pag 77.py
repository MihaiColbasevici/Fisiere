with open('C:Desktop\input.txt', 'r') as f:
    l = list(f.read())
vocale = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
voc = 0
for ch in l:
    if ch in vocale:
        voc += 1
print(voc, 'vocale')