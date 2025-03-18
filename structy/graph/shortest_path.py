# Write a function, shortest_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). 
# The function should return the length of the shortest path between A and B. Consider the length as the number of edges in the path, not the number of nodes. 
# If there is no path between A and B, then return -1. You can assume that A and B exist as nodes in the graph.

from collections import deque

def shortest_path(edges, node_A, node_B):
  graph = create_graph(edges)
  visited = set([node_A])

  q = deque([(node_A, 0)])
  while q:
    curr = q.popleft()
    node, distance = curr
    if node == node_B:
      return distance

    for nbr in graph[node]:
      if nbr not in visited:
        visited.add(nbr)
        q.append((nbr, distance + 1))
        
  return -1  

def create_graph(edges):
  graph = {}
  for edge in edges:
    n1, n2 = edge
    if n1 not in graph:
      graph[n1] = []
    if n2 not in graph:
      graph[n2] = []

    graph[n1].append(n2)
    graph[n2].append(n1)

  return graph