class Solution:
    def angleClock(self, h: int, m: int) -> float:
        m=abs(30*h - 5.5*m)
        return 360-m if m>180 else m
        