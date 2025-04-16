class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        size1=len(word1)
        size2=len(word2)
        if size1!=size2:
            return False
        chars1={}
        chars2={}
        for i in range(size1):
            chars1[word1[i]]=chars1.get(word1[i],0)+1
            chars2[word2[i]]=chars2.get(word2[i],0)+1
        for char in chars1.keys():
            if char not in chars2:
                return False
        if sorted(chars1.values())!=sorted(chars2.values()):
            return False
        return True
