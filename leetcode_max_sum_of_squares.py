class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        q, r = divmod(sum, 9)
        res = "9" * q
        used = q
        if r:
            res += str(r)
            used += 1
        res += "0" * (num - used)
        return res