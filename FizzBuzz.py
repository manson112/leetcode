class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                arr += ["FizzBuzz"]
            elif i % 3 == 0:
                arr += ["Fizz"]
            elif i % 5 == 0:
                arr += ["Buzz"]
            else:
                arr += [str(i)]
        return arr