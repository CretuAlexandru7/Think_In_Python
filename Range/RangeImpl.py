# Short explanation of for
# x = [1, 2, 3]
#
# it = iter(x)
#
# while True:
#     try:
#         y = next(it)
#     except:
#         print("stop")
#         break
#     else:
#         print(y)

from collections.abc import Iterator


class Range:
    def __init__(self, stop: int):
        self.start = 0
        self.stop = stop

    # Function annotation: the -> marks the return function annotation.
    # More Info: https://stackoverflow.com/questions/14379753/what-does-mean-in-python-function-definitions
    def __iter__(self) -> Iterator[int]:
        curr = self.start

        while curr < self.stop:
            yield curr
            curr += 1

def range_example():
    for i in Range(7):
        print(i)

range_example()

