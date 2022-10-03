class Solution:
    def interpret(self, command: str) -> str:
        goal = {"G": "G", "()": "o", "(al)": "al"}
        result = ""
        s = ""
        for c in command:
            s += c
            if goal.get(s) != None:
                result += goal[s]
                s = ""
        return result
