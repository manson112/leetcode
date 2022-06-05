class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        mmap = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        
        def getSeq(i:int, mmap:List[str], digits:List[str]):
            if i < 0:
                return ['']
            lhs = getSeq(i-1, mmap, digits)
            ans = []
            for l in lhs:
                for r in mmap[int(digits[i])-2]:
                    ans.append(l+r)
            return ans
        
        return getSeq(len(digits)-1, mmap, digits)