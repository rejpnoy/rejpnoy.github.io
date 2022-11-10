class Solution:
    def interpret(self, commad: str) -> str:
        return commad.replace("()","o").replace("(al)", "al")