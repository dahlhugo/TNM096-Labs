from itertools import chain

multi_list = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

flatten_list = list(chain.from_iterable(multi_list))

print(''.join(str(e) for e in flatten_list))

