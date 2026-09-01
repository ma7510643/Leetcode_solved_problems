class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx>sx and ty>sy:
            if ty>tx:
                ty=ty%tx
            else:
                tx=tx%ty
        if tx==sx and ty>=sy: 
            return (ty-sy)%tx==0
        if ty==sy and tx>=sx:
            return (tx-sx)%ty==0        
        
        return False 

# Additional part of the problem:
sx = int(input("Enter starting 'X' coordinate: "))
sy = int(input("Enter starting 'Y' coordinate: "))
tx = int(input("Enter ending 'X' coordinate: "))
ty = int(input("Enter ending 'Y' coordinate: "))

stmt=Solution.reachingPoints(Solution,sx,sy,tx,ty)
print(stmt)