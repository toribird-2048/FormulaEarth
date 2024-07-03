#最初(未完成)
import random

levelupCost = 1

class Formula() :
    def __init__(self,*formula) :
        """
        coefficient:係数
        dimention:次数
        formula:[xの係数,xの次数]
        """
        self.__formula = list(formula)
    
    def calc(self,x) :
        ans = 0
        for k in range(len(self.__formula)) :
            ans += self.__formula[k][0] * (x ** self.__formula[k][1])
        return ans
    
    def getFormula(self) :
        return self.__formula

    def getDimension(self) :
        dimentions = []
        for k in self.__formula :
            dimentions.append(k[1])
        return dimentions

    def getCoefs(self) :
        coefs = []
        for k in self.__formula :
            coefs.append(k[0])
        return coefs
    
    def changeCoef(self,dimention,change) :
        if dimention not in self.getDimention :
            raise ValueError()
        dimentionNum = self.getDimention.index(dimention)
        self.__formula[dimentionNum][0] += change

    def changeDimention(self,dimention) :
        pass


class Earth() :
    def __init__(self,limit,sample) :
        self.limit = limit
        self.list = []
        self.sample:Formula = sample

    def randomGen(self,num,dimCenter,dimRange,coefMin,coefMax):
        """
        --range--ave--range--
        整数次数
        """
        dim_min = dimCenter - dimRange
        dim_max = dimCenter + dimRange
        tempList = []
        for k in range(dim_min,dim_max + 1) :
            tempList.append([k,random.uniform(coefMin,coefMax)])
        for k in range(num) :
            self.list.append(Formuler(Formula(*tempList)))


class Formuler(Formula) :
    def mutation(self,rate) :
        if random.uniform(0,1) < rate :
            self.Formula


f = Formula([3,2],[2,1],[1,0])
print(f.calc(1))
print(f.getCoefs())