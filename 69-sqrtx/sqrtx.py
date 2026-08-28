class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        if x < 2:
            return x
        while left <= right:
            mid = (left + right)//2
            pow_mid = mid*mid
            if pow_mid < x:
                left = mid + 1
            elif pow_mid > x:
                right = mid - 1
            else:
                return mid
        return right
            