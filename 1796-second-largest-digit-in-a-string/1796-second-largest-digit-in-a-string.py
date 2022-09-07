class Solution:
    def secondHighest(self, s: str) -> int:
        s = sorted(set(list(re.sub(r'[a-z]', " ", s).strip())))
        return -1 if len(s) < 2 else s[-2]
    
