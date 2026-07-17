class Solution:

    def encode(self, strs: List[str]) -> str:
        newString = ""
        for i in strs:
            newString = newString + i + "<br>"
        return newString

    def decode(self, s: str) -> List[str]:
        temp = s.split("<br>")
        temp.pop(-1)
        return temp