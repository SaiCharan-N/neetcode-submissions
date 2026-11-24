class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for s in strs:
            for c in s:
                a=chr(ord(c)+1)
                encoded+=a
            encoded+=' '
        return encoded
    def decode(self, s: str) -> List[str]:
        l=[]
        a=''
        for c in s:
            if c==' ':
                l.append(a)
                a=''
            else:
                a+=chr(ord(c)-1)
        return l