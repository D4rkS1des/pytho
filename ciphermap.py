squad1 = " "
cryp = ['X...', '..X.', 'X..X', '....']
passwd = ['itdf', 'gdce', 'aton', 'qrdi']
otv = ""
i = 0
n = 0
str1 = cryp[0]
str2 = cryp[1]
str3 = cryp[2]
str4 = cryp[3]
squad1 = (str1 + str2 + str3 + str4)
squad2 = (str4[0] + str3[0] + str2[0] + str1[0] + str4[1] + str3[1]+ str2[1] + str1[1] + str4[2] + str3[2] + str2[2] + str1[2] + str4[3] + str3[3] + str2[3] + str1[3])
squad3 = (str4[3] + str4[2] + str4[1] + str4[0] + str3[3] + str3[2] + str3[1] + str3[0] + str2[3] + str2[2] + str2[1] + str2[0] + str1[3] + str1[2] + str1[1] + str1[0])
squad4 = (str1[3] + str2[3] + str3[3] + str4[3] + str1[2] + str2[2] + str3[2] + str4[2] + str1[1] + str2[1] + str3[1] + str4[1] + str1[0] + str2[0] + str3[0] + str4[0])
#print(squad1)
#print(squad2)
#print(squad3)
#print(squad4)
pwd = (passwd[0] + passwd[1] + passwd[2] +passwd[3])
print(pwd)
while i < 4:
    while n < 16:
        if i == 0 and squad1[n] == "X":
            otv = otv + pwd[n]
        if i == 1 and squad2[n] == "X":
            otv = otv + pwd[n]
        if i == 2 and squad3[n] == "X":
            otv = otv + pwd[n]
        if i == 3 and squad4[n] == "X":
            otv = otv + pwd[n]
        n = n + 1
    i = i + 1
    n = 0
print(otv)
