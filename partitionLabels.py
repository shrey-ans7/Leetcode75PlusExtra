class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        chars = list(s)
        book = {}
        for char in chars:
            if char in book.keys():
                book[char]+=1
            else:
                book[char]=1

        stack = []
        i=0; j=0
        for char in chars:
            i+=1
            book[char]-=1
            if book[char]==0:
                flag = True
                for k in range(j,i):
                    if book[chars[k]]!=0:
                        flag=False
                        break
                if flag:
                    stack.append(i-j)
                    j=i
        # print(book, chars)
        return stack



