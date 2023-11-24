class OddIterator:
    def __init__(self, container) -> None:
        self.container = container
        self.n = -1
    
    def __next__(self):
        self.n += 2
        if self.n > self.container.maxim:
            raise StopIteration
        return self.n

    def __iter__(self):
        return self

class OddNumbers:
    def __init__(self, maxim) -> None:
        self.maxim = maxim
    
    def __iter__(self):
        return OddIterator(self)

class FibonacciIterator:
    def __init__(self, container) -> None:
        self.container = container
        self.n1 = 0
        self.n2 = 1
        self.count = 0
    
    def __next__(self):
        self.n1, self.n2 = self.n2, self.n1 + self.n2
        self.count += 1
        if self.count > self.container.maxim:
            raise StopIteration
        return self.n2

    def __iter__(self):
        return self

class FibonacciNumbers:
    def __init__(self, maxim) -> None:
        self.maxim = maxim
    
    def __iter__(self):
        return FibonacciIterator(self)

class SquareIterator:
    def __init__(self, obj):
        self.obj = obj
        self.n = 0
    
    def __next__(self):
        res = self.n * self.n
        self.n += 1
        if self.n > self.obj.max:
            raise StopIteration
        return res

    def __iter__(self):
        return self


class Squares:
    def __init__(self, n):
        self.max = n
    
    def __iter__(self):
        return SquareIterator(self)


def squares(num):
    i = 0
    while i < num:
        yield i*i
        i+=1

class Sentence:
    def __init__(self, sentence) -> None:
        self.sentence = sentence.split()
        self.pos = 0
    
    def __next__(self):
        self.pos += 1
        try:
            return self.sentence[self.pos - 1]
        except IndexError:
            raise StopIteration

    def __iter__(self):
        return self

def sentence_genr(sentence):
    i = 0
    n = len(sentence)
    while i < n:
        word = ""
        while i<n and sentence[i]!=" ":
            word += sentence[i]
            i+=1
        yield word
        i+=1


if __name__=="__main__":
    '''Driver code goes here'''
    # sq_iter = iter(Squares(10))
    # for num in sq_iter:
    #     print(num)
    test = "India will win MCWC2023"
    sentence = Sentence(test)
    sengen = sentence_genr(test)
    print(sentence.__dict__)
    for word in sengen:
        print(word)