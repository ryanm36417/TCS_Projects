graph = {"A": ["B", "C", "D"],
         "B": ["A", "G"],
         "G": ["B"],
         "C": ["A", "E", "H"],
         "H": ["C", "J", "E"],
         "J": ["H"],
         "D": ["A", "E"],
         "E": ["D", "C", "F", "I"],
         "F": ["E"],
         "I": ["E"], }

visited = []


def depth_first_search(visited, graph, node):
    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            depth_first_search(visited, graph, neighbour)


# 1) when we get to a the end node stop recursing
# 2) true if we reach the end node, false if we dont

def dfs_modified(visited, graph, node, end):
    if node == end:
        visited.append(node)
        return True
    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            solved = dfs_modified(visited, graph, neighbour, end)
            if solved:
                return True
    return False

"""
depth_first_search(visited, graph, "A")
print(visited)
visited.clear()

solved = dfs_modified(visited, graph, "A", "E")
print(visited)
print(solved)
visited.clear()
"""