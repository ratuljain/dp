import string

def histo(t):
    alpha = t[0]
    num = t[1]
    s = ""
    for i in range(num):
        s += "*" + '\n'
    lis = list(s)
    lis.append(alpha)
    print ''.join(lis)

with open ("test.txt", "r") as myfile:
    s=myfile.read().replace('\n', '')
s.translate(None, string.punctuation)
d = {}
for letters in s:
    d.update({letters : s.count(letters)})
l =  d.items()
# for i in range(len(l)):
#     print histo(l[i]),

histo(l[2]),
histo(l[2]),
histo(l[2]),

