class MyNumbers:
    def __iter__(self):
        self.a = 2
        return self

    def __next__(self):
        x = self.a
        self.a += 2
        if (self.a < 11):
            return x
        else:
            StopIteration


mynumber = MyNumbers()
inumber = iter(mynumber)

print(next(inumber))
print(next(inumber))
print(next(inumber))
print(next(inumber))
print(next(inumber))