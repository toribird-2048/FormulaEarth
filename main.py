class Formula :
    def __init__(self,*coef) :
        """
        coefficient:係数
        coef:[xの係数,xの次数]
        """
        self.coef = list(coef)
    
    def calc(self,x) :
        ans = 0
        for k in range(len(self.coef)) :
            ans += self.coef[k][0] * (x ** self.coef[k][1])
        return ans

F = Formula([2,0],[4,1])
print(F.calc(0))