from itertools import chain
from queue import PriorityQueue
from dataclasses import dataclass, field
from copy import deepcopy

class Node:
    pass



@dataclass
class Node:
    state: list[[int]]
    x: int
    y: int
    cost: int
    level: int
    parent: Node = None

    def __lt__(self, other):
        return self.cost > other.cost


row = [1, 0, -1, 0]
col = [0, -1, 0, 1]


def print_state(state):
    for i in range(3):
        for j in range(3):
            print(f"{state[i][j]} ", end='')
        print("")


def compare_states(node1, node2):
    for i in range(3):
        for j in range(3):
            if node1.state[i][j] != node2.state[i][j]:
                return False

    return True


def print_path(counter, root):
    if root is None:
        return

    print_path(counter, root.parent)
    print_state(root.state)
    counter += 1

    print("\n")


def valid_swap(x, y):
    return (x >= 0) and (x < 3) and ((y >= 0) and y < 3)


def is_node_in_list(node, node_list):

    for i in node_list:

        if compare_states(node, node_list[i]):
            return True
    return False


def calculate_misplaced_tiles(node1, goal_node):
    count = 0

    for i in range(3):
        for j in range(3):
            if node1.state[i][j] != goal_node.state[i][j]:
                count += 1

    return count


def manahattan_distance(initial_state, goal_state):
    result = 0

    for i in range(3):
        for j in range(3):
            for goalRow in range(3):
                for goalColumn in range(3):
                    if initial_state[i][j] and initial_state[i][j] == goal_state[goalRow][goalColumn]:
                        result = result + abs(i - goalRow) + abs(j - goalColumn)
                        break

    return result


def list_to_key(state):
    flatten_list = list(chain.from_iterable(state))
    result = ''.join(str(e) for e in flatten_list)

    return result


def new_node(node, new_x, new_y):
    temp_node = deepcopy(node)

    old_state = temp_node.state
    old_x = temp_node.x
    old_y = temp_node.y
    old_level = temp_node.level
    parent = temp_node

    temp_state = old_state[old_x][old_y]

    new_state = old_state

    new_state[old_x][old_y] = new_state[new_x][new_y]
    new_state[new_x][new_y] = temp_state


    # cost will be calculated later, but for safety it is not zero
    node = Node(new_state, new_x, new_y, 10000, old_level + 1, parent)

    return node


def solver(init_node, goal_node):
    open_list = PriorityQueue()
    closed_list = {}

    initial_node = init_node
    goal_node = goal_node

    initial_node.cost = manahattan_distance(initial_node.state, goal_node.state)

    open_list.put(initial_node)


    counter = 0

    while not open_list.empty():

        min_node = open_list.get()

        closed_list[list_to_key(min_node.state)] = min_node

        if compare_states(min_node, goal_node):
            print_path(counter, min_node)
            print("\n Steps: " + str(counter - 1) + "\n")

            return

        # Expand the children

        # row[] = [1, 0, -1, 0]

        # col = [0, -1, 0, 1]

        for i in range(4):
            #print(closed_list)
            if valid_swap(min_node.x + row[i], min_node.y + col[i]):
                print("hej")
                child = new_node(min_node, min_node.x + row[i], min_node.y + col[i])

                child.cost = manahattan_distance(child.state, goal_node.state)
                open_list.put(child)
                if not is_node_in_list(child, closed_list):
                    open_list.put(child)


def main():
    initial_node = Node([
        [5, 6, 7],
        [4, 0, 8],
        [3, 2, 1]
    ], 0, 0, 0, 0)

    goal_node = Node([
        [1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]
    ], 0, 1, 0, 0)

    solver(initial_node, goal_node)

    # print(valid_swap(1, 1))


main()
