class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        str_list = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                str_list.append("FizzBuzz")
            elif i % 3 == 0:
                str_list.append("Fizz")
            elif i % 5 == 0:
                str_list.append("Buzz")
            else:
                str_list.append(str(i))
        return str_list
