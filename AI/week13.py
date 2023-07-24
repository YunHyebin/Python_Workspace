def dfs(graph, start_node):
  stack = list()
  visit = list()
  stack.append(start_node)
  while stack:
    node = stack.pop()
    if node not in visit:
      visit.append(node)
    stack.extend(reversed(graph[node]))
  return visit
graph={1:[2,7,8],2:[1,3,6],3:[2,4,5],4:[3],5:[3],6:[2],7:[1],
8:[1,9,12],9:[8,10,11],10:[9],11:[9],12:[8]}
print(dfs(graph,1))

# def bfs(graph, start_node):
#   queue = list()
#   visit = list()
#   queue.append(start_node)
#   while queue:
#     node = queue.pop(0)
#     if node not in visit:
#        visit.append(node)
#        queue.extend((graph[node]))
#   return visit
# graph={1:[2,7,8],2:[1,3,6],3:[2,4,5],4:[3],5:[3],6:[2],7:[1],
# 8:[1,9,12],9:[8,10,11],10:[9],11:[9],12:[8]}
# print(bfs(graph,1))

