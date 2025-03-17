# Write a function, undirected_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function should return a boolean indicating whether or not there exists a path between node_A and node_B.

def undirected_path(edges, node_A, node_B):
  adj_list = create_graph(edges)
  visited = set()
  
  def dfs(graph, curr, target):
    if curr == target:
      return True
    visited.add(curr)
    for n in graph[curr]:
      if n not in visited and dfs(graph, n, target):
        return True
    return False
  
  return dfs(adj_list, node_A, node_B)

def create_graph(edges):
  graph = {}
  for edge in edges:
    key1, key2 = edge
    if key1 not in graph:
      graph[key1] = []
    if key2 not in graph:
      graph[key2] = []

    graph[key1].append(key2)
    graph[key2].append(key1)
  

  return graph

# def undirected_path(edges, node_A, node_B):
#   graph = build_graph(edges)
#   return has_path(graph, node_A, node_B, set())

# def build_graph(edges):
#   graph = {}
  
#   for edge in edges:
#     a, b = edge
    
#     if a not in graph:
#       graph[a] = []
#     if b not in graph:
#       graph[b] = []
      
#     graph[a].append(b)
#     graph[b].append(a)
    
#   return graph
    
# def has_path(graph, src, dst, visited):
#   if src == dst:
#     return True
  
#   if src in visited:
#     return False
  
#   visited.add(src)
  
#   for neighbor in graph[src]:
#     if has_path(graph, neighbor, dst, visited) == True:
#       return True
    
#   return False
