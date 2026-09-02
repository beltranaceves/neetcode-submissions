class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return None
        return "ñ".join(strs)

    def decode(self, s: str) -> List[str]:
        if s is None:
            return []
        return s.split("ñ")
