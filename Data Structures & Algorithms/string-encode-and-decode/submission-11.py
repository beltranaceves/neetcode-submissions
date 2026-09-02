class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += "SEPARADORINCREIBLE" + string
        return encoded_string

    def decode(self, s: str) -> List[str]:
        return s.split("SEPARADORINCREIBLE")[1:]
