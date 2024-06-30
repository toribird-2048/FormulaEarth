import random

levelup_cost = 1
mutation_rate = 0.5
mutation_dim_range = 2
mutaiton_coef_range = 2
calc_interval = 1

def expanded_range(start,interval,num):
    return [start + k * interval for k in range(num)]

def get_keys_from_value(dict, val):
    return [k for k, v in dict.items() if v == val]

def sort_by_values(dict) :
    sorted_dict_tupple = sorted(dict.items(), key=lambda x:x[1])
    return {k:v for k,v in sorted_dict_tupple}

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

    def zero_check(self) :
        zero_list = get_keys_from_value(self.__formula,0)
        for dim in zero_list :
            self.del_term(dim)


class Formuler() :
    def __init__(self,formula) :
        self.__formula:Formula = formula

    def mutation(self) :
        if random.uniform(0,1) > mutation_rate :
            return
        else :
            selected_dim = random.choice(self.__formula.get_dim())
            coef = self.__formula.get_coef(selected_dim)
            self.__formula.add_term(selected_dim + random.randint(-mutation_dim_range,mutation_dim_range + 1),coef + random.uniform(-mutaiton_coef_range,mutaiton_coef_range))
            self.__formula.zero_check()

    def get_formula(self) :
        return self.__formula.get_formula()
    
    def calc(self,x) :
        return self.__formula.calc(x)


class Earth() :
    def __init__(self,limit,sample,initial_level,dim_min,dim_max,coef_min,coef_max,mutation_add_num) :
        """
        limit,sample,initial_level,dim_min,dim_max,coef_min,coef_max
        """
        self.__limit:int = limit
        self.__list = []
        self.__sample:Formula = sample
        self.__level:int = initial_level
        self.__dim_min:int = dim_min
        self.__dim_max:int = dim_max
        self.__coef_min:float = coef_min
        self.__coef_max:float = coef_max
        self.__mutation_add_num:int = mutation_add_num
        self.randomGen(limit)

    def randomGen(self,num) :
        terms = {}
        for l in range(num) :
            terms = {}
            for k in range(self.__dim_min,self.__dim_max + 1) :
                terms[k] = random.uniform(self.__coef_min,self.__coef_max)
            self.__list.append(Formuler(Formula(terms)))

    def get_list(self) :
        return [k.get_formula() for k in self.__list]
    
    def get_formuler(self) :
        return self.__list
    
    def get_sample(self) :
        return self.__sample.get_formula()

    def sample_calc(self,x) :
        return self.__sample.calc(x)
    
    def get_level(self) :
        return self.__level
    
    def sort(self) :
        sample_results = [self.sample_calc(k) for k in expanded_range(0,calc_interval,self.__level)]
        formulers_results = {}
        for k in self.__list :
            formulers_results[k] = sum([abs(k.calc(l) - sample_results[l]) for l in expanded_range(0,calc_interval,self.__level)])
        formula_reuslts = sort_by_values(formulers_results)
        self.__list = [Formuler(Formula(k)) for k in formula_reuslts.keys()]

    def mutation(self) :
        for l in range(self.__mutation_add_num) :
            for k in self.__list :
                k.mutation()
                self.__list.append(k)


earth = Earth(10,Formula({1:1}),10,0,9,0,9,1)
earth.mutation()
earth.sort()
#print(earth.get_formuler())
