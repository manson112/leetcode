class Solution:
    def countValidWords(self, sentence: str) -> int:
        result = 0
        sentences = sentence.split(" ")
        for sentence in sentences:
            if len(sentence) < 1:
                continue
            valid = True
            hypen = False
            punct = False
            for i, s in enumerate(sentence):
                if not ((ord(s) >= 97 and ord(s) <=122) or s == "-" or s == "!" or s == "." or s == ","):
                    valid = False
                    break
                if s == "-":
                    if hypen:
                        valid = False
                        break
                    if i == 0 or i == len(sentence)-1:
                        valid = False
                        break
                    if not ((ord(sentence[i-1]) in range(97, 123)) and (ord(sentence[i+1]) in range(97, 123))):
                        valid = False
                        break
                    hypen = True
                    
                if s == "!" or s == "." or s == ",":
                    if punct:
                        valid = False
                        break
                    if i != len(sentence)-1:
                        valid = False
                        break
                    punct = True
                    
            if valid:
                result += 1
        return result
            
            