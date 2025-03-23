from collections import deque
class Solution(object):

    def intersect(self, a,b):
        return list(set(a) & set(b))
    
    def numberOfComponents(self, properties, k):
        """
        :type properties: List[List[int]]
        :type k: int
        :rtype: int
        """
        # ©leetcode
        n = len(properties)
    
        # Build adjacency list representation of the graph
        graph = [[] for _ in range(n)]
        
        # Helper function to count distinct integers common to both arrays
        def intersect(a, b):
            return len(set(a) & set(b))
        
        # Construct the graph
        for i in range(n):
            for j in range(i + 1, n):  # Only need to check each pair once for undirected graph
                if intersect(properties[i], properties[j]) >= k:
                    graph[i].append(j)
                    graph[j].append(i)
        
        # BFS to count connected components
        visited = [False] * n
        component_count = 0
        
        for i in range(n):
            if not visited[i]:
                component_count += 1
                
                # BFS to mark all nodes in this component
                queue = deque([i])
                visited[i] = True
                
                while queue:
                    node = queue.popleft()
                    
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
        
        return component_count
a = Solution()
print(a.numberOfComponents([[1,2],[1,1],[3,4],[4,5],[5,6],[7,7]],1))
print(a.numberOfComponents([[1,2,3],[2,3,4],[4,3,5]], 2))
print(a.numberOfComponents([[1,1],[1,1]],2))