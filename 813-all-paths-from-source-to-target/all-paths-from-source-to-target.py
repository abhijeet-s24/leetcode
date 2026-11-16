class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        res=[]
        path=[0]
        def dfs(node):
            if node==len(graph)-1:
                res.append(path.copy())
                return 
            for neigh in graph[node]:
                path.append(neigh)
                dfs(neigh)
                path.pop()
        dfs(0)
        return res