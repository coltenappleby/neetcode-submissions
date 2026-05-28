class Solution:
    def minWindow(self, s: str, t: str) -> str:
        shortest_L = 0
        shortest_R = len(s)
        L = 0
        counts = {item: t.count(item) for item in set(t)}
        for R in range(len(s)):
            if s[R] in counts:
                counts[s[R]] -= 1
                if max(counts.values()) == 0:   
                    if R-L < shortest_R - shortest_L:
                        shortest_L = L
                        shortest_R = R
                while max(counts.values()) <= 0:
                    if s[L] in counts:
                        counts[s[L]] += 1     
                    L += 1       
                    
                    if max(counts.values()) == 0:
                        if R-L < shortest_R - shortest_L:
                            shortest_L = L
                            shortest_R = R



        if shortest_R == len(s):
            return ""
        else:
            return s[shortest_L:shortest_R+1]
