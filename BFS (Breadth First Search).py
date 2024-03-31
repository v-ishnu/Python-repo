#!/usr/bin/env python
# coding: utf-8

# In[6]:


graph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
    
}

visited = []
queue = []

def bfs (visited,graph,node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        s = queue.pop(0)
        print(s, end= " ")
        
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
#Driver Code                
bfs(visited, graph, 'A')


# In[ ]:





# In[ ]:





# In[ ]:




