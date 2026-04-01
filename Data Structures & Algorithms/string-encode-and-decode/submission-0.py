class Solution:

    def __init__(self):
        self.ed_dict = defaultdict(list)

    def encode(self, strs: List[str]) -> str:

        self.ed_dict["word"] = tuple(strs)
        return "word"

    def decode(self, s: str) -> List[str]:
        return list(self.ed_dict["word"])