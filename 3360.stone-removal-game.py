class Solution:
    def canAliceWin(self, n: int) -> bool:
        stone = n # 25
        move = 10
        while stone >= move: # 25>10 # 6>8
            if stone >= move: #25>10 Alice turn
                alice = stone - move #25-10
                stone = alice # 15
                move -= 1 #9
                print("Alice turn")
                if stone >= move: #15>9 bob turn
                    bob = stone - move #15-9
                    stone = bob #6
                    move -= 1 #8
                    print("Bob turn")
                
                else:
                    print("Alice wins")
                    return True
            # else:
            #     print("Bob wins")
            #     return False
        print("Bob wins")         
        return False #alice loss

#timecomplexity O(1) -- without loop
class WithoutLoop:
    def canAliceWin(self, n: int) -> bool:
        s = n # 29
        m = 10
        if s >= m: #25>10 Alice turn
            print("Alice turn")
            alice = s % m #25-10
            s = alice # 15
            m -= 1 #9
            if s >= m: #15>9 bob turn
                print("Bob turn")
                bob = s % m #15-9
                s = bob #6
                m -= 1 #8
                return s%m == 0
            else:
                print("Alice wins")
                return True
        else:
            print("Bob wins")
            return False
            

n = int(input("Enter a number of stone: "))
sts = WithoutLoop.canAliceWin(WithoutLoop,n)
print(sts)