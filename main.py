import random

levelup_cost = 1
mutation_rate = 0.5
mutation_dim_range = 2
mutaiton_coef_range = 2

class Formula() :
    def __init__(self,formula) :
        """
        coefficient,coef:係数
        dimension,dim:次数
        formula:{dim1:coef1,dim2:coef2,......}
        """
        self.__formula:dict = formula

    def calc(self,x) :
        ans = 0
        for dim,coef in self.__formula.items() :
            ans += coef * (x ** dim)
        return ans

    def get_formula(self) :
        return self.__formula
    
    def get_dim(self) :
        return list(self.__formula.keys())

    def get_coef(self,dim=all) :
        if dim == all :
            return list(self.__formula.values())
        elif dim in self.__formula.keys() :
            return self.__formula[dim]
        else :
            return
        
    def add_term(self,dim,coef) :
        if dim in self.__formula.keys() :
            self.__formula[dim] += coef
        else :
            self.__formula[dim] = coef

    def del_term(self,dim) :
        if dim in self.__formula.keys() :
            del self.__formula[dim]

    def zero_check(self):
        for coef in self.__formula.values() :
            if coef == 0 :
                self.del_term(self.__formula.keys()[self.__formula.values().index(coef)])
    
class Earth() :
    def __init__(self,limit,sample) :
        self.__limit:int = limit
        self.__list = []
        self.__sample:Formula = sample

    def randomGen(self,dim_min,dim_max,coef_min,coef_max) :
        terms = {}
        for k in range(dim_min,dim_max + 1) :
            terms[k] = random.uniform(coef_min,coef_max)
        for k in range(self.__list) :
            pass


class Formuler() :
    def __init__(self,formula) :
        self.__formula:Formula = formula
        super().__init__(formula)
    
    def mutation(self) :
        if random.uniform(0,1) > mutation_rate :
            return
        else :
            selected_dim = random.choice(self.__formula.get_dim())
            coef = self.__formula.get_coef(selected_dim)
            self.__formula.add_term(selected_dim + random.random(-mutation_dim_range,mutation_dim_range + 1),coef + random.uniform(-mutaiton_coef_range,mutaiton_coef_range))
            self.__formula.zero_check()

