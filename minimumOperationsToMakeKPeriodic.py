class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        sub_words={}
        size=len(word)
        i=0
        for j in range(size):
            if j%k==0:
                sub_words[word[i:j]]=sub_words.get(word[i:j],0)+1
                i=j
        sub_words[word[i:size]]=sub_words.get(word[i:size],0)+1
        most_freq=0
        for sub_word, count in sub_words.items():
            if most_freq<count:
                most_freq=count
        return size//k-most_freq


        
