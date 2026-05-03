class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for i in strs:
            encoded.append(str(len(i)))
            encoded.append('#')
            encoded.append(i)
        final_encoded = "".join(encoded)
        return final_encoded
    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j +=1
            length = int(s[i:j])
            j+=1
            word = s[j:j+length] 
            decoded.append(word)
            i = j+length
        return decoded
