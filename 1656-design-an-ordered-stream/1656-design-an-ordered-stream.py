class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None for _ in range(n+1)]
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        ret = []
        if idKey == self.ptr:
            while idKey < len(self.stream) and self.stream[idKey] != None:
                ret += [self.stream[idKey]]
                idKey += 1
            self.ptr = idKey
        return ret

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)