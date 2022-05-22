class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for r in magazine:
            ransomNote = ransomNote.replace(r, "", 1)
            if ransomNote == "":
                return True
        return False
