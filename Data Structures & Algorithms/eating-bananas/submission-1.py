class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        m = max(piles)

        #we essentially are searching for a median time each step
        #we must also test it, it CANNOT leave remaining bananas
        #in such case, we search for a more efficient sol'n, higher window
        #if we have remaining hours, we do a lower window until we are done

        l, r = 1, m
        res = r

        while l <= r:
            k = (l + r) // 2
            tot = 0
            for p in piles:
                #tot += p // k
                tot += math.ceil(float(p)/k)
            if tot <= h: # >=
                res = k # add
                r = k - 1 # add
            else:
                l = k + 1 # add
        return res

