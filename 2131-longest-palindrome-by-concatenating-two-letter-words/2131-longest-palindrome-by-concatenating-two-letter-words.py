class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ans = 0
        d = defaultdict(lambda : 0)
        for i in words:
            d[i] += 1
        ok = False
        for i in words:
            if(i[0] != i[1]):
                if(d[i] > 0 and d[i[::-1]] > 0):
                    ans += 4
                    d[i[::-1]] -= 1
                    d[i] -= 1
            else:
                if(d[i] > 1):
                    ans += 4
                    d[i] -=2
                elif (d[i] == 1):
                    ok = True
        
        if(ok):
            ans += 2
        
        return ans
        