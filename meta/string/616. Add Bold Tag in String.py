class Solution:
    def addBoldTag(self, s: str, words: list[str]) -> str:
        n = len(s)
        ans = []
        # bold[i] := True if s[i] should be bolded
        bold = [0] * n

        boldEnd = -1  # s[i:boldEnd] should be bolded
        for i in range(n):
            for word in words:
                if s[i:].startswith(word):
                    boldEnd = max(boldEnd, i + len(word))
            print(boldEnd)
            bold[i] = boldEnd > i
        print(bold)

        # Construct the with bold tags
        i = 0
        while i < n:
            if bold[i]:
                j = i
                while j < n and bold[j]:
                    j += 1
                # `s[i..j)` should be bolded.
                ans.append('<b>' + s[i:j] + '</b>')
                i = j
            else:
                ans.append(s[i])
                i += 1

        return ''.join(ans)


s = "abcxyz123"; words = ["abc","123"]

res = Solution().addBoldTag(s, words)
print(res) #<b>abc</b>xyz<b>123</b>
