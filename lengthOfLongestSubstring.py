dic = {}
preIndex = 0
maxLength = 0
s = "abcabcbb"
for i in range(len(s)):
    if dic.get(s[i]) != None:
        if len(dic) >= maxLength:
            maxLength = len(dic)
        
        cutIndex = dic.get(s[i])
        for j in range(preIndex, cutIndex+1):
            dic.pop(s[j])
        
        preIndex = cutIndex + 1
    dic[s[i]] = i
        

print(maxLength)