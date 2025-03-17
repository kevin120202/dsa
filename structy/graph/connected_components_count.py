# Write a function, connected_components_count, that takes in the adjacency list of an undirected graph. The function should return the number of connected components within the graph.

def connected_components_count(graph):
  count = 0
  visited = set()

  def dfs(curr):
    if curr in visited:
      return
    visited.add(curr)
    for n in graph[curr]:
      dfs(n)

  for node in graph:
    if node not in visited:
      count += 1
      dfs(node)
    
  return count