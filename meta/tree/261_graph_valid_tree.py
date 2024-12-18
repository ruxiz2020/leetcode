class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        if not n:
            return True
        adj = { i:[] for i in range(n) }
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        print(adj) #{0: [1, 2, 3], 1: [0, 4], 2: [0], 3: [0], 4: [1]}

        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False

            visit.add(i)
            for j in adj[i]:
                print(visit)
                if j == prev:
                    print(prev)
                    continue
                if not dfs(j, i):
                    return False
            return True

        return dfs(0, -1) and n == len(visit)


if __name__ == '__main__':

    n = 5
    edges = [[0,1],[0,2],[0,3],[1,4]]

    ss = Solution()
    res = ss.validTree(n, edges)
    print(res)
