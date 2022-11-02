class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        d = defaultdict(lambda : False)
        d1 = defaultdict(lambda : False)
        for i in bank:
            d[i] = True
        q = [start]
        d1[start] = True
        lev = -1
        while(len(q) != 0):
            n = len(q)
            lev += 1
            for i in range(n):
                s = q[0]
                if(s == end):
                    return lev
                for j in range(len(s)):
                        for k in "ACGT":
                            nn = s[:j] + k + s[j+1:]
                            if(d[nn] and not d1[nn]):
                                q.append(nn)
                                d1[nn] = True
                q.pop(0)
        return -1
                
                                
        