# Write a function, has_path, that takes in a dictionary representing the adjacency list of a directed acyclic graph and two nodes (src, dst). The function should return a boolean indicating whether or not there exists a directed path between the source and destination nodes.

# from collections import deque

# Recursive
def has_path(graph, src, dst):
  if src == dst:
    return True
  for n in graph[src]:
    if has_path(graph, n, dst):
      return True

  return False

# Iterative
# def has_path(graph, src, dst):
#   stack = [src]
#   while stack:
#     curr = stack.pop()
#     if curr == dst:
#       return True
#     for n in graph[curr]:
#       stack.append(n)

#   return False

# BFS
# def has_path(graph, src, dst):
#   q = deque([src])
#   while q:
#     curr = q.popleft()
#     if curr == dst:
#       return True
#     for n in graph[curr]:
#       q.append(n)

#   return False