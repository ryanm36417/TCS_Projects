from DataStructures.queue.queue import Queue

graph = {"A": ["B", "C", "D"],
         "B": ["A", "G"],
         "G": ["B"],
         "C": ["A", "E", "H"],
         "H": ["C", "J", "E"],
         "J": ["H"],
         "D": ["A", "E"],
         "E": ["D", "C", "F", "I"],
         "F": ["E"],
         "I": ["E"]
         }


visited = []
queue = Queue()
tracer = {}
path = []


def bfs(node):
    visited.append(node)
    queue.push(node)
    while not queue.is_empty():
        node = queue.peek()
        queue.pop()
        print(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.push(neighbour)
                visited.append(neighbour)


def bfs_mod(node, end):
    visited.append(node)
    queue.push(node)
    while not queue.is_empty():
        node = queue.peek()
        queue.pop()
        if node == end:
            return True
        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.push(neighbour)
                visited.append(neighbour)
                tracer.update({neighbour: node})
    return False


def get_path(node):
    path.insert(0, node)
    if node in tracer:
        get_path(tracer[node])

"""
solvable = bfs_mod("A", "F")
print(visited)
print(solvable)
print(tracer)
get_path("F")
print(path)
"""
































