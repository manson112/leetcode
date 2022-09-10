class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def getBadIndices(word: str):
            print(word)
            result = []
            for i, w in enumerate(word):
                if (w.isupper() and w.lower() in word) or (w.islower() and w.upper() in word):
                    continue
                else:
                    result += [i]
            return result
            
        
        
        def find(s: str):
            print()
            if len(s) < 2:
                return ""
            badIndices = [-1] + getBadIndices(s) + [len(s)]
            if len(badIndices) == 2:
                return s

            print("s:", s)
            print("bad:", badIndices)
            result = ""
            maxLen = 0
            for i in range(1, len(badIndices)):
                if badIndices[i] - badIndices[i-1]-1 < 2:
                    continue
                b = getBadIndices(s[badIndices[i-1]+1:badIndices[i]])
                print("b:",b)
                if len(b) == 0 and badIndices[i]-badIndices[i-1]+1 > maxLen:
                    maxLen = badIndices[i] - badIndices[i-1] + 1
                    result = s[badIndices[i-1]+1:badIndices[i]]
                    print("   found:", result)
                else:
                    ff = find(s[badIndices[i-1]+1:badIndices[i]])
                    if len(ff) > maxLen:
                        result = ff
                        maxLen = len(ff)
                
            return result
        
        return find(s)
        
        