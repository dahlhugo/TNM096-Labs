from array import array
from dataclasses import dataclass


@dataclass
class Node:
    state: list[int]
    cost: int


def main():
    k = 0
    node1 = Node([1, 2, 3], 1)

    print(node1.state)


main()
