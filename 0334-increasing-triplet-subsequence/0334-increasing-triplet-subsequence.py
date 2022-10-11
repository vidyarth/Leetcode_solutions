class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        ok1 = float("inf")
        ok2 = ok1
        for i in nums:
            if i <= ok1:
                ok1 = i
            elif i <= ok2:
                ok2 = i
            else:
                return True
        return False