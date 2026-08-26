class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        xdiff=abs(sx-fx)
        ydiff=abs(sy-fy)
        if xdiff==0 and ydiff==0 and t==1:
            return False
        return min(xdiff,ydiff)+abs(xdiff-ydiff)<=t

        