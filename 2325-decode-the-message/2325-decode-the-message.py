class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dict = {' ': ' '}
        chrNum = ord('a')
        for k in key:
            if dict.get(k) == None:
                dict[k] = chr(chrNum)
                chrNum += 1
        result = ""
        for msg in message:
            result += dict[msg]
        return result