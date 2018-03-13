glassn = ("a", 'e', 'i', 'o', 'u', 'y')
soglasn = ("b", 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',  'n', 'p', 'r', 's', 't', 'v', 'w', 'x', 'z', "q")
s = s.lower()
numstrip = []
deck = []
otv = 0
s = s.replace('...', " ")
s = s.replace('.', " ")
s = s.replace(',', " ")
s = s.replace(';', " ")
s = s.replace(':', " ")
s = s.replace('!', " ")
s = s.replace('?', " ")
s = s.replace('-', " ")
lent = len(s)
if lent > 1 and (s[lent - 1] in glassn or s[lent - 1] in soglasn):
    s = s + " "
    lent = len(s)
if lent > 1 and (s[0] in glassn or s[0] in soglasn):
    s = " " + s
    lent = len(s)
if lent > 1:
    i = 0
    f = 0
    while i < lent:
        if s[i] == " ":
            numstrip.insert(f, str(i))
            f += 1
        i += 1
elif lent <= 1:
    otv = 0
    return(otv)
    raise SystemExit
i = 0
t = 0
lenth = len(numstrip)
while i < (lenth - 1):
    if len(s[(int(numstrip[i]) + 1): int(numstrip[i + 1])]) > 1:
        deck.insert(t, s[(int(numstrip[i])+ 1): int(numstrip[i + 1])])
    i += 1
    t += 1
lenth = len(deck)
i = 0
t = 0
m = 0
while i < (lenth):
    str1 = deck[i]
    lent = len(str1)
    while t < lent - 1:
        if (str1[t] in glassn and str1[t+1] in soglasn) or (str1[t] in soglasn and str1[t+1] in glassn):
          m += 1
        t += 1
    i += 1
    if m == lent - 1:
        otv += 1
    t = 0
    m = 0
return(otv)