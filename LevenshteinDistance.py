#!/usr/bin/env python
def LevenshteinDistance(s,t):   #要进行比较的两个字符串s,t
    m,n = len(s),len(t)        #m,n分别为字符串s,t的长度 
    #创建一个二维数组d,d[i][j]表示字符串s的前i位与字符串t的前j位之间的Leventeish Distance
    #注意二维数组的元素个数是(m+1)*(n+1)
    d = [[0 for j in range(n+1)] for i in range(m+1)]  
    for i in range(1,m+1):
        d[i][0] = i
    for j in range(1,n+1):
        d[0][j] = j
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s[i-1] == t[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = min(d[i-1][j]+1,  #t delete a char
                            d[i][j-1]+1,    #t insert a char
                            d[i-1][j-1]+1)  #t substitute a char
    return d[m][n]

############### DEMO ################
#s:WOMAN
#t:WOMEN
s = 'WOMAN'
t = 'WOMEN'
dis = LevenshteinDistance(s,t)
print('Levenshtei Distance:',dis)
