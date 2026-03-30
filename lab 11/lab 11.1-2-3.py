from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}

print("nachanlyi graf:", graph)

graph['F'] = ['A', 'E']
graph['A'].append('F')
graph['E'].append('F')

print("posle dobavleniya F:", graph)

def get_neighbors(graph, node):
    return graph.get(node, [])

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    print(node, end=' ')

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited

def dfs_stack(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            stack.extend(graph[node])

    return visited

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(graph[node])

    return visited

def has_path(graph, start, end, visited=None):
    if visited is None:
        visited = set()

    if start == end:
        return True

    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            if has_path(graph, neighbor, end, visited):
                return True

    return False

def reachable_count(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])

    return len(visited)

def shortest_path(graph, start, end):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()

        if node == end:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((neighbor, path + [neighbor]))

    return None

start = 'A'
end = 'E'

print("\nSosedi vershini:", get_neighbors(graph, start))

print("\nDFS (rekursivniy):")
dfs(graph, start)

print("\n\nDFS (stek):")
dfs_stack(graph, start)

print("\n\nBFS:")
bfs(graph, start)

print("\n\nsushestvuet li put:", has_path(graph, start, end))

print("kolichestvo dostijimih vershin:", reachable_count(graph, start))

path = shortest_path(graph, start, end)
print("kratchayshiy put:", path if path else "puti net")

#1. Что такое граф? Граф — это структура данных, которая состоит из:
#вершин (узлов)
#рёбер (связей между вершинами)

#2. Чем DFS отличается от BFS?
#DFS (поиск в глубину)
#идёт “вглубь” как можно дальше
#использует стек или рекурсию
#BFS (поиск в ширину)
#идёт “по уровням” (сначала все соседи)
#использует очередь

#3. Почему необходимо хранить visited?
#Множество visited нужно, чтобы:
#не заходить в бесконечный цикл
#не посещать одну и ту же вершину несколько раз

#4. Как представляется граф в Python?
#graph = {
    #'A': ['B', 'C'],
    #'B': ['A']
#}

#5. Какой алгоритм используется для поиска кратчайшего пути?
#В невзвешенном графе → BFS
#Во взвешенном графе → алгоритм Дейкстры