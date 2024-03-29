class Solution(object):
    def alienOrder(self, words):
        '''topological sort (DAG)
        or post order DFS'''
        adj = { c: set() for w in words for c in w }

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visit = {} # False=visited, True=visited & current path
        res = []
        def dfs(c):
            if c in visit: # loop
                return visit[c]

            visit[c] = True

            for nei in adj[c]:
                if dfs(nei):
                    return True

            visit[c] = False # no longer in current path
            res.append(c) # post order DFS

        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)
