# Write a function, largest_component, that takes in the adjacency list of an undirected graph. The function should return the size of the largest connected component in the graph.

def largest_component(graph):
  largest = 0
  visited = set()
  
  for node in graph:
    size = get_size(graph, node, visited)
    largest = max(largest, size)

  return largest

def get_size(graph, node, visited):
  if node in visited:
    return 0

  visited.add(node)
  size = 1
  for n in graph[node]:
    size += get_size(graph, n, visited)

  return size