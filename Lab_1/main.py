from itertools import chain
from queue import PriorityQueue
from dataclasses import dataclass, field


@dataclass
class Node:
    state: list[[int]]
    x: int
    y: int
    cost: int
    level: int
    f: int


@dataclass
class PrioritizedItem:
    priority: int
    item: object = field()


def print_state(state):
    for i in range(3):
        for j in range(3):
            print(f"{state[i][j]} ")
        print("\n")


def compare_states(node1, node2):

    for i in range(3):
        for j in range(3):
            if node1.state[i][j] != node2.state[i][j]:
                return False

    return True


def is_node_in_list(node, node_list):
    for i in node_list:
        if compare_states(node, i):
            return True
    return False


def calculate_misplaced_tiles(node1, goal_node):
    count = 0

    for i in range(3):
        for j in range(3):
            if node1.state[i][j] != goal_node.state[i][j]:
                count += 1

    return count


def list_to_key(state):
    flatten_list = list(chain.from_iterable(state))
    result = ''.join(str(e) for e in flatten_list)

    return result

def solver(init_node, goal_node):
    open_list = PriorityQueue()
    closed_list = {}

    initial_node = init_node
    goal_node = goal_node

    initial_node.cost = calculate_misplaced_tiles(initial_node, goal_node)

    open_list.put((initial_node.cost, initial_node))


    counter = 0

    while not open_list.empty():
        min_node = open_list.get()
        closed_list[list_to_key(min_node.state)] = min_node

        if min_node.cost == 0:
            print_path(counter, min_node);
            print("\n Steps: " + str(counter - 1) + "\n")

            return


def main():
    initial_node = Node([
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ], 0, 0, 0, 0, 0)

    goal_node = Node([
        [1, 0, 2],
        [3, 4, 5],
        [6, 7, 8]
    ], 0, 1, 0, 0, 0)

    solver(initial_node, goal_node)



main()
