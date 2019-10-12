
alpha = "abcdefghijklmnoprstuvwxyz"
step=1
text = input("Text:").strip()
res = ''
for c in text:
    res += alpha[(alpha.index(c) + step)%len(alpha)]
print('Result :"'+ res + '"')