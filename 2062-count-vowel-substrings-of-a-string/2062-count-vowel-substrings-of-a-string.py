class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        word = 'z' + word + 'z'
        vowels = ['a', 'e', 'i', 'o', 'u']
        nonV = 0
        v = []
        for i in range(1, len(word)):
            if word[i] not in vowels:
                if i - nonV >= 5 and len(set(word[nonV+1:i])) == 5:
                    v += [word[nonV+1:i]]
                nonV = i
        result = 0
        for vword in v:
            for i in range(len(word)-5):
                s = set()
                for j in range(5, len(word)):
                    if len(set(vword[i:i+j])) == 5:
                        s.add(vword[i:i+j])
                result += len(s)
        return result
