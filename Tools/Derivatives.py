import re

class derivative:
    def __init__(self, inputs):
        self.inputs = inputs
    def poly(self):
        new_func = re.split(r'[+-]', self.inputs)
        signs = [a for a in self.inputs if a == '-' or a == '+']
        if '' in new_func: #Remove '' in list from seperation of string including - first coefficient
            new_func.remove('')
            
        for x in new_func: #polynomials
            if 'x' in x: #Works if it has a variable
                if '^' in x: #If term has a degree >=2
                    exponent = int(x[x.index('^')+1:])
                    coefficient = int(x[:x.index('x')])
                    new_func[new_func.index(x)] = x.replace(str(coefficient),'')
                    x = x.replace(str(exponent),'')


                else:
                    x = x.replace('x','') #Remove the x in first degree monomial
                   
            else:
                new_func.remove(x) #Remove the constant from the split string
                signs.pop() #This will remove the sign related to the constant
                   
derivative('2x^2+6x+9').poly()


import re

class derivative:
    def __init__(self, inputs):
        self.inputs = inputs
    def poly(self):
        new_func = [x for x in re.split(r'[()]', self.inputs) if x != '']
        signs = [a for a in self.inputs if a == '-' or a == '+']
        
        

        print(new_func)
        print(signs)
derivative('(2x^-2)+(6x^4)+(9)').poly()






'''
Sources:
https://docs.python.org/3/library/re.html
https://www.geeksforgeeks.org/python-split-multiple-characters-from-string/

'''





'''
Sources:
https://docs.python.org/3/library/re.html
https://www.geeksforgeeks.org/python-split-multiple-characters-from-string/


'''
