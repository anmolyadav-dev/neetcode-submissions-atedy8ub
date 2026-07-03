class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ct=0
        while left != right:
            left=left>>1
            right=right>>1
            ct+=1
        return left<<ct