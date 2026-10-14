Maximize Sum of Squares of Digits
=================================

PROBLEM
Given two positive integers num and sum, a positive integer n is "good" if:
  - it has exactly num digits, and
  - its digits add up to exactly sum.

The score of n is the sum of the squares of its digits. Return the good
integer with the maximum score, as a string. If several tie, return the
largest one. If no good integer exists, return "".

EXAMPLES
  num = 2, sum = 3   ->  "30"
  num = 2, sum = 17  ->  "98"
  num = 1, sum = 10  ->  ""

CONSTRAINTS
  1 <= num <= 2 * 10^5
  1 <= sum <= 2 * 10^6

APPROACH (GREEDY)
1. If sum > 9 * num, no valid number exists, so return "".
2. The sum of squares is maximized when digits are as unequal as possible:
   use as many 9s as possible, then one leftover digit, then zeros.
3. Among numbers with that same set of digits, the largest one puts the
   biggest digits first: 9s, then the leftover digit, then 0s.
4. Since sum >= 1, the leading digit is nonzero, so the result always has
   exactly num digits.

Let q = sum // 9 and r = sum % 9.
Result = '9' * q + (str(r) if r else '') + '0' * (num - q - (1 if r else 0))

SOLUTION (Python)
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

COMPLEXITY
  Time:  O(num)
  Space: O(num)
