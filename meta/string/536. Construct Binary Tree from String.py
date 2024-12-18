# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def str2tree(self, s: str) -> TreeNode:
        def dfs(s):
            if not s:
                return None
            p = s.find('(')
            if p == -1:
                # print(s)
                return TreeNode(int(s))
            root = TreeNode(int(s[:p]))
            start = p
            cnt = 0
            for i in range(p, len(s)):
                if s[i] == '(':
                    cnt += 1
                elif s[i] == ')':
                    cnt -= 1
                if cnt == 0:
                    if start == p:
                        print("left" + s[start + 1 : i])
                        print(start, p, i)
                        root.left = dfs(s[start + 1 : i])
                        start = i + 1
                    else:
                        print("right" + s[start + 1 : i])
                        print(start, p, i)
                        root.right = dfs(s[start + 1 : i])
            return root

        return dfs(s)


s = "4(2(3)(1))(6(5))"

res = Solution().str2tree(s)
