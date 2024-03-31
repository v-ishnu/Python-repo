#!/usr/bin/env python
# coding: utf-8

# In[2]:


graph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
    
}

visited = set()

def dfs (visited,graph,node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
            
# Drive Code
dfs (visited, graph, 'A')


# In[ ]:




