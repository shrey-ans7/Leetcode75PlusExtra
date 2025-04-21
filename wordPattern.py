class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split(" ")
        if len(s)!=len(pattern):
            return False
        mapping={}
        visited=set()
        for char,word in zip(pattern,s):
            if char not in mapping and word not in visited:
                mapping[char]=word
                visited.add(word)
            elif mapping.get(char,None)==word:
                continue
            else:
                return False
            
        return True
        
