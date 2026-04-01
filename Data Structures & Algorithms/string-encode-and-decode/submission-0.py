class Solution:

    def encode_s(self, s: str) -> str:
        ord_s = ""
        for ch in s:
            if ch == "":
                continue 
            ord_s += str(ord(ch) - ord('a')) + '?'
        return f"#{ord_s}"

    def decode_s(self, s: str) -> str:
        full_s = ""
        arr_s = s.split('?')
        print(arr_s)
        for ch in arr_s:
            if ch == '':
                continue 
            decoded_letter = chr(int(ch) + ord('a'))
            full_s += decoded_letter

        return full_s

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += self.encode_s(s)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        arr_s = s.split("#")[1:]
        for i in range(len(arr_s)):
            arr_s[i] = self.decode_s(arr_s[i])
        return arr_s
        




