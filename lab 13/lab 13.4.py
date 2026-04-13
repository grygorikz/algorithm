#4 блок 16 задание
#ГРАФ 
graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5],
    3: [],
    4: [],
    5: []
}

#DFS РЕКУРСИЯ
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    print(node, end=' ')

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

#DFS СТЕК
def dfs_stack(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            print(node, end=' ')
            stack.extend(reversed(graph[node]))

#ЗАПУСК
print("Rekursivniy DFS:")
dfs_recursive(graph, 0)

print("\nDFS cherez stek:")
dfs_stack(graph, 0)