'''
Example of Composite Design Pattern
     -
    / \
   /   \
  12    +
       / \
      /   \
     4     6
'''
op = {
        '+': lambda a, b: a+b,
        '-': lambda a, b: a-b
    }

from abc import ABCMeta, abstractmethod

class ExpType(metaclass=ABCMeta):
    @abstractmethod
    def evaluate(self):
        pass

class Exp(ExpType):
    def __init__(self, op: str, left: ExpType = None, right: ExpType = None) -> None:
        self.left = left
        self.right = right
        self.op = op

    def evaluate(self):
        return super().evaluate()
    
    def solve(self) -> int:
        r1 = self.left.solve() if self.left else 0
        r2 = self.right.solve() if self.right else 0
        if self.op in ['+', '-']:
            return op[self.op](r1, r2)
        return int(self.op)

    def __str__(self) -> str:
        return f'{self.left if self.left else ""} {self.op} {self.right if self.right else ""}'

        

if __name__=="__main__":
    exp = ['12','4','6','+','-']
    res = 0
    stack = []
    for opr in exp:
        if opr not in op:
            stack.append(Exp(opr))
        else:
            R, L = stack.pop(), stack.pop()
            stack.append(Exp(opr, L, R))
    
    res = stack.pop()
    print(res)
    print(res.solve())

