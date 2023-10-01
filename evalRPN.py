class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops=set()
        ops.add("+")
        ops.add("*")
        ops.add("-")
        ops.add("/")
        operands = []
        for i in tokens:
            if i in ops:
                op2=operands.pop()
                op1=operands.pop()
                op=i
                if op=="*":
                    op1*=op2
                elif op=="+":
                    op1+=op2
                elif op=="-":
                    op1-=op2
                else:
                    op1/=op2
                    op1=int(op1)
                operands.append(op1)
            else:
                operands.append(int(i))
        return operands.pop()
