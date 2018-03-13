check = True
str = email
perv = int(str.find("@"))
perva = int(str.rfind("@"))
if (perva > perv) or perv == -1:
    check = False
sec = int(str.find("."))
seca = int(str.rfind("."))
if (seca > sec) or sec == -1:
    check = False
poln = int(len(str) - 1)
str1 = str[0 - perv]
str2 = str[perv - sec]
str3 = str[sec - poln]
if (str1.isalnum() == True) and (str2.isalnum() == True) and (str3.isalnum() == True) and ( check == True):
    alfa = True
else:
    alfa = False
return(alfa)