class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        book={}
        for num in arr:
            book[num]=book.get(num,0)+1
        uniques=set()
        for num, freq in book.items():
            if freq in uniques:
                return False
            uniques.add(freq)
        return True
        
